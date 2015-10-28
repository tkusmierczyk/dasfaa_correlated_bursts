#!/bin/sh

echo "The script reads bursts and correlates them using 1D index."

#verify arguments:


if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.8

echo "RUNNING 100-250"

MIN=100
MAX=150
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=150
MAX=200
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=200
MAX=250
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "RUNNING 250-1200"

MIN=250
MAX=400
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=400
MAX=600
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=600
MAX=1200
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "DONE."

