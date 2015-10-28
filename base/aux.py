#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Auxiliary methods for maths, processing and io."""

import math
import log
from itertools import izip, imap


INF = float('inf')
CSV_SEPARATOR = " "


newton = lambda n,k: math.factorial(n)/math.factorial(k)/math.factorial(n-k)


def gaussian_density(m, s, x):
    a = 1.0 / s / math.sqrt(2.0*math.pi)
    b = (x-m) / s
    return a * math.exp(-0.5 * b*b)


def predicate_del_spacename(p):
    """Removes spacename from text rdfs:sthing -> sthing."""
    parts = p.split(":")
    if len(parts) == 1: return p
    else: return parts[1]


def is_two_types_predicate(p):
    """Whether predicate p is a between-two-types-specific relation."""
    return (p=="subclassof")


def is_type_predicate(p):
    """Whether predicate p is a type-specific relation."""
    return (p=="type" or p=="subclassof")


def load_csv_header(f, csvseparator=CSV_SEPARATOR, cast_method=lambda x: str(x).strip()):
    """Loads CSV file and returns just header."""
    import csv
    dmsoreader = csv.reader(f, delimiter=csvseparator)            
    header = dmsoreader.next()    
    return list(cast_method(e) for e in header)


def load_csv_rows(f, csvseparator=CSV_SEPARATOR, cast_method=lambda x: str(x).strip()):
    """Loads CSV file and yields rows (assumes that header is already loaded with load_csv_header)."""
    #import csv
    #dmsoreader = csv.reader(f, delimiter=csvseparator)            
    #for row in dmsoreader:
    for row in f.xreadlines():  
        row = row.strip()
        if len(row)==0 or row[0]=="#": continue
        #print row, "->", row.split(csvseparator)
        row = row.split(csvseparator)
        yield list(cast_method(e) for e in row)



def project(rows, col_ixs=[0]):
    return imap(lambda row: map(lambda ix: row[ix], col_ixs), rows)
        

def sort_o2c_dictionary(obj2count, reverse_order=True):
    lst = sorted(((c,o) for o,c in obj2count.iteritems()), reverse=reverse_order)
    return list( (o,c) for c,o in lst)
    

############################################################################################


def key2list_2_key2len(key2list):
    return dict( (k,len(l)) for k,l in key2list.iteritems() )

    
def lst2dcounts(lst):
    """Converts list->dictionary{element: count}."""
    counts = {}
    for e in lst:
        counts[e] = counts.get(e, 0) + 1
    return counts


def convert_dict2list_dict2dcounts(dict2list):
    dict2counts = {}
    for k,lst in dict2list.iteritems():
        dict2counts[k] = lst2dcounts(lst)
    return dict2counts


############################################################################################


def insert_dict2set(dict2set, key, element):
    if key in dict2set: dict2set[key].add(element)
    else: dict2set[key] = set([element])


def insert_dict2list(dict2list, key, element):
    lst = dict2list.get(key, [])
    lst.append(element)
    dict2list[key] = lst


############################################################################################


def yield_map(fin, sep=" "):
    for line in fin.xreadlines():
        line = line.strip()
        if line.strip()=="" or line[0]=="#": continue
        yield line.split(sep)


def store_o2c_list(output, obj2count_list, separator=CSV_SEPARATOR):
    log.dbg("writting list of pairs {key: count-value} to %s" % str(output))
    for o,c in obj2count_list:
        output.write(str(o)+separator+str(c)+"\n")


def store_o2c_dict(output, obj2count_dict, separator=CSV_SEPARATOR):
    log.dbg("writting dictionary {key: value} to %s" % str(output))
    for o,c in obj2count_dict.iteritems():
        output.write(str(o)+separator+str(c)+"\n")
    

def store_k2l_dictionary(output, key2list, separator=CSV_SEPARATOR):
    log.dbg("writting dictionary {key: list-of-peers} to %s" % str(output))
    key2len = key2list_2_key2len(key2list)
    len2key = sorted( ((l,k) for k,l in key2len.iteritems()), reverse=True)
    keys = list(k for _, k in len2key)
    for k in keys:
        lst = key2list[k]
        output.write(str(k)+"["+str(len(lst))+"]"+separator)
        output.write( reduce(lambda e1,e2: e1+separator+e2, (str(e) for e in lst) ) )
        output.write("\n")


def store_k2dc_dictionary(output, key2dc, separator=CSV_SEPARATOR):
    log.dbg("writting dictionary {key: dictionary{peer: count} } to %s" % str(output))
    key2len = key2list_2_key2len(key2dc)
    len2key = sorted( ((l,k) for k,l in key2len.iteritems()), reverse=True)
    keys = list(k for _, k in len2key)
    for k in keys:
        dc = key2dc[k]
        output.write(str(k)+"["+str(len(dc))+"]"+separator)
        counts_generator = (str(e)+":"+str(c) for e,c in dc.iteritems())
        output.write( reduce(lambda e1,e2: e1+separator+e2, counts_generator) )
        output.write("\n")


def store_list(output, lst):
    log.dbg("writting list to %s" % str(output))
    for e in lst:
        output.write(str(e)+"\n")


