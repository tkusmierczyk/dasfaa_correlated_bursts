#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reads (already processed and normalized) pageviews files."""


import urllib


def parse_line(line, delimeter=" "): 
    parts = line.strip().split(delimeter)
    project = parts[0]
    name = parts[1]
    date = parts[2]
    time = parts[3]
    meta = parts[4]
    timeline = parts[5:]
    return project, name, date, time, meta, timeline


def unify_name(name):
    name = urllib.unquote(name)
    name = name.strip().replace(" ", "_")
    name = name[0].upper()+name[1: ]
    return name


def construct_line(project, name, date, time, meta, timeline, delimeter=" "):
    delimeter = str(delimeter)
    timeline_str = delimeter.join( str(o) for o in timeline )
    return str(project)+delimeter+str(name)+delimeter+str(date)+delimeter+\
                            str(time)+delimeter+str(meta)+delimeter+timeline_str;


def yield_entries(fin):
    for line in fin.xreadlines():
        if line.strip()=="" or line.strip()[0]=="#": continue
        yield parse_line(line)


def yield_entity2data(fin):
    for project, name, date, time, meta, timeline in yield_entries(fin):
        yield (name, (project, name, date, time, meta, timeline) )


def build_entity2data_safe(fin):
    entity2data = {}
    for name, data in yield_entity2data(fin):
        if name in entity2data:
            print "WARNING! Entity <"+name+"> included more than once in data!"
        entity2data[name] = data
    return entity2data


def build_entity2data(fin):
    #return dict( (name, (project, name, date, time, meta, timeline) ) \
    #            for project, name, date, time, meta, timeline in yield_entries(fin) )
    return build_entity2data_safe(fin)


def entity_str(entity):
    project, name, date, time, meta, timeline = entity
    return str(name)+"-"+date+time+"-"+str(meta)+"-"+str(len(timeline))


def is_1_before_2(date1, time1, date2, time2):
    date1 = int(date1[:8])
    time1 = int(time1[:2])
    date2 = int(date2[:8])
    time2 = int(time2[:2])
    if date1<date2: before=True
    elif date1==date2 and time1<time2: before=True
    else: before = False
    return before









