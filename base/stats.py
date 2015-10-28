#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Auxiliary methods for statistical analysis of the data and plotting."""

import math
import sys
import numpy as np
import matplotlib
import pylab 

from matplotlib import pyplot


def ufraction(values, fraction=0.95):
    """Calculates value that splits data in given proportion (to the up)."""
    return sorted(values)[min([int(math.floor(len(values)*fraction)), len(values)-1])]


def tfraction(values):
    return np.mean(values)+5.0*np.std(values)


def lenk(x, k):
    return sum(1 for e in x if e==k) 


def len_krange(x, rng):
    return sum(lenk(x, k) for k in rng)


def lengk(x, k):
    return sum(1 for e in x if e>=k) 


def recalc_prec(x, prec):
    """Adjusts (only if prev<=0) precision for given data."""
    if prec<=0: 
        if np.percentile(x, 10)!=0: tick=abs(np.percentile(x, 10))
        elif np.median(x)!=0: tick = abs(np.median(x)) 
        elif np.mean(x)!=0: tick = abs(np.mean(x))
        else:   tick = abs(np.max(x))
        try:    prec = int(math.ceil(math.log(1.0/tick,10)))
        except: prec = 4
    return prec


def stats_string(x, prec=-1):
    """Calculates string containing basic statistic about numeric data variable x.

       Args:
            prec: Statistic values precision. 
    """
    prec = recalc_prec(x, prec)
    if max(x)>1:
        formatter = "B=%%i  min=%%.0f max=%%.0f median=%%.0f mean=%%.%if std=%%.%if" \
                    % (prec, prec)
        return formatter % \
                ( len(x), min(x), max(x), np.median(x), np.mean(x), np.std(x) )
    
    formatter = "B=%%i  Q1/10=%%.%if Q5/10=%%.%if Q9/10=%%.%if  min=%%.%if max=%%.%if median=%%.%if mean=%%.%if std=%%.%if" \
                    % (prec, prec, prec, prec, prec, prec, prec, prec)
    return formatter % \
                ( len(x), np.percentile(x, 10), np.percentile(x, 50), np.percentile(x, 90), \
                  min(x), max(x), np.median(x), np.mean(x), np.std(x) )


def reset_pyplot():
    pyplot.cla()
    pyplot.clf()
    pyplot.close()


def calc_hist(x, bins, weights1, multiplexy):
    h1, edges1 = np.histogram(x, bins, weights=weights1, normed=False)
    h1 = list(h1)
    if multiplexy:  
        h1 = list( h1[i]*0.5*(edges1[i]+edges1[i+1]) for i in xrange(len(h1)) )
    h1 = [h1[0]]+h1
    return h1, edges1


