#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Indexing and correlation of bursts from many timelines using R-trees."""

import time
import sys
sys.path.append("../")

from base.bursts import *
from base.bursts_filtering import *
from base.bursts_stats import *
from base.bursts_jaccard import *
from base.aux import *

from bursts_index import *
from itertools import combinations, combinations_with_replacement

from rtree import index

###############################################################################


"""MAX_REPEATED_POSITIONS_LIMIT - additional assumption on data: no burst overlaps with more that this many+1 
    e.g. for MAX_REPEATED_POSITIONS_LIMIT=2 we assume the situation where single burst overlapping
    with more than 3 bursts is impossible."""
MAX_REPEATED_POSITIONS_LIMIT = 1


def yield_bursts_ids(bursts, d, max_positions_repeated):
    """Constructs tuples of <d>-size substes of bursts. 

    Args:
        max_positions_repeated - each bursts can be included in the bbox this many times+1.
            e.g. max_positions_repeated=3 means that we need to consider situation when one burst can overlap with even four bursts
            therefore we need to include such situation by repeating it four times
            This parameter is limited by global MAX_REPEATED_POSITIONS_LIMIT.
    """
    bursts_ids = range(len(bursts))

    #All the combinations where any element is repeated once:
    for ids in combinations(bursts_ids, d):
        yield ids
    
    #Combinations with repeating elements:
    max_positions_repeated = min(max_positions_repeated, MAX_REPEATED_POSITIONS_LIMIT)
    for max_positions_repeated in xrange(1, max_positions_repeated+1):
        for ids in combinations(bursts_ids, d-max_positions_repeated): #any combinations
            for repeat_pos in combinations_with_replacement(range(len(ids)), max_positions_repeated): #repeat elements
                yield sorted(list(ids) + [ids[pos] for pos in repeat_pos]) #remember to sort!


def yield_bursts_ids_continous(bursts, d, max_positions_repeated): #TODO
    """Constructs tuples of <d> consequent bursts.

    See: yield_bursts_ids.
    """
    bursts_ids = range(len(bursts))

    #All the combinations where any element is repeated once:
    for start in xrange(len(bursts)-d+1):
        yield bursts_ids[start:start+d]
    
    #Combinations with repeating elements:
    max_positions_repeated = min(max_positions_repeated, MAX_REPEATED_POSITIONS_LIMIT)
    if max_positions_repeated<=0: return    
    raise Exception("max_positions_repeated>0 NOT SUPPORTED YET")#TODO (nie dziala poprawnie)

    for max_positions_repeated in xrange(1, max_positions_repeated+1):
        d = d-max_positions_repeated
        for start in xrange(len(bursts)-d+1): #any combinations
            ids = bursts_ids[start:start+d]
            for repeat_pos in combinations_with_replacement(range(len(ids)), max_positions_repeated): #repeat elements
                yield sorted(list(ids) + [ids[pos] for pos in repeat_pos]) #remember to sort!


def yield_bursts_ids_continous_with_holes(bursts, d, max_positions_repeated, numholes): #TODO
    """Constructs tuples of <d> bursts with max <numholes> holes in sequences."""    
    for ids in yield_bursts_ids_continous(bursts, d+numholes, 0): 
        for selected_ids in combinations(ids, d):
            yield selected_ids

    #Combinations with repeating elements:
    max_positions_repeated = min(max_positions_repeated, MAX_REPEATED_POSITIONS_LIMIT)
    if max_positions_repeated<=0: return    
    raise Exception("max_positions_repeated>0 NOT SUPPORTED YET")     #TODO

    d = d-max_positions_repeated
    for ids in yield_bursts_ids_continous(bursts, d+numholes, 0): 
        for selected_ids in combinations(ids, d):
            for repeat_pos in combinations_with_replacement(range(len(selected_ids)), max_positions_repeated): #repeat elements
                yield sorted(list(selected_ids) + [selected_ids[pos] for pos in repeat_pos]) #remember to sort!                   


###############################################################################


def _build_tuple_(bursts, ids):
    lefts   = list(bursts[i][1] for i in ids)
    rights  = list(bursts[i][2] for i in ids)
    return (ids, lefts+rights)


# Whole stream matching:

def yield_bursts_query_tuples(bursts, d, max_positions_repeated): 
    """Generates boundaries for index querying purposes."""
    for ids in yield_bursts_ids(bursts, d, max_positions_repeated):
        yield _build_tuple_(bursts, ids)    


