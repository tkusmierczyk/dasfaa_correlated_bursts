#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Statistics of indexing of bursts from many timelines."""

import sys
sys.path.append("../")

from base.aux import *
from index.bursts_index_list import *
from bursts_index_rtrees import *
from base.bursts_stats import bursts_stats

import time

def print_numbursts2entities(fout, numbursts2entities, entites_formatter = lambda entities: "%i, " % len(entities)):
    for numbursts, entities in numbursts2entities:
        fout.write( "%s: %s" % (str(numbursts), str(entites_formatter(entities))) )
    fout.write("\n")
   
 
def calc_numentities_in_range(numbursts2entities, numbursts_range):
    return sum(len(numbursts2entities.get(numbursts, list())) for numbursts in numbursts_range)


def calc_numbursts_in_range(numbursts2entities, numbursts_range):
    return sum(sum(len(bursts) for name, bursts in numbursts2entities.get(numbursts, list())) for numbursts in numbursts_range)


if __name__=="__main__":

    fout = sys.stdout
    sys.stdout = sys.stderr

    print "The script reads bursts and calculates some stats."
    
    try: path = sys.argv[1]
    except: sys.stderr.write("Arg expected: input data file!\n"); sys.exit(-1)

    print "Loading data from %s" % path
    name2bursts = list( yield_name2bursts(open(path)) )
    print "[%f] %i loaded" % (time.clock(), len(name2bursts))

    data_size, tmin, tmax, bursts_stats = bursts_stats(name2bursts)
    print  "N =",data_size,"tmin =", tmin,"tmax =", tmax, "bursts_stats =", bursts_stats
        
    print "[%f] Computing numbursts2entities" % (time.clock())
    numbursts2entities = calc_numbursts2entities(name2bursts, element_constructor = lambda name, bursts: (name, bursts))
    #print_key2entities(numbursts2entities.iteritems(), fout, entities_formatter = lambda entities: "%i" % len(entities))

    print "Num entities with numbursts in [0, 3]:", calc_numentities_in_range(numbursts2entities, range(0,4))
    print "Num entities with numbursts in [0, 4]:", calc_numentities_in_range(numbursts2entities, range(0,5))
    print "Num entities with numbursts in [0, 5]:", calc_numentities_in_range(numbursts2entities, range(0,6))
    print "Num entities with numbursts in [5, 10]:", calc_numentities_in_range(numbursts2entities, range(5,11))    
    print "Num entities with numbursts in [10, 20]:", calc_numentities_in_range(numbursts2entities, range(10,21))    
    print "Num entities with numbursts in [10, 30]:", calc_numentities_in_range(numbursts2entities, range(10,31))        
    print "Num entities with numbursts in [10, 40]:", calc_numentities_in_range(numbursts2entities, range(10,41))        
    print "Num entities with numbursts in [10, 50]:", calc_numentities_in_range(numbursts2entities, range(10,51))
    print "Num entities with numbursts in [50, 100]:", calc_numentities_in_range(numbursts2entities, range(50,101))
    print "Num entities with numbursts in [20, 10000]:", calc_numentities_in_range(numbursts2entities, range(20,10001))
    print "Num entities with numbursts in [30, 10000]:", calc_numentities_in_range(numbursts2entities, range(30,10001))
    print "Num entities with numbursts in [50, 10000]:", calc_numentities_in_range(numbursts2entities, range(50,10001))
    print "Num entities with numbursts in [100, 10000]:", calc_numentities_in_range(numbursts2entities, range(100,10001))
    print "Num entities with numbursts in [100, 200]:", calc_numentities_in_range(numbursts2entities, range(100,201))

    for i in xrange(1, 20):
        print "Num entities with numbursts in [%i, %i]:" % (i*10, (i+1)*10), calc_numentities_in_range(numbursts2entities, range(i*10, (i+1)*10+1))

    for i in xrange(1, 20):
        print "Num entities with numbursts in [%i, %i]:" % (i*100, (i+1)*100), calc_numentities_in_range(numbursts2entities, range(i*100, (i+1)*100+1))


    print "Num bursts in entities with numbursts in in [0, 3]:", calc_numbursts_in_range(numbursts2entities, range(0,4))
    print "Num bursts in entities with numbursts in in [0, 4]:", calc_numbursts_in_range(numbursts2entities, range(0,5))
    print "Num bursts in entities with numbursts in in [0, 5]:", calc_numbursts_in_range(numbursts2entities, range(0,6))
    print "Num bursts in entities with numbursts in in [5, 10]:", calc_numbursts_in_range(numbursts2entities, range(5,11))    
    print "Num bursts in entities with numbursts in in [10, 20]:", calc_numbursts_in_range(numbursts2entities, range(10,21))    
    print "Num bursts in entities with numbursts in in [10, 30]:", calc_numbursts_in_range(numbursts2entities, range(10,31))        
    print "Num bursts in entities with numbursts in in [10, 40]:", calc_numbursts_in_range(numbursts2entities, range(10,41))        
    print "Num bursts in entities with numbursts in in [10, 50]:", calc_numbursts_in_range(numbursts2entities, range(10,51))
    print "Num bursts in entities with numbursts in in [50, 100]:", calc_numbursts_in_range(numbursts2entities, range(50,101))
    print "Num bursts in entities with numbursts in in [20, 10000]:", calc_numbursts_in_range(numbursts2entities, range(20,10001))
    print "Num bursts in entities with numbursts in in [30, 10000]:", calc_numbursts_in_range(numbursts2entities, range(30,10001))
    print "Num bursts in entities with numbursts in in [50, 10000]:", calc_numbursts_in_range(numbursts2entities, range(50,10001))
    print "Num bursts in entities with numbursts in in [100, 10000]:", calc_numbursts_in_range(numbursts2entities, range(100,10001))
    print "Num bursts in entities with numbursts in in [100, 200]:", calc_numbursts_in_range(numbursts2entities, range(100,201))

    for i in xrange(1, 20):
        print "Num bursts in entities with numbursts in in [%i, %i]:" % (i*10, (i+1)*10), calc_numbursts_in_range(numbursts2entities, range(i*10, (i+1)*10+1))

    for i in xrange(1, 20):
        print "Num bursts in entities with numbursts in in [%i, %i]:" % (i*100, (i+1)*100), calc_numbursts_in_range(numbursts2entities, range(i*100, (i+1)*100+1))

