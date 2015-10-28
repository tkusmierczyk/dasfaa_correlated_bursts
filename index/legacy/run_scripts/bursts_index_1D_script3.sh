#!/bin/sh

echo "The script reads bursts and correlates them using 1D index."

#verify arguments:


if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.975

echo "RUNNING 100-60"

MIN=90
MAX=100
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=85
MAX=95
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=80
MAX=90
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=75
MAX=85
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=70
MAX=80
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=65
MAX=75
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=60
MAX=70
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait
echo "RUNNING 65-40"

MIN=55
MAX=65
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=50
MAX=60
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=45
MAX=55
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &


MIN=40
MAX=50
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait
echo "RUNNING 45-30"

MIN=35
MAX=45
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=30
MAX=40
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait
echo "RUNNING 35-20"

MIN=25
MAX=35
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=20
MAX=30
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait
echo "DONE."






