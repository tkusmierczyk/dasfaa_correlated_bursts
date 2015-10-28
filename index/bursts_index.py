#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Indexing of bursts from many timelines."""

import sys
sys.path.append("../")

from base.bursts import *
from base.bursts_filtering import *
from base.bursts_stats import *
from base.aux import *


def calc_entity2numbursts(name2bursts):
    """Builds counter {entity: number of bursts}."""
    entity2numbursts = dict()
    for counter, (name, bursts) in enumerate(name2bursts):
        if counter%1000000==0: print "[calc_entity2numbursts] %i processed, index size: %i" % (counter,len(entity2numbursts))
        entity2numbursts[name] = len(bursts)
    print "[calc_entity2numbursts] len(entity2numbursts) = %i" % len(entity2numbursts)
    return entity2numbursts


def calc_numbursts2entities(name2bursts, element_constructor=lambda name, bursts: name):
    """Builds data split {number of bursts: list of entites}."""
    numbursts2entities = dict()
    for counter, (name, bursts) in enumerate(name2bursts):
        if counter%1000000==0: print "[calc_numbursts2entities] %i processed, index size: %i" % (counter,len(numbursts2entities))
        numbursts = len(bursts)
        numbursts2entities.setdefault(numbursts, list()).append( element_constructor(name, bursts) )
    print "[calc_numbursts2entities] len(numbursts2entities) = %i" % len(numbursts2entities)
    return numbursts2entities


def yield_bursts_pairs(name2bursts):
    for name, bursts in name2bursts:

        for i in xrange(len(bursts)):
            _, first1, last1 = bursts[i]
            for j in xrange(i+1, len(bursts)):
                _, first2, last2 = bursts[j]     

                yield (name, [i,j], (first1, first2, last1, last2))
                

def calc_burstpair2entities(name2bursts, key_builder = lambda t1,t2: (t1 ,t2), is_time_ok = lambda t1, t2: True):
    """Index for bursts of pairs"""
    pair2entities = dict()
    for counter, (name, bursts) in enumerate(name2bursts):
        if counter%1000==0: print "[calc_burstpair2entities] %i processed, index size: %i" % (counter,len(pair2entities)) 
        for name, ixs, (first1, first2, last1, last2) in yield_bursts_pairs(name2bursts):
            for t1 in xrange(first1, last1+1):
                for t2 in xrange(first2, last2+1):
                    if t1>t2: t1, t2 = t2, t1
                    if not is_time_ok(t1, t2): continue
                    pair2entities.setdefault(key_builder(t1,t2), set()).add(name) #todo list zamiast set-u
    return pair2entities


def extract_entities_subset(numbursts2entities, numbursts_subset):    
    subset = list()
    for numbursts in numbursts_subset:
        subset.extend( numbursts2entities.get(numbursts, list()) )
    return subset


def name2bursts_chunks(name2bursts, max_bursts_per_chunk=100000):
    chunks = list()
    chunk = list()
    chunk_size = 0
    for name, bursts in name2bursts:
        chunk.append( (name, bursts) )
        chunk_size += len(bursts)
        if chunk_size > max_bursts_per_chunk:
            chunks.append(chunk)
            chunk = list()
            chunk_size = 0
    if len(chunk)>0: chunks.append(chunk)
    return chunks