def yield_bursts_tuples(bursts, d):
    """Generates boundaries for index building purposes."""
    max_positions_repeated = len(bursts)-d #how many positions can be covered with repeating bursts
    return yield_bursts_query_tuples(bursts, d, max_positions_repeated)


def yield_name2bursts_tuples(name2bursts, d):
    """Generates (name, ids, boundaries) for index building purposes."""
    for name, bursts in name2bursts:
        for ids, boundaries in yield_bursts_tuples(bursts, d):
            yield (name, ids, boundaries)  


# Part of the stream matching:

#def yield_name2bursts_tuples(name2bursts, d):
#yield_bursts_ids_continous_with_holes(bursts, d, max_positions_repeated, numholes)
#    for name, bursts in name2bursts:
#        for ids, boundaries in yield_bursts_tuples(bursts, d):
#            yield (name, ids, boundaries)  



###############################################################################

def build_rtree_index(name2bursts, d, name2bursts_tuples_generator=yield_name2bursts_tuples):   
    """ Constructs d-dimensional rtree index of bursts pairs."""             
    if len(name2bursts)<=0:
        print "[build_rtree_index][%f] Builiding %iD index out of %i entities will be skipped" % \
               (time.clock(), d, len(name2bursts))
        return None
    print "[build_rtree_index][%f] Builiding %iD index out of %i entities with %i bursts per enitity" % \
           (time.clock(), d, len(name2bursts), len(name2bursts[0][1]))

    p = index.Property()
    p.dimension = d
    p.index_type = index.RT_RTree #RT_RTree RT_MVTree RT_TPRTree
    p.fill_factor = 0.25
    p.variant = index.RT_Quadratic #RT_Linear, RT_Quadratic, RT_Star
    p.storage = index.RT_Disk
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    #p.filename='theindex'
    p.leaf_capacity = 50
    #p.index_capacity = 
    idx = index.Index(properties=p)

    tuples_gen = name2bursts_tuples_generator(name2bursts, d)
    counter = -1
    for counter, (name, ids, boundaries) in enumerate(tuples_gen): 
        if counter>0 and counter%100000==0: 
            print "[build_rtree_index][%f]   %i bursts inserted" % (time.clock(), counter)
        idx.insert(counter, boundaries, obj=(name, ids))
    print "[build_rtree_index][%f] %i bursts inserted in total" % (time.clock(), 1+counter)

    return idx


def query_rtree_index(query_name2bursts, idx_name2bursts, idx, JT, output_storage, \
                      bursts_query_tuples_generator=yield_bursts_query_tuples):
    if idx is None: return
    if len(query_name2bursts)<=0: return

    # Compute parameters:
    d                           = idx.properties.get_dimension()
    idx_numbursts               = len(idx_name2bursts[0][1])
    query_numbursts             = len(query_name2bursts[0][1])
    #what is max for how many positions can be covered with repeating bursts:
    max_positions_repeated      = query_numbursts-min_overlapping_required(idx_numbursts, query_numbursts, JT)
    print "[query_rtree_index][%f] Querying %iD index with %i entities with %i bursts per enitity (max_positions_repeated=%i)" % \
           (time.clock(), d, len(query_name2bursts), len(query_name2bursts[0][1]), max_positions_repeated) 

    # Query index:
    total_number_of_tuples, total_number_of_candidates = 0, 0 
    idx_name2bursts = dict(idx_name2bursts)
    for counter, (name, bursts) in enumerate(query_name2bursts): 

        if counter>0 and counter%10000==0: 
            print "[query_rtree_index][%f]   %i/%i processed (queried with %i tuples; %i candidadates)" % \
                (time.clock(), counter, len(query_name2bursts), total_number_of_tuples, total_number_of_candidates)   

        candidates = set()
        tuples_counter = -1
        for tuples_counter, (ids, boundaries) in enumerate( bursts_query_tuples_generator(bursts, d, max_positions_repeated) ):
            candidates.update( e.object[0] for e in idx.intersection(boundaries, objects=True) )
        total_number_of_tuples      += (tuples_counter+1)
        total_number_of_candidates  += len(candidates)        
        #print "[build_rtree_index] %i candidates for %s" % (len(candidates), name)

        for candidate_name in candidates:
            candidate_bursts = idx_name2bursts[candidate_name]
            JI = JaccardIndex(bursts, candidate_bursts)
            if JI >= JT:  
                output_storage.store(name, candidate_name, JI, ("%i %i" % (len(bursts), len(candidate_bursts))) )
            #print "[build_rtree_index] %i overlaps with %s" % (calc_num_overlapping(bursts, candidate_bursts), candidate_name)

        output_storage.flush()

    print "[query_rtree_index][%f] %i/%i processed in total (queried with %i tuples; %i candidadates)" % \
            (time.clock(), counter+1, len(query_name2bursts), total_number_of_tuples, total_number_of_candidates)                          


