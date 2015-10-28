#!/bin/sh

echo "The script reads bursts and correlates them using 1D index."

#verify arguments:


if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.975

MIN=95
MAX=105
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=105
MAX=115
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=115
MAX=125
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=125
MAX=135
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=135
MAX=145
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=145
MAX=155
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=155
MAX=165
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=165
MAX=175
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=175
MAX=185
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=185
MAX=195
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=195
MAX=205
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

wait

MIN=214
MAX=226
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=234
MAX=246
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=253
MAX=267
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=273
MAX=287
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=292
MAX=308
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=331
MAX=349
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=370
MAX=390
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=435
MAX=465
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=535
MAX=565
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &

MIN=633
MAX=668
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &


wait
echo "DONE."






