#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The script analyses output logs from bursts_index_1D."""

import sys
sys.path.append("../")

from base.bursts_jaccard import *
from base.bursts import *
from output_parse import *

def block_start(line):
    return ("identify_linked_pairs_with_1D_index" in line and "Considering" in line)


def block_end(line):
    return ("identify_linked_pairs_with_1D_index" in line and "Current output size" in line)


def extract_numbursts(line):
    if "vs." in line:   return int(line.split(" ")[-3]), int(line.split(" ")[-1])
    else:               return int(line.split(" ")[-1]), int(line.split(" ")[-1])


def extract_numentities(line):
    return int(line.split(" ")[1])


def extract_output_size(line):
    return int(line.split(" ")[-1])


def extract_validated_vs_candidates(line):
    return int(line.split(" ")[1].split("/")[0]), int(line.split(" ")[1].split("/")[1])


def extract_validated_vs_candidates_overall(block):
    total_validated, total_candidates = 0, 0
    for line in block:
        if "above threshold" in line:
            validated, candidates = extract_validated_vs_candidates(line)               
            total_validated += validated
            total_candidates += candidates
    return total_validated, total_candidates
            

def parse_block(block):
    #print block
    numbursts   = extract_numbursts(block[0])
    time        = round( extract_clock_value(block[-1])-extract_clock_value(block[0]), 2)
    numentities = extract_numentities(block[1])
    output_size = extract_output_size(block[-1])
    validated, candidates = extract_validated_vs_candidates_overall(block)
    return numbursts, time, numentities, output_size, validated, candidates


def build_queries_dict(lines):
    queries_dict = dict()
    for block in yield_blocks(lines, block_start, block_end):
        val = parse_block(block)
        key = val[0]
        queries_dict.setdefault(key, list()).append(val)
    return queries_dict


if __name__=="__main__":
    
    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "The script analyses output logs (of bursts_index_list.py)."
    lines = list(line.strip() for line in fin.readlines() if line.strip()!="")
    JT = extract_JT(lines)   
    print "JT = %.4f" % JT
    queries_dict = build_queries_dict(lines)
    print "queries_dict = %s" % str(sorted(queries_dict.iteritems()))
    #JT = 0.9;     print "JT changed to %.4f" % JT

    keys = sorted(set(map(lambda k: k[1], queries_dict.keys())))
    print "keys:", min(keys), "-", max(keys)
    for numbursts in xrange(min(keys), max(keys)+1):
        
        time = 0.0
        missing = list()
        for bursts_per_entity in xrange(numbursts_lower_bound(numbursts, JT), numbursts+1):
            if (bursts_per_entity, numbursts) not in queries_dict:
                missing.append((bursts_per_entity, numbursts))
                continue
            time += queries_dict[(bursts_per_entity, numbursts)][0][1]
        #if len(missing)>0: print "[ERROR] Missing pairs:", str(missing)[:100],"..."

        #candidates = 0
        #candidates_num = 0
        #for i in xrange(lowerbound, numbursts+1):
        #    for j in xrange(i+1, numbursts+1):
        #        if (i,j) not in queries_dict:  
        #            if i<300:   print "MISSING:",(i,j)
        #            continue
        #        #print queries_dict[(i,j)]
        #        time += queries_dict[(i,j)][0][1]
        #        candidates += queries_dict[(i,j)][0][5]
        #        candidates_num += 1 

        print time
        #print numbursts, candidates, candidates_num
                

