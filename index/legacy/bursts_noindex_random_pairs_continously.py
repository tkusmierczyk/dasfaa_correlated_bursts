#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Indexing of bursts from many timelines."""

import sys
sys.path.append("../")

from base.bursts import *
from bursts_filtering import *
from bursts_stats import *
from base.bursts_jaccard import *
from base.ui import KeyEventThread, STOP_BASELINE_SCRIPT

from itertools import *
from rtree import index
from aux import *
import random
from ui import *




if __name__=="__main__":

    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[bursts_index_baseline] The script reads bursts and correlates them."
    print "[bursts_index_baseline] Pairs to be compared are selected randomly."

    try:    
        path = sys.argv[1]
    except: 
        sys.stderr.write("[bursts_index_baseline] Arg expected: input data file!\n"); sys.exit(-1)

    try:    
        JT = float(sys.argv[2])
    except: 
        sys.stderr.write("[bursts_index_baseline] Arg expected: JT!\n"); sys.exit(-1)

    try:    
        min1 = int(sys.argv[3])
        max1 = int(sys.argv[4])
        min2 = int(sys.argv[5])
        max2 = int(sys.argv[6])
    except: 
        sys.stderr.write("[bursts_index_baseline] Arg expected: min1 max1 min2 max2 \n"); 
        sys.stderr.write("[bursts_index_baseline] Pairs will be selected from indices [min1, max1]x[min2, max2]\n"); 
        sys.exit(-1)

    minbursts = 5

    print "[bursts_index_baseline] Loading data from %s " % (path)
    name2bursts = list( yield_name2bursts(open(path)) )
    print "[bursts_index_baseline][%f] %i loaded in total" % (time.clock(), len(name2bursts))
    
    name2bursts = list( (name,bursts) for name, bursts in name2bursts if len(bursts) >= minbursts)
    print "[bursts_index_baseline][%f] %i left after filtering" % (time.clock(), len(name2bursts))    

    max1, max2 = min(max1, len(name2bursts)-1), min(max2, len(name2bursts)-1)
    print "[bursts_index_baseline] JT=%.4f numbursts=%s min1=%i max1=%i min2=%i max2=%i" % \
                (JT, sys.argv[3], min1, max1, min2, max2)
    marker = "%s_%s_%i_%i_%i_%i" % (("%f" % JT).rstrip("0"), sys.argv[3].replace(",","-"), min1, max1, min2, max2)

    storage_file = open(path+".index_baseline_%s" % marker, "w")
    output_storage = JIOutputStorage(storage_file)
    print "[bursts_index_baseline] Storage file: %s" % str(storage_file)

    print "[bursts_index_baseline] q + ENTER to stop"
    kethread = KeyEventThread()
    kethread.start()

    print "[bursts_index_baseline][%f] Starting for %s: min1=%i max1=%i min2=%i max2=%i" % \
            (time.clock(), marker, min1, max1, min2, max2) 
    considered = set()
    matched = 0
    time0 = time.clock()
    repeated = 0
    prevtime = 0
    try:
        while True:
            if len(considered)>1000000000: break
            if STOP_BASELINE_SCRIPT: break

            #randomly select a pair:
            while True: 
                i1 = random.randint(min1, max1)
                i2 = random.randint(min2, max2)
                i1, i2 = min(i1,i2), max(i1,i2)
                if i1!=i2 and (i1, i2) not in considered: break
                repeated += 1 #num times we had to repeat selection
            considered.add( (i1, i2) )

            #validate pair
            name1, bursts1 = name2bursts[i1]
            name2, bursts2 = name2bursts[i2]            

            JI = JaccardIndex(bursts1, bursts2)
            if JI>=JT: 
                if not output_storage.store(name1, name2, JI):
                    print "[ERROR] name1=%s name2=%s JI=%.4f" % (name1, name2, JI)                    
                matched += 1  

            if round(time.clock()) != prevtime:
                prevtime = round(time.clock())
                print "%.3f: %i = %i/%i  %i" % ((time.clock()-time0), output_storage.stored_count(), matched, len(considered), repeated)

    except KeyboardInterrupt:
        STOP_BASELINE_SCRIPT = True

    output_storage.flush()
    print "%.3f: %i/%i  %i" % ((time.clock()-time0), matched, len(considered), repeated)
    print "[bursts_index_baseline][%f] Done for %s. %i pairs generated." % (time.clock(), marker, output_storage.stored_count())



