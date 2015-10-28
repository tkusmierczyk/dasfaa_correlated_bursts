#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The script analyses output logs of R-Trees-based Index."""

import sys
sys.path.append("../")

from base.bursts_jaccard import numbursts_lower_bound
from output_parse import *

def block_start(line):
    return ("Building" in line or "Builiding" in line or "Querying" in line)


def block_end(line):
    return ("in total" in line and not "loaded in total" in line)


def building_block(block):
    return ("Builiding" in block[0])


def parse_header(line):
    """Parsing lines like this: Builiding 7D index out of 187955 entities with 7 bursts per enitity."""
    d = int(line.split("D")[0].split(" ")[-1])
    numentities = get_value_by_name(line, "entities")
    bursts_per_entity = get_value_by_name(line, "bursts")
    return d, numentities, bursts_per_entity


def parse_building_block(block):
    time        = round( extract_clock_value(block[-1])-extract_clock_value(block[0]), 4)
    d, numentities, bursts_per_entity = parse_header(block[0])
    numinserted = get_value_by_name(block[-1], "bursts")
    return d, numentities, bursts_per_entity, time, numinserted


def parse_querying_block(block):
    time            = round( extract_clock_value(block[-1])-extract_clock_value(block[0]), 4)
    d, numentities, bursts_per_entity = parse_header(block[0])
    numqueries      = get_value_by_name(block[-1], "tuples;")
    numcandidates   = get_value_by_name(block[-1], "candidadates)")
    return d, numentities, bursts_per_entity, time, numqueries, numcandidates


def build_numbursts_dict(lines, verbose=False):
    queries_dict = {} #(query bursts_per_entity, index bursts_per_entity) -> list of queries
    builds_dict = {}
    prevblock = None
    for block in yield_blocks(lines, block_start, block_end):
        try:
            if building_block(block):
                prevblock = parse_building_block(block)
                d, numentities, bursts_per_entity, time, numinserted = prevblock           
                builds_dict.setdefault(bursts_per_entity, list()).append(prevblock) 
                if verbose: print "building block for %i: %s" % (prevblock[2], block)
            else:
                query = parse_querying_block(block) 
                d, numentities, bursts_per_entity, time, numqueries, numcandidates =  query  
                prev_block_bursts_per_entity = prevblock[2]
                queries_dict.setdefault( (bursts_per_entity, prev_block_bursts_per_entity), list() ).append(query)
                if verbose: print "query block for %i vs. %i: %s" % (bursts_per_entity, prev_block_bursts_per_entity, block)
        except Exception as e:
            print "\nERROR (",e,") WHILE PROCESSING BLOCK:",block,"\n"
    return queries_dict, builds_dict           


if __name__=="__main__":
    
    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "The script analyses output logs of R-Trees-based Index (bursts_index_rtrees.py)."
    print "Logs are read from stdin."

    lines = list(line.strip() for line in fin.readlines())
    JT = extract_JT(lines)   
    print "JT = %.4f" % JT
    queries_dict, builds_dict = build_numbursts_dict(lines, verbose=False)
    print "queries_dict =", queries_dict 
    print "builds_dict =", builds_dict
    #JT = 0.9;     print "JT changed to %.4f" % JT

    print "Building costs:"
    for numbursts, val in builds_dict.iteritems():
        d, numentities, bursts_per_entity, time, numinserted = val[0]
        #print numbursts, d, time, numentities, bursts_per_entity, numinserted
        print time

    print "Querying Index costs:"

    keys = sorted(set(map(lambda k: k[1], queries_dict.keys())))
    print "keys:", min(keys), "-", max(keys)
    for numbursts in xrange(min(keys), max(keys)+1):
        total_time = 0
        total_queries = 0
        total_candidates = 0 

        missing = list()
        for bursts_per_entity in xrange(numbursts_lower_bound(numbursts, JT), numbursts+1):
            if (bursts_per_entity, numbursts) not in queries_dict:
                missing.append((bursts_per_entity, numbursts))
                continue
            qval = queries_dict[(bursts_per_entity, numbursts)]
            d, numentities, bursts_per_entity, time, numqueries, numcandidates = qval[0]
            total_time += time
            total_queries += numqueries
            total_candidates += numcandidates
        #if len(missing)>0: print "[ERROR] Missing pairs:", str(missing)[:100],"..."

        print total_time
        #print numbursts, total_time , total_queries, total_candidates

            
    
