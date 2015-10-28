#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The script analyses output logs of NoIndex processing."""


import sys
sys.path.append("../")

from base.bursts_jaccard import numbursts_lower_bound
from output_parse import *

def block_start(line):
    return ("Considering" in line)


def block_end(line):
    return ("Current output size" in line)


def parse_header(line):
    """Parsing lines like this: Considering 369 vs. 384 or Considering 369"""
    line = line.strip()
    if "vs" in line:
        nb1 = int(line.split(" ")[-1])
        nb2 = int(line.split(" ")[-3])
        return min(nb1, nb2), max(nb1, nb2)
    nb = int(line.split(" ")[-1])
    return nb, nb


def parse_block(block):
    time        = round( extract_clock_value(block[-1])-extract_clock_value(block[0]), 4)
    nb1, nb2    = parse_header(block[0])
    return nb1, nb2, time


def build_numbursts_dict(lines, verbose=False):
    queries_dict = {} #(query bursts_per_entity, index bursts_per_entity)
    prevblock = None
    for block in yield_blocks(lines, block_start, block_end):
        try:
            nb1, nb2, time = parse_block(block)             
            queries_dict[(nb1, nb2)] = time
            if verbose: print "query block for %i vs. %i: %s" % (nb1, nb2, block)
        except Exception as e:
            print "\nERROR (",e,") WHILE PROCESSING BLOCK:",block,"\n"
    return queries_dict   


if __name__=="__main__":
    
    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    print "The script analyses output logs of R-Trees-based Index."
    print "Logs are read from stdin."

    lines = list(line.strip() for line in fin.readlines())
    JT = extract_JT(lines)   
    print "JT = %.4f" % JT
    queries_dict = build_numbursts_dict(lines, verbose=False)
    print "queries_dict =", queries_dict 

    print "Querying Index costs:"
    keys = sorted(set(map(lambda k: k[1], queries_dict.keys())))
    print "keys:", min(keys), "-", max(keys)
    for numbursts in xrange(min(keys), max(keys)+1):
        total_time = 0
        total_queries = 0
        total_candidates = 0 

        for numbursts2 in xrange(numbursts_lower_bound(numbursts, JT), numbursts+1):
            total_time += queries_dict[(numbursts2, numbursts)]

        #print numbursts, total_time
        print total_time

            
    
