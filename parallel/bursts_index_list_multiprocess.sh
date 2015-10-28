#!/bin/sh

cd ../index
echo "The script reads bursts and correlates them using list index."
echo "[processes enitites with 25-120 bursts]"

#verify arguments:

if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi
if [ -z "$2" ]
  then
    echo "ARGUMENT NEEDED: THRESHOLD VALUE"
    exit
fi
if [ -z "$3" ]
  then
    echo "ARGUMENT NEEDED: NUMPROCESSES PARALLEL"
    exit
fi
JI=$2
NUMPROC=$3


MIN=100
MAX=120
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=120
MAX=140
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=140
MAX=160
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=160
MAX=180
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=180
MAX=200
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=200
MAX=240
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=240
MAX=280
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=280
MAX=320
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=320
MAX=360
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=360
MAX=400
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=400
MAX=450
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=450
MAX=600
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=600
MAX=1200
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=85
MAX=100
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=70
MAX=85
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=60
MAX=70
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=50
MAX=60
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=43
MAX=50
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=35
MAX=43
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=30
MAX=35
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=27
MAX=30
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=25
MAX=27
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

#MIN=22
#MAX=25
#echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
#python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
#echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
#python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &

#MIN=20
#MAX=22
#echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
#python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
#echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
#python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &

wait
echo "DONE."

