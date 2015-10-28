#!/bin/sh

echo "The script reads bursts and correlates them using 1D index."

#verify arguments:


if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.9
echo "RUNNING 25-50 JI=$JI"

MIN=25
MAX=35
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &


MIN=35
MAX=50
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait
echo "RUNNING 32-39 (BORDERS) JI=$JI"

MIN=32
MAX=39
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait
echo "DONE."

