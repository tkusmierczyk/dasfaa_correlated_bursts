#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Indexing of bursts from many timelines."""

import math
import sys
sys.path.append("../")

import bursts_index_list 
from base.bursts_jaccard import numbursts_lower_bound

if __name__=="__main__":
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[bursts_index_1D_border_run] Analysis of border entities to be checked in bursts_index_list."
    
    argv = sys.argv
    try:    
        path = argv[1]
    except: 
        sys.stderr.write("[bursts_index_1D_border_run] Arg expected: input data file!\n"); 
        sys.exit(-1)
        
    try:    
        JT = float(argv[2])
    except: 
        sys.stderr.write("[bursts_index_1D_border_run] Arg expected: JT!\n"); 
        sys.exit(-1)
        
    try:    
        numbursts = int(argv[3])
    except: 
        sys.stderr.write("[bursts_index_1D_border_run] Arg expected: (border) number of bursts (per entity)!\n"); 
        sys.exit(-1)

    min_numbursts = numbursts_lower_bound(numbursts, JT)
    max_bursts    = int( math.ceil(float(numbursts-1)/JT) )
    print "[bursts_index_1D_border_run] min_numbursts=%i max_bursts=%i" % (min_numbursts, max_bursts)

    argv = [argv[0], path, JT, min_numbursts, max_bursts]
    bursts_index_list.main(argv)