def plotting(x, y=None, wy=None, wx=None, \
                 fraction=None, numbins=100, \
                 label1 = "data1", label2 = "data2", \
                 title="Data distribution",\
                 xlabel="value", ylabel="probability",  \
                 xmax=None, xmin=None, ymax=None, \
                 logx=False, log=False, prec=-1, multiplexy=False):
    """Universal plotting (use this method to plot everything)."""

    if y is None: y=x

    if wx is None: wx = 1.0/len(x)
    if wy is None: wy = 1.0/len(y)
    weights1, weights2 = list(wx for e in x), list(wy for e in y)

    #ranges:
    if xmax is None:
        if fraction is None: fraction = 1.0
        minv, maxv = min(x+y), ufraction(x+y, fraction)  
    else:
        minv, maxv = 0, xmax
    bins = np.linspace(minv, maxv, numbins+1)

    #plotting
    reset_pyplot()
    pylab.figure(num=None, figsize=(6, 3), dpi=90, facecolor='w', edgecolor='k')
    pyplot.subplots_adjust(left=0.175, right=0.95, top=0.875, bottom=0.175) 
    font = {'family': 'normal', 'weight': 'bold', 'size': 16}
    matplotlib.rc('font', **font)
    #pyplot.figure(num=None, figsize=(10, 6.5), dpi=30, facecolor='w', edgecolor='k')
    #pyplot.figure(facecolor='w', edgecolor='k')

    h1, edges1 = calc_hist(x, bins, weights1, multiplexy)
    p1 = pyplot.plot(edges1, h1, color="red", label=label1,  drawstyle='steps')

    if y!=x:
        h2, edges2 = calc_hist(y, bins, weights2, multiplexy)
        p2 = pyplot.plot(edges2, h2, color="black", label=label2,  drawstyle='steps')

    #pyplot.legend()
    prec = recalc_prec(x, prec)
    descr = stats_string(x, prec)
    pyplot.annotate("["+label1+"]\n"+descr.replace(" ", "\n"), xy=(1.0, 1.0), xytext=(-100, -10), \
                 va='top', xycoords='axes fraction', textcoords='offset points', color="red", fontsize=16)

    if x!=y:        
        descr = stats_string(y, prec)
        pyplot.annotate("["+label2+"]\n"+descr.replace(" ", "\n"), xy=(1.0, 1.0), xytext=(-200, -10), \
                 va='top', xycoords='axes fraction', textcoords='offset points', color="black", fontsize=16)

    if logx:    pyplot.xscale('log')
    if log:     pyplot.yscale('log')
    pyplot.ylabel(ylabel) 
    pyplot.xlabel(xlabel)
    pyplot.title(title)
    pyplot.grid(True)
    x1,x2,y1,y2 = pyplot.axis()
    if ymax: y2 = ymax
    if xmin: x1 = xmin 
    if xmax: x2 = xmax
    pyplot.axis( (x1, x2, 0, y2) )
    pyplot.show()


plot_compare = plotting


def plot_log_log(x, ylabel="probability", xlabel="value", title="Histogram", label="hist", \
                    maxx=None, minx=None, numbins=10, log=True, logx=False, normed=True, prec=1):
    if len(x) <= 0: return

    h1, edges1      = np.histogram(x, normed=normed, bins=numbins)
    edge_centers    = list( 0.5*(edges1[i-1]+edges1[i]) for i in xrange(1, len(edges1)) )
    plot            = pyplot.plot(edge_centers, h1, color="red")

    #pyplot.legend()
    descr = stats_string(x, prec)
    pyplot.annotate(descr.replace(" ", "\n"), xy=(1.0, 1.0), xytext=(-150, -12), \
                 va='top', xycoords='axes fraction', textcoords='offset points')
    if logx:    pyplot.xscale('log')
    if log:     pyplot.yscale('log')
    pyplot.ylabel(ylabel) 
    pyplot.xlabel(xlabel)
    pyplot.title(title)
    pyplot.grid(True)
    x1,x2,y1,y2 = pyplot.axis()
    if normed: y1, y2 = 0.0, min(y2, 1.0)
    if not minx is None: x1=minx
    if not maxx is None: x2=maxx
    pyplot.axis((x1,x2,y1,y2))
    pyplot.show()

    return list(edges1), list(h1)


def plot_histogram(x, ylabel="probability", xlabel="value", title="Histogram", label="hist", \
                    maxx=None, minx=None, numbins=10, log=True, logx=False, normed=True, prec=1):
    if len(x) <= 0: return
    if normed:  weights = list(1.0/len(x) for i in x)
    else:       weights = None

    h1, edges1  = np.histogram(x, normed=False, bins=numbins)
    pyplot.hist(x, numbins, histtype='step', label=label, weights=weights, color="red")

    #pyplot.legend()
    descr = stats_string(x, prec)
    pyplot.annotate(descr.replace(" ", "\n"), xy=(1.0, 1.0), xytext=(-150, -12), \
                 va='top', xycoords='axes fraction', textcoords='offset points')
    if logx:    pyplot.xscale('log')
    if log:     pyplot.yscale('log')
    pyplot.ylabel(ylabel) 
    pyplot.xlabel(xlabel)
    pyplot.title(title)
    pyplot.grid(True)
    x1,x2,y1,y2 = pyplot.axis()
    if normed: y1, y2 = 0.0, min(y2, 1.0)
    if not minx is None: x1=minx
    if not maxx is None: x2=maxx
    pyplot.axis((x1,x2,y1,y2))
    pyplot.show()

    return list(edges1), list(h1)


