#!/bin/sh

echo "The script reads bursts and correlates them using 1D index."

#verify arguments:


if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.975

MIN=100
MAX=110
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=110
MAX=120
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=120
MAX=130
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=130
MAX=140
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=140
MAX=150
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=150
MAX=160
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=160
MAX=170
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=170
MAX=180
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=180
MAX=190
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=190
MAX=200
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait

MIN=200
MAX=220
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=220
MAX=240
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=240
MAX=260
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=260
MAX=280
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=280
MAX=300
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=300
MAX=340
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=340
MAX=380
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=380
MAX=450
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=450
MAX=550
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=550
MAX=650
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=650
MAX=1200
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &


wait
echo "DONE."






