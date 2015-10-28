#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Jaccard Index calculation on bursts."""

import sys
sys.path.append("../")

import math
from base.bursts import overlap, bursts_overlap
from aux import safe_div

def calc_num_overlapping_each(bursts1, bursts2):
    """Calculates min(overlapping1, overlapping2).

        Assumptions: bursts are not overlapping internally (not nested!) and are sorted.
    """
    if len(bursts1)==0 or len(bursts2)==0: return 0, 0

    i, j = 0, 0
    overlapping1, overlapping2 = 0, 0
    prev1, prev2 = None, None
    while i<len(bursts1) and j<len(bursts2):
        level1, first1, last1 = bursts1[i]
        level2, first2, last2 = bursts2[j]        

        if overlap(first1, last1, first2, last2):
            overlapping1 += int(prev1 is None  or  bursts1[i]!=prev1)
            overlapping2 += int(prev2 is None  or  bursts2[j]!=prev2)
            prev1, prev2 = bursts1[i], bursts2[j] 

        if last1<last2:
            i += 1
        elif last1>last2:
            j += 1
        else:
            i += 1
            j += 1

    return overlapping1, overlapping2


def calc_num_overlapping(bursts1, bursts2):
    """Calculates min(overlapping1, overlapping2).

        Assumptions: bursts are not overlapping internally (not nested!) and are sorted.
    """
    overlapping1, overlapping2 = calc_num_overlapping_each(bursts1, bursts2)
    return min(overlapping1, overlapping2)


def calc_num_overlapping_brutal(bursts1, bursts2):
    """Calculates min(overlapping1, overlapping2).

        This method is exaustive version of calc_num_overlapping.
    """
    set1, set2 = set(), set()
    for b1 in bursts1:
        for b2 in bursts2:
            if bursts_overlap(b1, b2): 
                set1.add(b1)
                set2.add(b2)
    return min(len(set1), len(set2))


def overlap_ratio(bursts1, bursts2):
    overlapping1, overlapping2 = calc_num_overlapping_each(bursts1, bursts2)
    return safe_div( (overlapping1+overlapping2), (len(bursts1)+len(bursts2)) )


jaccard_calc = lambda o, nb1, nb2: float(o) / (nb1+nb2-o)

def JaccardIndex(bursts1, bursts2):
    """Calculates value of Jaccard Index on bursts.

        Assumptions: bursts are not overlapping internally (not nested!) and are sorted.
    """
    overlapping = calc_num_overlapping(bursts1, bursts2)
    #return float(overlapping) / (len(bursts1)+len(bursts2)-overlapping)
    if overlapping<=0: return 0.0
    return jaccard_calc(overlapping, len(bursts1), len(bursts2))


def ceiling(v, prec=4):
    return int(math.ceil(round(v, prec)))


def min_overlapping_required(numbursts1, numbursts2, JT):
    """Calculates how many (at least) overlapping bursts is 
        required to obtain JaccardIndex value above the threshold JT."""
    return ceiling( float(JT)*(numbursts1+numbursts2) / (1.0+JT) )


def numbursts_lower_bound(numbursts, JT):
    """Calculates how many bursts must other stream have to have the chance 
        to obtain JaccardIndex value above the threshold JT."""
    return ceiling(float(numbursts) * JT)


def numbursts_range(numbursts, JT):
    """Calculates range of how many bursts must streams have to have the chance 
        to obtain JaccardIndex value above the threshold JT."""
    range_first, range_last = numbursts_lower_bound(numbursts, JT), numbursts
    return range_first, range_last


class JIOutputStorage:
    """Output storage for identified correlated pairs."""

    def __init__(self, fout):        
        self.fout = fout
        self.counter = 0 
        self.stored = set() #for backward compatibility

    def store(self, name1, name2, JI, additional=""):
        if name1==name2: return False
        self.fout.write( "%.4f %s %s %s\n" % (JI, name1, name2, str(additional)) )
        self.counter += 1
        return True

    def store_batch(self, pair2jaccard, additional=""):
        for (name1, name2), JI in pair2jaccard:
            self.store(name1, name2, JI, additional)
        self.flush()

    def flush(self):
        self.fout.flush()

    def stored_count(self):
        return self.counter


