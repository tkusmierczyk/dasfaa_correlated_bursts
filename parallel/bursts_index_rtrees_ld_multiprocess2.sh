#!/bin/sh

echo "The script reads bursts and correlates them using Low dimensional R-Trees index."

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
    echo "ARGUMENT NEEDED: INDEX DIMENSIONALITY"
    exit
fi
if [ -z "$5" ]
  then
    echo "ARGUMENT NEEDED: NUMPROCESSES PARALLEL"
    exit
fi

JI=$2
MAX=$3
DIM=$4
NUMPROC=$5
echo "JI=$JI MAX=$MAX DIM=$DIM NUMPROC=$NUMPROC"


SET="5"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="6"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="7"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="8"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="9"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="10"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="11"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="12"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="13"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="14"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="15"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="16"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="17"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="18"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="19"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="20"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="21"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="22"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="23"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="24"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="25"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="26"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="27"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="28"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="29"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="30"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="31"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="32"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="33"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="34"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python


SET="35"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="36"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="37"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="38"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="39"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="40"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="41"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="42"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="43"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="44"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="45"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="46"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="47"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="48"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="49"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="50"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python




wait


