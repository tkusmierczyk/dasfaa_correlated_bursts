#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Indexing of bursts from many timelines."""

import time
import sys
sys.path.append("../")

from base.bursts import *
from base.bursts_filtering import *
from base.bursts_stats import *
from base.bursts_jaccard import *

from bursts_index import *

from itertools import *


MAX_BURSTS_PER_CHUNK = 200000


def calc_time2active(name2bursts, element_constructor = lambda name, ix, first, last: (name, ix, first, last) ):
    """Calculates list[time] -> list of tuples (name, ix, first, last) representing bursty entities in time."""
    maxt = max(last1+1 for name, bursts in name2bursts for level1, first1, last1 in bursts)
    time2active = list( list() for i in xrange(maxt+1) )

    for name, bursts in name2bursts:    
        for ix, (level, first, last) in enumerate(bursts):                               
            for t in xrange(first, last+1):
                time2active[t].append( element_constructor(name, ix, first, last) ) 

    return time2active


calc_time2names = lambda name2bursts: calc_time2active(name2bursts, \
                                        element_constructor=lambda name, ix, first, last: name)



class IndexElement:

    def __init__(self, name, ix, first, last):
        self.object = (name, [ix])
        self.bounds = (first, last)


class IntervalIndex:

    def __init__(self, name2bursts=list()):
        self.time2active = calc_time2active(name2bursts)

    def intersection(self, bounds, objects=True):
        matching = list()
        first, last = bounds
        for t in xrange(first, last+1): matching.extend( self.time2active[t] )
        return list( IndexElement(name, ix, first, last) for name, ix, first, last in set(matching) )

    def calculate_canidadates_set(self): 
        """Calculates pair2overlaps = {(name1,name2): count}.
           
           Each pair is included twice:
            for key (name1,name2) count is for bursts from stream of name1 overlapping with these from stream of name2.
            for key (name2,name1) count is for bursts from stream of name2 overlapping with these from stream of name1.
         """
        print "[calculate_canidadates_set][%f] Calculating candidates set" % (time.clock())
        pair2overlaps, prev    = dict(), set()
        overlaps                = dict() #(name, ix) -> list of names
        for t in xrange(len(self.time2active)):

            if t>0 and t%5000==0:
                print "[calculate_canidadates_set][%f]  %i/%i processed; candidates set size = %i" % \
                        (time.clock(), t, len(self.time2active), len(pair2overlaps)/2)

            active  = set( self.time2active[t] )
            new     = list( active.difference(prev) )
            old     = list( active.difference(new) )
            end     = list( prev.difference(active) )
            prev    = active

            for name, ix, first, last in end:
                if (name, ix) in overlaps: overlaps.pop( (name, ix) )           

            for i, (name1, ix1, first1, last1) in enumerate(new):
                for j in xrange(i+1, len(new)): 
                    name2, ix2, first2, last2 = new[j] 

                    if name2 not in overlaps.get((name1,ix1), set()):
                        pair2overlaps[(name1, name2)] = pair2overlaps.get((name1, name2), 0) + 1
                        overlaps.setdefault( (name1, ix1), set() ).add(name2)
                    if name1 not in overlaps.get((name2,ix2), set()):
                        pair2overlaps[(name2, name1)] = pair2overlaps.get((name2, name1), 0) + 1
                        overlaps.setdefault( (name2, ix2), set() ).add(name1)

            for name1, ix1, first1, last1 in old:
                for name2, ix2, first2, last2 in new: 

                    if name2 not in overlaps.get((name1,ix1), set()):
                        pair2overlaps[(name1, name2)] = pair2overlaps.get((name1, name2), 0) + 1
                        overlaps.setdefault( (name1, ix1), set() ).add(name2)
                    if name1 not in overlaps.get((name2,ix2), set()):
                        pair2overlaps[(name2, name1)] = pair2overlaps.get((name2, name1), 0) + 1
                        overlaps.setdefault( (name2, ix2), set() ).add(name1)

        #pair2overlaps = sorted(pair2overlaps.iteritems(), key=lambda k: k[1], reverse=True)
        #print sorted(pair2overlaps.iteritems(), key=lambda k: k[1], reverse=True)[:10]
        print "[calculate_canidadates_set][%f] Candidates set size = %i" % (time.clock(), len(pair2overlaps)/2)
        return pair2overlaps