###############################################################################


def test_tuples_generation_time(name2bursts, d):
    print "[test_tuples_generation_time][%f] Checking %i-tuples generation time with %i entities with %i bursts per enitity" % \
           (time.clock(), d, len(name2bursts), len(name2bursts[0][1])) 

    total_number_of_tuples =  0 
    for counter, (name, bursts) in enumerate(name2bursts): 
        if counter%10000==0: print "[test_tuples_generation_time][%f]   %i/%i processed (queried with %i tuples)" % \
                                (time.clock(), counter, len(name2bursts), total_number_of_tuples)   
        for tuples_counter, (ids, boundaries) in enumerate( yield_bursts_tuples(bursts, d) ): pass
        total_number_of_tuples      += (tuples_counter+1)

    print "[test_tuples_generation_time][%f] %i/%i processed in total (queried with %i tuples)" % \
            (time.clock(), counter+1, len(name2bursts), total_number_of_tuples)



def report_rtree_index(idx, leaves):    
    if idx is None: return

    try:
        print "[report_rtree] Number of leaves:", len(index.Index.leaves(idx))
        leave_sizes = list( len(ids) for i,ids,bounds in index.Index.leaves(idx) )
        print "[report_rtree] %i leaves (min=%i, max=%i, median=%i, mean=%i)" % \
              (len(leave_sizes), min(leave_sizes), max(leave_sizes), np.median(leave_sizes), np.mean(leave_sizes))
    except:
        print "[report_rtree] Failed extracting leaves"

    start = time.clock()
    candidate_sizes =  list()
    for i, (idd, ids, leave_bounds) in enumerate(leaves):
        candidate_sizes.append( len(list(e.object for e in idx.intersection(leave_bounds, objects=True)))  )
        if i%1000==0: 
            print "[report_rtree] %i processed out of %i" % (i, len(leaves)) 
            print "[report_rtree] %i candidate sets (min=%i, max=%i, median=%i, mean=%i) [took: %f sec]" % \
                 (len(candidate_sizes), min(candidate_sizes), max(candidate_sizes), \
                np.median(candidate_sizes), np.mean(candidate_sizes), time.clock()-start)       
    print "[report_rtree] %i candidate sets (min=%i, max=%i, median=%i, mean=%i) [took: %f sec]" % \
         (len(candidate_sizes), min(candidate_sizes), max(candidate_sizes), \
            np.median(candidate_sizes), np.mean(candidate_sizes), time.clock()-start)


def _maintain_numbursts2index_(numbursts2index, numbursts2entities, range_first, range_last, JT): 
    print "[identify_linked_pairs_with_rtrees_index] Building required indexes"
    for n in xrange(range_first, range_last+1):
        if n in numbursts2index: continue
        dim                 = numbursts_lower_bound(n, JT)
        name2bursts         = numbursts2entities.get(n, list())
        numbursts2index[n]  = build_rtree_index(name2bursts, dim)
    print "[identify_linked_pairs_with_rtrees_index] Removing outdated indexes"
    for n in list(numbursts2index.keys()):
        if n<range_first or n>range_last:   numbursts2index.pop(n)
    print "[identify_linked_pairs_with_rtrees_index] %i indexes in the memory" % (len(numbursts2index))


def identify_linked_pairs_with_rtrees_index(numbursts2entities, JT, output_storage, \
                                            minbursts=3, maxbursts=10000):
    numbursts2index = dict() 
    considered = set()
    for nb in xrange(minbursts, maxbursts+1):

        range_first, range_last = numbursts_range(nb, JT)
        if range_first<minbursts or range_last>maxbursts: continue
        nb_range = range(range_first, range_last+1)        
        print "[identify_linked_pairs_with_rtrees_index] Considering in range [%i, %i]" % (range_first, range_last)
        _maintain_numbursts2index_(numbursts2index, numbursts2entities, range_first, range_last, JT)

        for n in nb_range:
            if (n, n) in considered: continue
            considered.add( (n, n) )
            selected = numbursts2entities.get(n, list())
            if len(selected)<=0: continue
            print "[identify_linked_pairs_with_rtrees_index] Considering %i vs. %i" % (n, n)
            query_rtree_index(selected, selected, numbursts2index[n], JT, output_storage)

        for n1, n2 in combinations(nb_range, 2):
            n1, n2 = min(n1, n2), max(n1, n2)
            if (n1, n2) in considered: continue
            considered.add( (n1, n2) )
            selected1 = numbursts2entities.get(n1, list())
            selected2 = numbursts2entities.get(n2, list()) 
            if len(selected1)<=0 or len(selected2)<=0: continue
            print "[identify_linked_pairs_with_rtrees_index] Considering %i vs. %i" % (n1, n2)
            query_rtree_index(selected1, selected2, numbursts2index[n2], JT, output_storage)


