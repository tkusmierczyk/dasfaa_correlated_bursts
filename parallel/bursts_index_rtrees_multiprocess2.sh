#!/bin/sh

cd ../index
echo "The script reads bursts and correlates them using R-Trees index."
echo "[processes enitites with [36, 50] bursts]"

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
    echo "ARGUMENT NEEDED: MAX REPEATED POSITIONS (1,2,3...)"
    exit
fi
if [ -z "$4" ]
  then
    echo "ARGUMENT NEEDED: NUMPROCESSES PARALLEL"
    exit
fi


JI=$2
MAX=$3
NUMPROC=$4
echo "JI=$JI MAX=$MAX NUMPROC=$NUMPROC"

SET="36"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="37"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="38"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="39"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="40"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="41"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="42"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="43"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="44"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="45"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="46"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="47"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="48"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="49"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="50"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

wait

