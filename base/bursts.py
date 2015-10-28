#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Managing and processing bursts (burst = <level, starttime, endtime>)."""

import sys
from pageviews_io import *


def yield_kleinberg_bursts(str_bursts_list, type_cast=float, separator=","):
    for burst in str_bursts_list:
        parts = burst.split(separator)
        yield (int(parts[0]), type_cast(parts[1]), type_cast(parts[2]))                   
          
  
def bursts2str_bursts_list(bursts, separator=","):
    return list( str(level)+separator+str(first)+separator+str(last) for level, first, last in bursts )


def parse_meta(meta_str):
    """Calculates pair (timeline length, reduction rate, number of bursts)."""
    parts = meta_str.split(",")
    return int(parts[0]), int(parts[1]), int(parts[2])


def yield_name2bursts(fin, type_cast=int, minlevel=0):
    """Yields pairs (name, list-of-bursts)."""
    for line in fin.xreadlines():
        if line.strip()=="" or line[0]=="#": continue
        project, name, date, time, meta_str, str_bursts_list = parse_line(line)
        bursts = list(b for b in yield_kleinberg_bursts(str_bursts_list, type_cast) if b[0]>=minlevel)
        bursts = sorted((bursts), key=lambda b: (b[1],b[2],b[0]) )
        yield name, bursts


def yield_name2bursts_numbursts(name2bursts, numbursts = [1,2,3]):
    """Yields bursts that have number of bursts included in numbursts."""
    numbursts = set(numbursts)
    for name, bursts in name2bursts:
        if len(bursts) in numbursts:
            yield name, bursts
    

def yield_name2bursts_for_entites(name2bursts, entites):
    """Yields bursts that for selected entities."""
    entites = set(entites)
    for name, bursts in name2bursts:
        if name in entites:
            yield name, bursts


def mark_burst_levels(bursts):
    """Calculates timeline with levels instead of views."""
    if len(bursts)<=0: return list()

    maxt = max(end+1 for level, start, end in bursts)
    levels = list(0 for i in xrange(maxt+1))
    for level, start, end in bursts:
        for t in xrange(start, end+1): #end is included!
            levels[t] = max(levels[t], level)    

    return levels


###############################################################################


def burst_length(burst):
    level, start, end = burst
    return end-start+1 #end is included


def bursts_length(bursts):
    return sum(burst_length(burst) for burst in bursts)


def burst_center(burst):
    level, start, end = burst
    return 0.5*(start+end)


def overlap(first1, last1, first2, last2):
    if first1 >= first2 and last1 <= last2: #1 nested in 2
        return True
    elif first2 >= first1 and last2 <= last1: #2 nested in 1
        return True
    elif first2 >= first1 and first2 <= last1: #overlap: 1 earlier
        return True    
    elif first1 >= first2 and first1 <= last2: #overlap: 2 earlier
        return True
    return False   


def overlap_borders(first1, last1, first2, last2):
    """Calculates borders of overlapping segment"""
    if first1 >= first2 and last1 <= last2: #1 nested in 2
        return (first1, last1)
    elif first2 >= first1 and last2 <= last1: #2 nested in 1
        return (first2, last2)
    elif first2 >= first1 and first2 <= last1: #overlap: 1 earlier
        return (first2, last1)
    elif first1 >= first2 and first1 <= last2: #overlap: 2 earlier
        return (first1, last2)
    return (None, None)   


def bursts_overlap(burst1, burst2):
    level1, first1, last1 = burst1
    level2, first2, last2 = burst2
    return overlap(first1, last1, first2, last2)


def second_nested_in_first(first_burst, second_burst):
    level1, first1, last1 = first_burst
    level2, first2, last2 = second_burst
    return (first2 >= first1 and last2 <= last1)


def any_overlap(bursts, ignore_level=1):
    result = False
    for i, (l1,f1,e1) in enumerate(bursts):
        for j in xrange(i+1, len(bursts)):
            l2, f2, e2 = bursts[j];
            if l1==ignore_level or l2==ignore_level: continue
            if overlap(f1, e1, f2, e2): 
                print "[any_overlap] WARNING: Overlaping bursts:", (l1,f1,e1),"-",(l2, f2, e2)
                result = True
    return result


def print_overlapping(bursts1, bursts2):
    for b1 in bursts1:
        for b2 in bursts2:
            if bursts_overlap(b1, b2): 
                print "[pair_overlap] WARNING: Overlaping bursts:", b1,"-",b2


def equal_borders(first_burst, second_burst):
    level1, first1, last1 = first_burst
    level2, first2, last2 = second_burst
    return (first2 == first1 and last2 == last1)


def merge_bursts(level1, first1, last1, level2, first2, last2):
    level1 = min(level1, level2)
    first1 = min(first1, first2)
    last1  = max(last1, last2)
    return level1, first1, last1


###############################################################################


def calc_time2bursts(name2bursts_generator, min_level=2):
    """Calculates {time: level: list of names} structure."""
    from bursts_rounding import round_bursts
    from aux import _ensure_list_of_lists_length_
    time2bursts = []
    for name, bursts in name2bursts_generator:
        bursts = round_bursts(bursts)

        for level, first, last in bursts:
            if level < min_level: continue
            
            _ensure_list_of_lists_length_(time2bursts, last+1)
            for t in xrange(first, last+1):
                _ensure_list_of_lists_length_(time2bursts[t], level+1)
                time2bursts[t][level].append(name)

    return time2bursts


def print_time2bursts(time2bursts, fout, \
                      bursts_formatter = lambda bursts: " %i" % len(bursts)):
    on = False
    for t in xrange(len(time2bursts)):
        if not on and len(time2bursts[t])>0: on=True
        if on:
            fout.write("%i" % t)
            for level in xrange(len(time2bursts[t])):
                fout.write( bursts_formatter(time2bursts[t][level]) )                    
            fout.write("\n")


if __name__=="__main__":

    print "The script reads (from stdin) pageviews with kleinberg bursts and prints out timeline."

    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    from bursts_rounding import round_bursts
    time2bursts = calc_time2bursts( ( (name, round_bursts(bursts)) \
                        for name,bursts in yield_name2bursts(fin)), min_level=2)
    print_time2bursts(time2bursts, fout)