###############################################################################


def linked_pairs_with_rtrees_idx_numbursts(numbursts2entities, idx_numbursts, JT, output_storage):
    range_first, range_last = numbursts_range(idx_numbursts, JT)
    dim                     = numbursts_lower_bound(idx_numbursts, JT)
    idx_name2bursts         = numbursts2entities.get(idx_numbursts, list())
    #test_tuples_generation_time(idx_name2bursts, dim)
    idx                     = build_rtree_index(idx_name2bursts, dim)
    for query_numbursts in xrange(range_first, range_last+1):
        query_name2bursts = numbursts2entities.get(query_numbursts, list())
        #test_tuples_generation_time(query_name2bursts, idx.properties.get_dimension())
        query_rtree_index(query_name2bursts, idx_name2bursts, idx, JT, output_storage)  


if __name__=="__main__":

    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[bursts_index_rtrees] The script reads bursts and correlates them using R-trees."

    try:    
        path = sys.argv[1]
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: input data file!\n")
        sys.exit(-1)

    try:    
        JT = float(sys.argv[2])
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: JT!\n")
        sys.exit(-1)

    try:    
        consider_numbursts = list(int(e) for e in sys.argv[3].split(','))
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: Comma-separated list of numbers of bursts!\n")
        sys.exit(-1)

    try:    
        MAX_REPEATED_POSITIONS_LIMIT = max(int(sys.argv[4])-1, 0)
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: how many single burst can maximally overlap e.g. 1,2 or 3!\n") 
        sys.exit(-1)

    ###########################################################################

    print "[bursts_index_rtrees] JT=%.4f numbursts=%s MAX_REPEATED_POSITIONS_LIMIT=%i" % \
                (JT, sys.argv[3], MAX_REPEATED_POSITIONS_LIMIT)
    marker = "%s_%s_%i" % (("%f" % JT).rstrip("0"), sys.argv[3].replace(",","-"), MAX_REPEATED_POSITIONS_LIMIT+1)

    storage_file = open(path+".index_rtrees_%s" % marker, "w")
    output_storage = JIOutputStorage(storage_file)
    print "[bursts_index_rtrees] Storage file: %s" % str(storage_file)

    print "[bursts_index_rtrees] Loading data from %s" % path
    name2bursts = list( yield_name2bursts(open(path)) )
    print "[bursts_index_rtrees][%f] %i loaded in total" % (time.clock(), len(name2bursts))

    #data_size, tmin, tmax, bursts_stats = bursts_stats(name2bursts)
    #print  "[bursts_index_rtrees]","N =",data_size,"tmin =", tmin,"tmax =", tmax, "bursts_stats =", bursts_stats
        
    print "[bursts_index_rtrees][%f] Computing numbursts2entities" % (time.clock())
    numbursts2entities = calc_numbursts2entities(name2bursts, element_constructor = lambda name, bursts: (name, bursts))
    #print_key2entities(numbursts2entities.iteritems(), fout, entities_formatter = lambda entities: "%i" % len(entities))
    
    print "[bursts_index_rtrees][%f] Starting for %s" % (time.clock(), marker)
    for idx_numbursts in consider_numbursts:
        print "[bursts_index_rtrees][%f] Considering index for %i bursts" % (time.clock(), idx_numbursts)
        linked_pairs_with_rtrees_idx_numbursts(numbursts2entities, idx_numbursts, JT, output_storage)
        print "[bursts_index_rtrees][%f] Current output size: %i" % (time.clock(), output_storage.stored_count())
    print "[bursts_index_rtrees][%f] Done for %s. %i pairs generated." % (time.clock(), marker, output_storage.stored_count())

    #identify_linked_pairs_with_rtrees_index(numbursts2entities, JT, output_storage, min(consider_numbursts), max(consider_numbursts))