def validate_canidadates_set(pair2overlaps, name2bursts_dict, JT):
    """Calculates list of candidates for which Jaccard >= JT."""
    #print "[validate_canidadates_set][%f] Validating candidates set of size %i " % \
    #        (time.clock(), len(pair2overlaps)/2)

    pair2jaccard    = list()
    for (name1, name2), overlaps in pair2overlaps.iteritems():   
        if name1 > name2: continue
        overlapping = min(pair2overlaps[(name1, name2)], pair2overlaps[(name2, name1)])
        e1          = len(name2bursts_dict[name1])
        e2          = len(name2bursts_dict[name2])
        JI          = float(overlapping) / (e1+e2-overlapping)
        if JI >= JT: 
            pair2jaccard.append( ((name1, name2), JI) )  

    print "[validate_canidadates_set][%f] %i/%i above threshold JT=%.3f" % \
            (time.clock(), len(pair2jaccard), len(pair2overlaps)/2, JT)
    return pair2jaccard


def build_1D_bursts_index(name2bursts):   
    """ Constructs index of single bursts."""       
    print "[build_1D_bursts_index][%f] Builiding index out of %i entities" % (time.clock(), len(name2bursts))
    return IntervalIndex(name2bursts)


def test_1D_bursts_index(name2bursts, numbursts2entities, range_first, range_last):
    """Validates if 1D index returns properly value of min(overlapping1, overlapping2)"""
    entities        = extract_entities_subset(numbursts2entities, xrange(range_first, range_last+1) )
    idx             = build_1D_bursts_index(entities)  
    pair2overlaps   = idx.calculate_canidadates_set()
    name2bursts     = dict(name2bursts)

    ok = True
    for pair, count in pair2overlaps.iteritems():
        name1, name2    = pair 
        overlaps_index  = min(pair2overlaps[(name1,name2)], pair2overlaps[(name2,name1)])
        overlaps_naive  = calc_num_overlapping(name2bursts[name1], name2bursts[name2])
        ok              = overlaps_index==overlaps_naive
        if not ok:
            print pair2overlaps[(name1,name2)], pair2overlaps[(name2,name1)]
            print "calc_num_overlapping=", calc_num_overlapping(name2bursts[name1], name2bursts[name2])
            print "bursts1 =", name2bursts[name1]
            print "bursts2 =", name2bursts[name2]
            print print_overlapping(name2bursts[name1], name2bursts[name2])
            ok = False            
    return ok


def identify_linked_pairs(name2bursts, JT, output_storage, max_bursts_per_chunk=100000):
    if len(name2bursts)<=0: return

    name2bursts_dict    = dict(name2bursts)
    chunks  = name2bursts_chunks(name2bursts, max_bursts_per_chunk)
    print "[calc_burstpair2index][%f] %i entities split into  %i chunks of max size: %i" \
                % (time.clock(), len(name2bursts), len(chunks), max_bursts_per_chunk)

    if len(chunks)==1:
        idx             = build_1D_bursts_index(chunks[0])   
        pair2overlaps   = idx.calculate_canidadates_set()
        pair2jaccard    = validate_canidadates_set(pair2overlaps, name2bursts_dict, JT)
        output_storage.store_batch(pair2jaccard)

    for chunk1, chunk2 in combinations(chunks, 2):
        idx             = build_1D_bursts_index(chunk1+chunk2)   
        pair2overlaps   = idx.calculate_canidadates_set()
        pair2jaccard    = validate_canidadates_set(pair2overlaps, name2bursts_dict, JT)
        output_storage.store_batch(pair2jaccard)


