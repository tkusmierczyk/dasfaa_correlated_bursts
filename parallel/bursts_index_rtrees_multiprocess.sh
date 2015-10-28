#!/bin/sh

cd ../index
echo "The script reads bursts and correlates them using R-Trees index."
echo "[processes enitites with [1, 35] bursts]"

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


SET="1"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="2"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="3"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="4"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="5"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="6"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="7"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="8"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="9"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="10"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="11"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="12"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="13"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="14"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="15"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="16"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="17"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="18"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="19"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="20"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="21"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="22"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="23"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="24"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="25"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="26"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="27"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="28"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="29"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="30"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="31"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="32"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="33"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="34"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

SET="35"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

wait

