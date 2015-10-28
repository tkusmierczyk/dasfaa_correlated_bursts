#!/usr/bin/env python
# -*- coding: utf-8 -*-

def yield_blocks(lines, block_start, block_end):
    block = None
    for line in lines:
        if block_start(line):
            block = [line]
        elif block_end(line):
            block.append(line)
            yield block
            block = None
        elif block is not None:
            block.append(line)
    if block is not None:
        yield block


def extract_clock_value(line):
    return float( line.split("]")[-2].strip("[") )


def extract_equality_value(lines, name):
    vals = list( set( float(line.split("%s=" % name)[1].split(" ")[0]) for line in lines if "%s=" % name in line ) )
    if len(vals)>1:
        raise Exception("Too many values of %s=%s" % (name,str(vals)) )
    return vals[0]


def extract_JT(lines):
    return extract_equality_value(lines, "JT")


def get_value_by_name(line, name):
    parts = line.split(" ")
    for i in xrange(len(parts)):   
        if parts[i].strip()==name: return int(parts[i-1])
    return None






