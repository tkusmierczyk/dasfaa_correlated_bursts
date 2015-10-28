#!/usr/bin/python
# -*- coding: utf-8 -*-

#from ontology.log import *

import inspect
import sys
import datetime


def str_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def info(txt):
    print "[INF]["+str_time()+"][",inspect.stack()[1][3],"]",txt


def dbg(txt):
    print "[DBG]["+str_time()+"][",inspect.stack()[1][3],"]",txt


def err(txt):
    if not txt.endswith("\n"): txt = txt+"\n"
    sys.stderr.write( "[ERR]["+str_time()+"][ "+str(inspect.stack()[1][3])+" ] "+str(txt))


def error(txt):
    if not txt.endswith("\n"): txt = txt+"\n"
    sys.stderr.write( "[ERR]["+str_time()+"][ "+str(inspect.stack()[1][3])+" ] "+str(txt))


def warn(txt):
    if not txt.endswith("\n"): txt = txt+"\n"
    sys.stderr.write( "[WRN]["+str_time()+"][ "+str(inspect.stack()[1][3])+" ] "+str(txt))

def warning(txt):
    if not txt.endswith("\n"): txt = txt+"\n"
    sys.stderr.write( "[WRN]["+str_time()+"][ "+str(inspect.stack()[1][3])+" ] "+str(txt))