def identify_linked_pairs_with_1D_index(numbursts2entities, JT, output_storage, \
                                        minbursts=3, maxbursts=10000, max_bursts_per_chunk=100000):
    numbursts_range = range(minbursts, maxbursts+1)
    considered = set()

    print "[identify_linked_pairs_with_1D_index][%f] Considering combinations from range %s:" % \
                (time.clock(), str(numbursts_range))
    for n1, n2 in combinations(numbursts_range, 2):
        if n1<numbursts_lower_bound(n2, JT): continue
        considered.add(n1); considered.add(n2)
        selected1 = numbursts2entities.get(n1, list())
        selected2 = numbursts2entities.get(n2, list())
        if len(selected1)<=0 or len(selected2)<=0: continue
        print "[identify_linked_pairs_with_1D_index][%f] Considering %i vs. %i" % (time.clock(), n1, n2)
        identify_linked_pairs(selected1+selected2, JT, output_storage, max_bursts_per_chunk)
        print "[identify_linked_pairs_with_1D_index][%f] Current output size: %i" % (time.clock(), output_storage.stored_count())

    print "[identify_linked_pairs_with_1D_index][%f] Not considered in any combinations from range %s:" % \
                (time.clock(), str(numbursts_range))
    for n in numbursts_range:
        if n in considered: continue
        selected = numbursts2entities.get(n, list())
        if len(selected)<=0: continue
        print "[identify_linked_pairs_with_1D_index][%f] Considering %i" % (time.clock(), n)
        identify_linked_pairs(selected, JT, output_storage, max_bursts_per_chunk)
        print "[identify_linked_pairs_with_1D_index][%f] Current output size: %i" % (time.clock(), output_storage.stored_count())


###############################################################################


def main(argv=list()):
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[bursts_index_1D] The script reads bursts and correlates them."
    
    try:    path = argv[1]
    except: sys.stderr.write("[bursts_index_1D] Arg expected: input data file!\n"); sys.exit(-1)

    try:    JT = float(argv[2])
    except: sys.stderr.write("[bursts_index_1D] Arg expected: JT!\n"); sys.exit(-1)

    try:    min_numbursts, max_numbursts = int(argv[3]), int(argv[4])
    except: sys.stderr.write("[bursts_index_1D] Args expected: Min and max number of bursts!\n"); sys.exit(-1)


    max_bursts_per_chunk = MAX_BURSTS_PER_CHUNK
    print "[bursts_index_1D] JT=%.4f min_numbursts=%i max_numbursts=%i max_bursts_per_chunk=%i" % \
            (JT, min_numbursts, max_numbursts, max_bursts_per_chunk)
    marker = "%s_%i_%i_%i" % (("%f"%JT).rstrip('0'), min_numbursts, max_numbursts, max_bursts_per_chunk)


    storage_file = open(path+".index_1D_%s" % marker, "w")
    output_storage = JIOutputStorage(storage_file)
    print "[bursts_index_1D] Storage file: %s" % str(storage_file)

    print "[bursts_index_1D] Loading data from %s" % path
    name2bursts = list( yield_name2bursts(open(path)) )
    print "[bursts_index_1D][%f] %i loaded in total" % (time.clock(), len(name2bursts))

    #data_size, tmin, tmax, bursts_stats = bursts_stats(name2bursts)
    #print  "[bursts_index_1D]","N =",data_size,"tmin =", tmin,"tmax =", tmax, "bursts_stats =", bursts_stats
        
    print "[bursts_index_1D][%f] Computing numbursts2entities" % (time.clock())
    numbursts2entities = calc_numbursts2entities(name2bursts, element_constructor = lambda name, bursts: (name, bursts))
    #print_key2entities(numbursts2entities.iteritems(), fout, entities_formatter = lambda entities: "%i" % len(entities))
    
    print "[bursts_index_1D][%f] Starting for %s" % (time.clock(), marker)
    identify_linked_pairs_with_1D_index(numbursts2entities, JT, output_storage, min_numbursts, max_numbursts, max_bursts_per_chunk)
    print "[bursts_index_1D][%f] Done for %s. %i pairs generated." % (time.clock(), marker, output_storage.stored_count())


if __name__=="__main__":
    main(sys.argv)




