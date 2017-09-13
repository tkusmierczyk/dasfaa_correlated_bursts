Code used in the following paper:

**T. Kusmierczyk, K. Nørvåg: Mining Correlations on Massive Bursty Time Series Collections. DASFAA 2015.**

-----------------------------------------------------------------------------------------------------------------

### Introduction

The software implements a novel approach for mining correlation in collections consisting
of a large number of time series. In our approach, we use bursts co-occurring in
different streams as the measure of their relatedness. By exploiting the pruning
properties of our measure we develop new indexing structures and algorithms
that allow for efficient mining of related pairs from millions of streams. 

### Requirements

The code was tested on Ubuntu 14.04 (3.18.5-031805-generic x86_64 GNU/Linux) with Python 2.7.6. The following libraries are required:
* numpy
* Rtree (and libspatialindex-dev)

On Ubuntu Rtree library can be installed as following:
```
sudo deb http://us.archive.ubuntu.com/ubuntu precise main universe
sudo apt-get update
sudo apt-get install libspatialindex-dev
sudo easy_install Rtree
```

### Data format

Scripts work with files that contain multiple bursty time series. 
Each line describes a single time serie. 
Lines contain space-separated fields: 
* group identifier (two chars) [ignored]
* time serie identifier 
* metadata [ignored]
* metadata [ignored]
* metadata [ignored]
* a list of space-separated bursts in the time serie.
Each burst is described with 3 comma-separated numbers: intensity [ignored], start time, end time.

Sample entry:
`en UEFA_Euro_1992_officials 20080626 110000 meta 2,42703,42710 3,43619,43647`

Sample data can be found in `sample_data` directory.


### Running scripts

To identify correlated bursty time series use the following:
* List-based (LB) index: `index/bursts_index_list.py` `index/bursts_index_list_border_run.py`
* RTree-based High Dimensional index (IBHD): `index/bursts_index_rtrees.py`
* RTree-based Low Dimensional index (IBLD): `index/bursts_index_rtrees_ld.py`
* naive baseline: `index/bursts_noindex.py`

Python scripts can be run in parallel by sharding input files.
Entities are sharded according to the number of attached bursts.
This is done with the help of bash scripts from the directory `parallel`.

