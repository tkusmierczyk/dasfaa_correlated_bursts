#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reads pageviews with kleinberg bursts and calculates statistics."""

from pageviews_io import *
from bursts import *
from stats import *
from bursts_filtering import *
from aux import *
from math import ceil, floor
import time as tt


def bursts_stats(entity2bursts):
    tmin, tmax, data_size = 1000000, 0, 0
    numbursts = list()
    for entity, bursts in entity2bursts:
        data_size += 1
        numbursts.append( len(bursts) ) 
        for level, first, last in bursts:
            tmin, tmax = int(floor(min(first, tmin))), int(ceil(max(last, tmax)))
    return data_size, tmin, tmax, "bursts: %s" % stats_string(numbursts)


def bursts_stats_file(fin):
    print "Reading %s to obtain general stats" % fin
    return bursts_stats( yield_name2bursts(fin) )


def load_entity2bursts(fin, timeline_original_length):
    entity2bursts = list()
    bursts_filter = lambda bursts: bursts
    #bursts_filter =lambda bursts: round_bursts( reduce_overlaping( filter_bursts_range(bursts, min_level=2) ) )
    for counter, line in enumerate(fin.xreadlines()):
        if counter%100000==0: print "%i processed" % counter

        project, name, date, time, meta_str, str_bursts_list = parse_line(line)
        bursts = bursts_filter( list( yield_kleinberg_bursts(str_bursts_list, type_cast=int) ) )
        #timeline_original_length, reduction_rate, number_of_original_bursts = parse_meta(meta_str)

        entity2bursts.append( ((name, timeline_original_length), bursts) )
    return entity2bursts


def calc_time2numbursts2count(entity2bursts):
    maxnumbursts = max( len(bursts) for entity, bursts in entity2bursts )
    time2numbursts2count = [[0 for b in xrange(maxnumbursts+1)] for t in xrange(tmax+1)]
    for counter, ((name, timeline_original_length), bursts) in enumerate(entity2bursts): 
        if counter%1000==0: print "[%.2f] %i processed" % (tt.clock(),counter)
        bursts = sorted( (first,last) for level,first,last in bursts )

        number_of_bursts, time = 0, 0
        for first, last in bursts: 

            for time in xrange(time, first): #updating up to the next burst
                time2numbursts2count[time][number_of_bursts] += 1
            time = first - 1

            number_of_bursts += 1

            for time in xrange(time, last+1): #updating next burst
                time2numbursts2count[time][number_of_bursts] += 1                
            time = last + 1 

        for time in xrange(time, tmax): #update up to the end of the timeline
            time2numbursts2count[time][number_of_bursts] += 1    

    return time2numbursts2count


def calc_bursts_overall_stats(entity2bursts):
    number_of_bursts = []
    bursts_coverage = []
    bursts_coverage_fraction = []    
    timeline_length = []
    number_of_bursts_per_hour = []
    bursts_length = []
    
    for (name, timeline_original_length), bursts in entity2bursts:
        coverage = sum(burst_length(b) for b in bursts)

        bursts_length.extend(burst_length(b) for b in bursts)
        number_of_bursts.append( len(bursts) )
        bursts_coverage.append( coverage )
        bursts_coverage_fraction.append( float(coverage)/timeline_original_length )
        timeline_length.append( timeline_original_length )   
        number_of_bursts_per_hour.append( float(len(bursts))/timeline_original_length )   
    
    return number_of_bursts, bursts_coverage, bursts_coverage_fraction, timeline_length, number_of_bursts_per_hour, bursts_length


def calc_numbursts_in_time(entity2bursts, tmin, tmax):
    count = 0 
    for (name, timeline_original_length), bursts in entity2bursts:
        count += len( filter_bursts_overlapping(bursts, tmin, tmax) )
    return count


