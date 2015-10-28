#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Indexing of bursts from many timelines using low-dimensional R-Trees."""

import sys
sys.path.append("../")

from bursts_index_rtrees import *


def linked_pairs_with_rtrees_low_dimension_idx_numbursts(numbursts2entities, idx_numbursts, JT, dim, output_storage):
    range_first, range_last = numbursts_range(idx_numbursts, JT)
    idx_name2bursts         = numbursts2entities.get(idx_numbursts, list())
    idx                     = build_rtree_index(idx_name2bursts, dim)

    for query_numbursts in xrange(range_first, range_last+1):
        query_name2bursts = numbursts2entities.get(query_numbursts, list())
        query_rtree_index(query_name2bursts, idx_name2bursts, idx, JT, output_storage)  


if __name__=="__main__":

    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[bursts_index_rtrees] The script reads bursts and correlates them using low-dimensional R-Trees."

    try:    
        path = sys.argv[1]
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: input data file!\n"); sys.exit(-1)

    try:    
        JT = float(sys.argv[2])
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: JT!\n"); sys.exit(-1)

    try:    
        if "-" in sys.argv[3]:
            parts = sys.argv[3].split("-")
            consider_numbursts = range(int(parts[0]), int(parts[1])+1)
        else:
            consider_numbursts = list(int(e) for e in sys.argv[3].split(','))
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: Comma-separated " + \
                         "(or range start-end) list of numbers of bursts!\n"); 
        sys.exit(-1)

    try:    
        #Internally MAX_REPEATED_POSITIONS_LIMIT has different meaning and therefore one is substracted.
        MAX_REPEATED_POSITIONS_LIMIT = max(int(sys.argv[4])-1, 0)
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: how many single burst can maximally overlap " + \
                         " e.g. 1,2 or 3!\n") 
        sys.exit(-1)

    try:    
        dimensions = int(sys.argv[5])
    except: 
        sys.stderr.write("[bursts_index_rtrees] Arg expected: what should be index dimensionality!\n") 
        sys.exit(-1)


    print "[bursts_index_rtrees] JT=%.4f d=%i numbursts=%s MAX_REPEATED_POSITIONS_LIMIT=%i" % \
                (JT, dimensions, sys.argv[3], MAX_REPEATED_POSITIONS_LIMIT)
    marker = "%s_%s_%i_%i" % (("%.3f" % JT).rstrip("0"), sys.argv[3].replace(",","-"), \
              MAX_REPEATED_POSITIONS_LIMIT+1, dimensions)

    storage_file = open(path+".index_rtrees_ld_%s" % marker, "w")
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
        linked_pairs_with_rtrees_low_dimension_idx_numbursts(numbursts2entities, idx_numbursts, JT, dimensions, output_storage)
        print "[bursts_index_rtrees][%f] Current output size: %i" % (time.clock(), output_storage.stored_count())
    print "[bursts_index_rtrees][%f] Done for %s. %i pairs generated." % (time.clock(), marker, output_storage.stored_count())

    #identify_linked_pairs_with_rtrees_index(numbursts2entities, JT, output_storage, min(consider_numbursts), max(consider_numbursts))


