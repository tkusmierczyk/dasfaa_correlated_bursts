#!/bin/sh

echo "The script reads bursts and correlates them using R-Trees index."

#verify arguments:
if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=1.0
MAX=1
echo "RUNNING 1-5, MAX=$MAX JI=$JI"

SET="1"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="2"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="3"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="4"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="5"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &


wait
MAX=2
echo "RUNNING 1-5, MAX=$MAX JI=$JI"

SET="1"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="2"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="3"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="4"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="5"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &


wait
MAX=3
echo "RUNNING 1-5, MAX=$MAX JI=$JI"

SET="1"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="2"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="3"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="4"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="5"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &


wait
echo "DONE."

