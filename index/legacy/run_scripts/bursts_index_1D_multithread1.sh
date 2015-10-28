#!/bin/sh

echo "The script reads bursts and correlates them using 1D index."

#verify arguments:


if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.9

echo "RUNNING 100-200"

MIN=100
MAX=120
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=120
MAX=140
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=140
MAX=160
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=160
MAX=180
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=180
MAX=200
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "RUNNING 200-400"

MIN=200
MAX=240
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=240
MAX=280
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=280
MAX=320
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=320
MAX=360
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=360
MAX=400
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "RUNNING 400-1200"

MIN=400
MAX=450
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=450
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
echo "RUNNING 50-100"

MIN=85
MAX=100
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=70
MAX=85
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=60
MAX=70
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=50
MAX=60
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "RUNNING 30-50"

MIN=43
MAX=50
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=35
MAX=43
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=30
MAX=35
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "RUNNING 20-30"

MIN=27
MAX=30
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=25
MAX=27
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=22
MAX=25
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

MIN=20
MAX=22
echo "LOG = $1.index_1D_${JI}_${MIN}_${MAX}.log"
python bursts_index_1D.py $1 $JI $MIN $MAX 2> $1.index_1D_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_1D_${JI}_${MIN}_borders.log"
python bursts_index_1D_border_run.py $1 $JI $MIN 2> $1.index_1D_${JI}_${MIN}_borders.log &

wait
echo "DONE."