class JIOutputStorageMemory:
    """Output storage for identified correlated pairs."""

    def __init__(self, fout):        
        self.fout = fout
        self.stored = set()

    def store(self, name1, name2, JI, additional=""):
        if name1==name2: return False
        if (name1, name2) in self.stored or (name2, name1) in self.stored: return False

        self.fout.write( "%.4f %s %s %s\n" % (JI, name1, name2, str(additional)) )
        self.stored.add( (name1, name2) )
        return True

    def store_batch(self, pair2jaccard):
        for (name1, name2), JI in pair2jaccard:
            self.store(name1, name2, JI)
        self.flush()

    def flush(self):
        self.fout.flush()

    def stored_count(self):
        return len(self.stored)


def load_from_output_storage(fin):
    """Reads from storage with identified correlated pairs."""
    pair2JI = {}
    for line in fin.xreadlines():
        parts = line.split(" ")
        JI, name1, name2 = float(parts[0]), parts[1].strip(), parts[2].strip()
        if name1 == name2: continue
        name1, name2 = min(name1, name2), max(name1, name2)
        pair2JI[(name1,name2)] = JI
    return pair2JI


def JI(set1, set2):
    """Calculates value of Jaccard Index on sets. """
    JI = float( len( set1.intersection(set2) ) ) / len( set1.union(set2) )
    return JI


def JI_pairs(pairs1, pairs2):
    """Calculates value of Jaccard Index on lists of pairs. """
    set1 = set( list(i for i,j in pairs1) + list(j for i,j in pairs1) )
    set2 = set( list(i for i,j in pairs2) + list(j for i,j in pairs2) )
    return JI(set1, set2)


if __name__=="__main__":

    from base.bursts import *
    from bursts_filtering import *
    from stats import *
    
    print "The script searches for pages with bursts"
    print "where JaccardIndex>threshold in time in [start, end]."
    #print "WARNING! Input bursts should be sorted and should not be nested!"    

    try: path = sys.argv[1]
    except: sys.stderr.write("Arg expected: knowledge base data file with bursts!\n"); sys.exit(-1)

    try: qpath = sys.argv[2]
    except: sys.stderr.write("Arg expected: query data file with bursts!\n"); sys.exit(-1)
    
    try: threshold = float(sys.argv[3])
    except: sys.stderr.write("Arg expected: threshold value!\n"); sys.exit(-1)
    
    try: minbursts = int(sys.argv[4])
    except: sys.stderr.write("Arg expected: minimum number of bursts!\n"); sys.exit(-1)

    try: start = int(sys.argv[5])
    except: start = 0
    
    try: end = int(sys.argv[6])
    except: end = 10000000

    print "path = %s" % path
    print "qpath = %s" % qpath
    print "threshold = %.2f" % threshold
    print "minbursts = %i" % minbursts
    print "start = %i" % start
    print "end = %i" % end

    verbose = False

    ###########################################################################
    
    for query_line in open(qpath).xreadlines():
        if query_line.strip()=="" or query_line.strip()[0]=="#": continue

        qproject, qname, qdate, qtime, qmeta, qbursts = parse_line(query_line)
        qbursts = list( yield_kleinberg_bursts(qbursts) )
        qbursts = filter_bursts_overlapping(qbursts, start, end)
        qbursts = sorted(qbursts, key=lambda b: (b[1],b[2]))

        if any_overlap(qbursts, ignore_level=1):
            print "[scaling] ERROR: Bursts overlap!"
            sys.exit(-1)
 
        if verbose: print "Q -> ", query_line[:120]
        JIvals = list()
        fout = open("%s.%s.matched_%.2f_%i_%i_%i" % (path, qname, threshold, minbursts, start, end), "w")
        for counter, line in enumerate(open(path).xreadlines()):
            if line.strip()=="" or line.strip()[0]=="#": continue
            if counter>0 and counter%100000==0: 
                print (" %i processed " % counter)
                print "JaccardIndex stats for %s: %s" % (qname, stats_string(JIvals))

            project, name, date, time, meta, bursts = parse_line(line)
            if len(bursts) < minbursts: continue
            bursts = list( yield_kleinberg_bursts(bursts) )
            bursts = filter_bursts_overlapping(bursts, start, end)    
            bursts = sorted(bursts, key=lambda b: (b[1],b[2]))
            
            if any_overlap(bursts, ignore_level=1):
                print "[scaling] ERROR: Bursts overlap!"
                sys.exit(-1)

            JI = JaccardIndex(qbursts, bursts)
            JIvals.append(JI)
            if JI >= threshold:
                fout.write(str(JI)+" "+line)
            if verbose: print "%.3f -> %s" % (JI, line[:120])
        fout.close()
        print "JaccardIndex stats for %s: %s" % (qname, stats_string(JIvals))
        print "Output: %s" % str(fout)
           



