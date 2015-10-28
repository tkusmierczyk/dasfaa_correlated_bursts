#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rounding float bursts into integer bursts."""


from bursts import *
from bursts_filtering import *
from math import floor, ceil


def round_bursts(bursts):
    return map(lambda b: (b[0], int(round(b[1])), int(round(b[2]))), bursts)


def floor_bursts(bursts):
    return map(lambda b: (b[0], int(floor(b[1])), int(floor(b[2]))), bursts)


def spread_burst(burst):
    level = burst[0]
    start = int( floor(burst[1]) )
    end = int( ceil(burst[2]) )
    if start==end: 
        end += 1
    return level, start, end


def round_spread_bursts(bursts):
    return map(spread_burst, bursts)



    
if __name__=="__main__":
    
    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "[rounding] The script rounds bursts."
    
    counter = 0
    for counter, line in enumerate(fin.xreadlines()):
        if len(line.strip())==0 or line[0]=='#': continue    

        project, name, date, time, meta_str, str_bursts_list = parse_line(line)
        bursts = list( yield_kleinberg_bursts(str_bursts_list) )
        #fout.write("Number of input bursts %i \n" % len(bursts))

        bursts = round_bursts(bursts) #round_spread_bursts
        #fout.write("After rounding number of bursts %i \n" % len(bursts))

        bursts = list((level,first,last) for level,first,last in bursts if last>=first)
        #fout.write("Number of nonempty bursts %i \n" % len(bursts))

        #merging this that overlap and have the same level
        bursts = reduce_overlaping_with_levels(bursts)        
        #fout.write("Number of nonmerged bursts %i \n" % len(bursts))

        #sorting properly
        bursts = list((level, first, last) for first, level, last in \
                        sorted((first, level, last) for level, first, last in bursts)) 
        #fout.write("Number of output bursts %i \n" % len(bursts))

        #TODO removing empty bursts
        
        meta_str += ","+str(len(bursts)) #append info
        str_bursts_list = bursts2str_bursts_list(bursts)
        fout.write( construct_line(project, name, date, time, meta_str, str_bursts_list) )
        fout.write("\n")
 
    print "[rounding] Done. %i processed." % (counter+1)

