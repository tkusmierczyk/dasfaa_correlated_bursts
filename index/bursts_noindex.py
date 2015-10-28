#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
sys.path.append("../")

from base.bursts import *
from base.bursts_jaccard import *
from bursts_index import calc_numbursts2entities


def identify_linked_pairs(name2bursts1, name2bursts2, JT, output_storage):
    if len(name2bursts1)<=0 or len(name2bursts2)<=0: return

    num_pairs = len(name2bursts1)*len(name2bursts2)
    matched = 0    
    for counter, (name1, bursts1) in enumerate(name2bursts1):
        if counter>0 and counter%10000==0: 
            print "[identify_linked_pairs][%f] %i/%i" % (time.clock(), counter*len(name2bursts1), num_pairs)

        for name2, bursts2 in name2bursts2:
            if name1==name2: continue

            JI = JaccardIndex(bursts1, bursts2)
            if JI >= JT:  
                output_storage.store(name1, name2, JI, str(len(bursts1))+" "+str(len(bursts2)))    
                matched += 1                         
   
    print "[identify_linked_pairs][%f] %i/%i matched" % (time.clock(), matched, num_pairs)
    

def identify_linked_pairs_without_index(numbursts2entities, JT, output_storage, min_numbursts, max_numbursts):
    base_range = range(min_numbursts, max_numbursts+1)

    print "[identify_linked_pairs_without_index][%f] Considered combinations from range %s" % \
                (time.clock(), str(base_range))
    for n1 in base_range:
        for n2 in xrange(numbursts_lower_bound(n1, JT), n1+1):
            print "[identify_linked_pairs_without_index][%f] Considering %i vs. %i" % (time.clock(), n1, n2)
            selected1 = numbursts2entities.get(n1, list())
            selected2 = numbursts2entities.get(n2, list())
            if len(selected1)>0 and len(selected2)>0: identify_linked_pairs(selected1, selected2, JT, output_storage)
            print "[identify_linked_pairs_without_index][%f] Current output size: %i" % \
                        (time.clock(), output_storage.stored_count())


if __name__=="__main__":

    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[bursts_noindex] The script reads bursts and correlates them."
    
    try:    path = sys.argv[1]
    except: sys.stderr.write("[bursts_noindex] Arg expected: input data file!\n"); sys.exit(-1)
    try:    JT = float(sys.argv[2])
    except: sys.stderr.write("[bursts_noindex] Arg expected: JT!\n"); sys.exit(-1)
    try:    min_numbursts, max_numbursts = int(sys.argv[3]), int(sys.argv[4])
    except: sys.stderr.write("[bursts_noindex] Args expected: Min and max number of bursts!\n"); sys.exit(-1)

    print "[bursts_noindex] JT=%.4f min_numbursts=%i max_numbursts=%i" % \
            (JT, min_numbursts, max_numbursts)
    marker = "%.4f_%i_%i" % (JT, min_numbursts, max_numbursts)

    storage_file = open(path+".noindex_%s" % marker, "w")
    output_storage = JIOutputStorage(storage_file)
    print "[bursts_noindex] Storage file: %s" % str(storage_file)

    print "[bursts_noindex] Loading data from %s" % path
    name2bursts = list( yield_name2bursts(open(path)) )
    print "[bursts_noindex][%f] %i loaded in total" % (time.clock(), len(name2bursts))

    #data_size, tmin, tmax, bursts_stats = bursts_stats(name2bursts)
    #print  "[bursts_noindex]","N =",data_size,"tmin =", tmin,"tmax =", tmax, "bursts_stats =", bursts_stats
        
    print "[bursts_noindex][%f] Computing numbursts2entities" % (time.clock())
    numbursts2entities = calc_numbursts2entities(name2bursts, element_constructor = lambda name, bursts: (name, bursts))
    #print_key2entities(numbursts2entities.iteritems(), fout, entities_formatter = lambda entities: "%i" % len(entities))
    
    print "[bursts_noindex][%f] Starting for %s" % (time.clock(), marker)
    identify_linked_pairs_without_index(numbursts2entities, JT, output_storage, min_numbursts, max_numbursts)
    print "[bursts_noindex][%f] Done for %s. %i pairs generated." % (time.clock(), marker, output_storage.stored_count())