def plot_distribution(x, numbins=100,  \
                      title="Distribution",  xlabel="x", ylabel="y", \
                      prec=1, normed=False, log=False, logx=False):
    if len(x)==0: return

    #ranges:
    minv, maxv = 1, max(x)   #min(x)
    bins = np.linspace(minv, maxv, numbins)

    #plotting
    reset_pyplot()
    pyplot.figure(num=None, figsize=(10, 6.5), dpi=90, facecolor='w', edgecolor='k')

    h1,edges1 = np.histogram(x, bins, weights=list(1 for e in x), normed=normed)
    p1 = pyplot.step(edges1[1:], h1, color="red")
   
    #pyplot.legend()
    descr = stats_string(x, prec)
    pyplot.annotate(descr.replace(" ", "\n"), xy=(1.0, 1.0), xytext=(-150, -12), \
                 va='top', xycoords='axes fraction', textcoords='offset points')
    if logx:    pyplot.xscale('log')
    if log:     pyplot.yscale('log')
    pyplot.ylabel(ylabel) 
    pyplot.xlabel(xlabel)
    pyplot.title(title)
    pyplot.grid(True)
    x1,x2,y1,y2 = pyplot.axis()
    pyplot.axis((x1,x2,y1,y2))

    pyplot.show()


def summarization(x, plot=False):
    """Prints out summary about numeric data x."""
    print "Stats:", stats_string(x)
    print "Percentiles [0:0.1:1.0]:", list(np.percentile(x, i*10) for i in xrange(11))
    print "Percentiles [0.9:0.01:1.0]:", list(np.percentile(x, 90+i) for i in xrange(11))
    if plot: plotting(x, x) 


if __name__=="__main__":

    print "The script plots statistics of data (one number per line) loaded from stdin."

    fin = sys.stdin
    fout = sys.stdout
    sys.stdout = sys.stderr

    try:
        title = sys.argv[1]
    except:
        title = "Data plot"

    try:
        xlab = sys.argv[2]
    except:
        xlab = "value"

    print "Loading data from %s..." % str(fin)
    values = list( float(v) for v in fin.xreadlines() if v.strip()!="" and v[0]!="#" )

    print "Summarization..."
    summarization(values, plot=False)

    print "Plotting..."

    plotting(values,  \
                 fraction=None, numbins=100, \
                 label1 = "data1", label2 = "data2", \
                 title=title,\
                 xlabel=xlab, ylabel="probability/bin (#bins=100)",  \
                 xmax=None, xmin=None, ymax=None, \
                 logx=False, log=False, prec=1, multiplexy=False)

    plot_histogram(values, ylabel="probability/bin (#bins=100)", xlabel=xlab, title=title, \
                   log=False, normed=True, prec=3, numbins=100)
    plot_histogram(values, ylabel="probability/bin (#bins=100)", xlabel=xlab, title=title, \
                   log=True, normed=True, prec=3, numbins=100)

    plot_distribution(values, numbins=100,  title=title, xlabel=xlab, ylabel="count", prec=3, normed=False)
    plot_distribution(values, numbins=100,  title=title, xlabel=xlab, ylabel="probability", prec=3, normed=True)

    plot_log_log(values, ylabel="probability", xlabel=xlab, title=title, label="hist", \
                    maxx=None, minx=None, numbins=100, log=True, normed=True, prec=3)
    plot_log_log(values, ylabel="count", xlabel=xlab, title=title, label="hist", \
                    maxx=None, minx=None, numbins=100, log=True, normed=True, prec=3)








    
