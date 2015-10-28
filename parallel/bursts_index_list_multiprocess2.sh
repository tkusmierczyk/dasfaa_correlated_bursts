#!/bin/sh

cd ../index
echo "The script reads bursts and correlates them using list index."
echo "[processes enitites with 1-25 bursts]"

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


MIN=20
MAX=25
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=15
MAX=20
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=10
MAX=15
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=5
MAX=10
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN=1
MAX=10
echo "LOG = $1.index_list_${JI}_${MIN}_${MAX}.log"
python bursts_index_list.py $1 $JI $MIN $MAX 2> $1.index_list_${JI}_${MIN}_${MAX}.log &
echo "LOG = $1.index_list_${JI}_${MIN}_borders.log"
python bursts_index_list_border_run.py $1 $JI $MIN 2> $1.index_list_${JI}_${MIN}_borders.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

wait
echo "DONE."

