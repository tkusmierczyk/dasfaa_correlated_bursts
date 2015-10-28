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


SET="30,31"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="32,33,34"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="35,36,37,38"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="39,40,41,42,43"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="44,45,46,47,48,49,50"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="51-60"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="61-75"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="76-100"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="101-140"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="141-200"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="201-250"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="251-300"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="301-350"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="351-400"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="401-500"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="501-600"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="601-700"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="701-800"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="801-900"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="901-1200"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="20-22"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="23-25"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="26-28"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="29"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="1,2,3"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="4,5,6"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="7,8,9"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="10,11,12,13"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

SET="14,15,16,17,18,19"
echo "LOG = $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log"
python bursts_index_rtrees_ld.py $1 $JI $SET $MAX $DIM 2> $1.index_rtrees_ld_${JI}_${SET}_${MAX}_${DIM}.log &
sh ../numprocesses_gate.sh $NUMPROC python

wait