def extract_pairdict2weight_keys(pairdict2weight):
    keys = set()
    for key in pairdict2weight:
        keys.add(key[0])
        keys.add(key[1])
    keys = list(sorted(keys))
    return keys


def check_pairdict2weight_symmetric(pairdict2weight):
    keys = extract_pairdict2weight_keys(pairdict2weight)
    for k1 in keys:
        for k2 in keys:
            if pairdict2weight[(k1,k2)] != pairdict2weight[(k2,k1)]:
                return False
    return True
    

def store_pairdict2weight(output, pairdict2weight, separator=CSV_SEPARATOR):
    log.dbg("writting dictionary { (key1,key2): count } to %s" % str(output))
    log.dbg("airdict2weight:"+str(list(pairdict2weight.iteritems())))

    keys = sorted( extract_pairdict2weight_keys(pairdict2weight) )

    output.write("%s" % str(separator))
    output.write( reduce(lambda e1,e2: e1+separator+e2, (str(e) for e in keys)) )
    output.write("\n")
    
    for k1 in keys:
        weight_generator = ( ("%.12f" % pairdict2weight[k1,k2]) for k2 in keys)
        output.write("%s%s" % (str(k1), str(separator)))
        output.write( reduce(lambda e1,e2: e1+separator+e2, weight_generator) )
        output.write("\n")


def load_pairdict2weight(f, separator=CSV_SEPARATOR):
    log.dbg("loading dictionary { (key1,key2): count } from %s" % str(f))
    d = {}
    keys2 =  list( e.strip() for e in f.readline().strip().split(separator) if e.strip()!="" )
    for line in f.xreadlines():
        parts = line.strip().split(separator)
        key1 = parts[0].strip()
        for key2, weight in izip(keys2, parts[1:]):
            try: weight = int(weight)
            except: weight = float(weight)
            d[(key1,key2)] = weight
    return d


def hist(values):
    import numpy        
    return  numpy.histogram(values, bins=10, normed=False)


def entity_name_format(name):
    return name.lower().replace("<","").replace(">","").replace("_","").replace(".","")


def k2w_str(k2w_dictionary, inv=True, limit=200):
    size = str(len(k2w_dictionary))
    content = str( list( sorted( list( (w,k) for k,w in k2w_dictionary.iteritems() ), reverse=inv) )[:limit] )[:5*limit]
    return "dict["+size+"]{"+content+"}"


def print_key2entities(key2entities, fout, entities_formatter = lambda entities: "%i" % len(entities)):
    for key, entities in key2entities:                
        fout.write("%s " % str(key))
        fout.write(entities_formatter(entities))
        fout.write("\n")


def assign_pow2_ceil(value):
    for i in xrange(1, 100): 
        if pow(2, i)  >value: return int(pow(2, i))
    return int(pow(2, 100))


def store_matrix(fout, matrix, element_formatter=lambda e: str(e)):
    for row in matrix:
        fout.write( " ".join(element_formatter(e) for e in row) )
        fout.write("\n")


def store_values(fout, values):
    for v in values:
        fout.write(str(v))
        fout.write("\n")


def store_list_of_lists(fout, l2l, separator="\t"):
    for row in l2l:        
        fout.write( separator.join( str(e) for e in row ) )
        fout.write("\n")


def load_list_of_lists(fin, element_extractor=int, separator="\t"):
    l2l = []
    for line in fin.xreadlines():        
        if line.strip()=="" or line[0]=="#": continue
        row = list(element_extractor(e) for e in line.strip().split(separator))
        l2l.append(row)
    return l2l


def ensure_list_of_lists_length(lst, length):
    while len(lst) < length: lst.append(list())
    return lst


def ensure_list_of_ints_length(lst, length):
    while len(lst) < length: lst.append(0)
    return lst


def yield_dlists(d, minval, maxval):
    if d<=1:
        for i in xrange(minval, maxval+1):
            yield [i]
    else:
        for i in xrange(minval, maxval+1):
            for lst in yield_dlists(d-1, minval, maxval):
                yield lst+[i]


def slog(value):
    if value==0.0:
        return 0.0
    else:
        return math.log(value)


def safe_div(a,b):
    if b==0: return 0.0
    return float(a)/b


def average_value2weight(value2weight):
    sums = 0
    total = 0
    for v, w in value2weight:
        sums    += v*w
        total   += w
    return float(sums)/total


def value2list_to_len2value(value2list):
    len2value = list()
    for val, lst in value2list.iteritems():
        len2value.append( (len(lst), val) )
    len2value = sorted(len2value, reverse=True)
    return len2value


def calc_value2count(values):
    value2count = dict()
    for v in values:
        value2count[v] =  value2count.get(v, 0) + 1
    return value2count


def nested(set1, set2):
    #set1, set2 = set(set1), set(set2)
    both = len( set1.intersection(set2) )
    return both==len(set1) or both==len(set2)


def _ensure_list_of_lists_length_(lst, length):
    while len(lst) < length: lst.append(list())


def _ensure_list_of_numbers_length_(lst, length):
    while len(lst) < length: lst.append(0)