if __name__=="__main__":

    print "The script reads pageviews with kleinberg bursts and calculates statistics."
    print "Values are stored in separate files."

    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    try:
        path = sys.argv[1]
    except:
        print "Argument expected: input file path"    
        sys.exit(-1)

    try:
        timeline_original_length = int(sys.argv[2])
    except:
        print "Argument expected: number of hours covered (e.g. 8760, 26304)."    
        sys.exit(-1)

    fin = open(path)    

    print "Loading entity2bursts into memory from %s" % str(fin)
    entity2bursts = load_entity2bursts(fin, timeline_original_length)
    print "%i loaded" % len(entity2bursts)

    ###########################################################################

    print "Basic statistics"
    data_size, tmin, tmax, bursts_stats = bursts_stats(entity2bursts)
    print  "N =",data_size,"tmin =", tmin,"tmax =", tmax, " bursts_stats =",  bursts_stats

    ###########################################################################

    print "Number of bursts per year"
    print "#bursts in time interval1:",calc_numbursts_in_time(entity2bursts, 0, 8760)
    print "#bursts in time interval2:",calc_numbursts_in_time(entity2bursts, 8761, 17544)
    print "#bursts in time interval3:",calc_numbursts_in_time(entity2bursts, 17545, 26304)

    ###########################################################################

    #print "Calculating number of burst per entity up to some time"
    #time2numbursts2count = calc_time2numbursts2count(entity2bursts)
    #store_list_of_lists(open("bursts_stats.time2numbursts2count", "w"), time2numbursts2count)

    ###########################################################################

    print "Calculating overall stats"
    number_of_bursts, bursts_coverage, bursts_coverage_fraction, \
        timeline_length, number_of_bursts_per_hour, bursts_length = \
        calc_bursts_overall_stats(entity2bursts)    

    print "Storing values per element to %s.*" % path
    store_values(open(path+".bursts_stats.bursts_length", "w"), bursts_length)
    store_values(open(path+".bursts_stats.number_of_bursts", "w"), number_of_bursts)
    store_values(open(path+".bursts_stats.bursts_coverage", "w"), bursts_coverage)
    store_values(open(path+".bursts_stats.bursts_coverage_fraction", "w"), bursts_coverage_fraction)
    store_values(open(path+".bursts_stats.timeline_length", "w"), number_of_bursts)
    store_values(open(path+".bursts_stats.number_of_bursts_per_hour", "w"), number_of_bursts)

    ###########################################################################


    plot_histogram(bursts_length, ylabel="probability", xlabel="length [h]", title="Bursts length", label="hist", \
                    maxx=None, minx=None, numbins=100, log=False, normed=True)
    plot_log_log(bursts_length, ylabel="probability", xlabel="length [h]", title="Bursts length", label="hist", \
                    maxx=None, minx=None, numbins=100, log=True, normed=True)

    plot_histogram(number_of_bursts, ylabel="probability", xlabel="value", title="Number of bursts per entity", label="hist", \
                    maxx=None, minx=None, numbins=100, log=True, normed=True)
    plot_log_log(number_of_bursts, ylabel="probability", xlabel="value", title="Number of bursts per entity", label="hist", \
                    maxx=None, minx=None, numbins=100, log=True, normed=True)

    plot_histogram(bursts_coverage, ylabel="probability", xlabel="value", title="Number of bursty hours", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)
    plot_log_log(bursts_coverage, ylabel="probability", xlabel="value", title="Number of bursty hours", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)

    plot_histogram(bursts_coverage_fraction, ylabel="probability", xlabel="value", \
                    title="Fraction of bursty hours", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)
    plot_log_log(bursts_coverage_fraction, ylabel="probability", xlabel="value", \
                    title="Fraction of bursty hours", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)


    plot_histogram(number_of_bursts_per_hour, ylabel="probability", xlabel="value", title="Number of bursts per hour", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)
    plot_log_log(number_of_bursts_per_hour, ylabel="probability", xlabel="value", title="Number of bursts per hour", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)


    plot_histogram(bursts_length, ylabel="probability", xlabel="length [h]", title="Bursts length", label="hist", \
                    maxx=None, minx=None, numbins=100, log=False, normed=True)

    plot_log_log(number_of_bursts, ylabel="probability", xlabel="value", title="Number of bursts per entity", label="hist", \
                    maxx=None, minx=None, numbins=100, log=False, normed=True)

    plot_histogram(bursts_coverage, ylabel="probability", xlabel="value", title="Number of bursty hours", label="hist", \
                    maxx=None, minx=None, numbins=30, log=False, normed=True)

    plot_log_log(bursts_coverage_fraction, ylabel="probability", xlabel="value", \
                    title="Fraction of bursty hours", label="hist", \
                    maxx=None, minx=None, numbins=30, log=False, normed=True)

    plot_log_log(number_of_bursts_per_hour, ylabel="probability", xlabel="value", title="Number of bursts per hour", label="hist", \
                    maxx=None, minx=None, numbins=30, log=False, normed=True)



    plot_histogram(timeline_length, ylabel="probability", xlabel="value", title="Number of hours per entity", label="hist", \
                    maxx=None, minx=None, numbins=30, log=False, normed=True)

    plot_histogram(timeline_length, ylabel="probability", xlabel="value", title="Number of hours per entity", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)

    plot_log_log(timeline_length, ylabel="probability", xlabel="value", title="Number of hours per entity", label="hist", \
                    maxx=None, minx=None, numbins=30, log=True, normed=True)


