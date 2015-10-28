#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Filtering containers of bursts (burst = <level, starttime, endtime>)."""

import sys
from bursts import *
from bursts_rounding import *
import numpy as np


def filter_bursts_length(bursts, min_length=0, max_length=1000000):
    return list(b for b in bursts if burst_length(b)>=min_length and burst_length(b)<=max_length)


def filter_bursts_range(bursts, min_level=2, max_level=1000000):
    return list((level, first, last) for level, first, last in bursts if level>=min_level and level<=max_level)


def filter_bursts(bursts, levels):
    levels = set(levels)
    return list( (level, start, end) for level, start, end in bursts if level in levels )


def filter_bursts_overlapping(bursts, first, last):
    """Calculates bursts that overlap with [first, last]"""
    return list( (level, start, end) for level, start, end in bursts if overlap(first, last, start, end) )            


def reduce_bursts_into_centers(bursts):
    center = lambda first, last: (0.5*(last+first))
    return map(lambda b: (b[0], center(b[1], b[2]), center(b[1], b[2])), bursts)


def expand_bursts(bursts, minlen, maxlen):
    new_bursts = list()
    for b in bursts:
        if burst_length(b)<minlen:
            new_bursts.append( (b[0], ) )
        elif burst_length(b)>maxlen:   
            new_bursts.append( (b[0], ) )
        else:
            new_bursts.append(b)
    return new_bursts    


def reduce_overlaping(bursts, overlapping_criteria = lambda lev1,f1,l1,lev2,f2,l2: overlap(f1, l1, f2, l2)): 
    """Calculates set of non overlapping bursts."""
    new_bursts = list()
    bursts = set(bursts)
    while len(bursts)>0:                        #move bursts to new_bursts
        level1, first1, last1 = bursts.pop()    #next to be considered
        
        while True:
            to_remove = list()                      #set of overlapping
            for burst in bursts:
                level2, first2, last2 = burst
                if overlapping_criteria(level1, first1, last1, level2, first2, last2):
                    to_remove.append(burst)         #add to be detected as overlapping
                    level1, first1, last1 = merge_bursts(level1, first1, last1, level2, first2, last2) #extend considered burst
            if len(to_remove) == 0: break
            for burst in to_remove:                 #removing bursts included in the considered one
                bursts.remove(burst)

        new_bursts.append( (level1, first1, last1) ) #adding considered (extended) burst

    return new_bursts


def reduce_overlaping_with_levels(bursts):
    """Merging bursts that overlap and have the same level."""
    return reduce_overlaping(bursts, \
        overlapping_criteria = lambda lev1,f1,l1,lev2,f2,l2: (lev1==lev2 and overlap(f1,l1,f2,l2)) )



def time_granularity_reduction(bursts, time_scatter = 0, reduction_rate = 1):
        return list( (level, float(first-time_scatter)/reduction_rate, float(last+time_scatter)/reduction_rate) 
                        for level, first, last in bursts )    


def filter_bursts_time(bursts, start_time, end_time):
    """Keeps bursts having center point in [start_time, end_time)."""
    center = lambda first, last: (0.5*(last+first))
    return list((level, f, l) for level, f, l in bursts if center(f,l)>=start_time and center(f,l)<end_time)
 
    
if __name__=="__main__":
    
    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[filtering] The script filters bursts of selected levels."
    print "[filtering] Optional parameters: min_level max_level of bursts"
    print "[filtering] If min_level<=0 or max_level<=0 then will be interpreted as percentiles (e.g. -90 means 90%)."

    try: min_level = int(sys.argv[1])
    except: min_level = 3

    try: max_level = int(sys.argv[2])
    except: max_level = 10000000000

    try: max_length = int(sys.argv[3])
    except: max_length = 10000000000

    print "[filtering] min_level = %i " % min_level
    print "[filtering] max_level = %i " % max_level
    print "[filtering] max_length = %i " % max_length
    
    counter = 0
    for counter, line in enumerate(fin.xreadlines()):

        #if counter%100000==0: print "%i processed" % counter
        if len(line.strip())==0 or line[0]=='#': continue    

        try:
            project, name, date, time, meta_str, str_bursts_list = parse_line(line)
            bursts = list( yield_kleinberg_bursts(str_bursts_list, type_cast=float) )

            if len(bursts)>0:

                if min_level<=0:    absolute_min_level = np.percentile(list(b[0] for b in bursts), -min_level)
                else:               absolute_min_level = min_level
                if max_level<=0:    absolute_max_level = np.percentile(list(b[0] for b in bursts), -max_level)
                else:               absolute_max_level = max_level

                bursts = filter_bursts_range(bursts, absolute_min_level, absolute_max_level)
                bursts = filter_bursts_length(bursts, 0, max_length)

            str_bursts_list = bursts2str_bursts_list(bursts)
            fout.write("%s\n" % construct_line(project, name, date, time, meta_str, str_bursts_list) )
        except:
            print "[filtering][ERROR] Failed parsing line: %s" % (line.strip())
            fout.write("%s\n" % line.strip())

    print "[filtering] Done. %i processed." % (counter+1)


