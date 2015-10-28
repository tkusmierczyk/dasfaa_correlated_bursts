#!/bin/sh

echo "The script reads bursts and correlates them using R-Trees index."

#verify arguments:
if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: BURSTS FILE"
    exit
fi

JI=0.975
MAX=1
echo "RUNNING 5-30, MAX=$MAX JI=$JI"

SET="5,6"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="7,8,9,10"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="11,12,13,14,15"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="16,17,18,19,20"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="21,22,23,24,25"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="26,27,28,29,30"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

wait
JI=0.975
MAX=2
echo "RUNNING 5-30, MAX=$MAX JI=$JI"

SET="5,6"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="7,8,9,10"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="11,12,13,14,15"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="16,17,18,19,20"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="21,22,23,24,25"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="26,27,28,29,30"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

wait
JI=0.9
MAX=1
echo "RUNNING 5-30, MAX=$MAX JI=$JI"

SET="5,6"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="7,8,9,10"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="11,12,13,14,15"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="16,17,18,19,20"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="21,22,23,24,25"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="26,27,28,29,30"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

wait
JI=0.9
MAX=2
echo "RUNNING 5-30, MAX=$MAX JI=$JI"

SET="5,6"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="7,8,9,10"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="11,12,13,14,15"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="16,17,18,19,20"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="21,22,23,24,25"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="26,27,28,29,30"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

wait
JI=0.975
MAX=3
echo "RUNNING 5-30, MAX=$MAX JI=$JI"

SET="5,6"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="7,8,9,10"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="11,12,13,14,15"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="16,17,18,19,20"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="21,22,23,24,25"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

SET="26,27,28,29,30"
echo "LOG = $1.index_rtrees_${JI}_${SET}_${MAX}.log"
python bursts_index_rtrees.py $1 $JI $SET $MAX 2> $1.index_rtrees_${JI}_${SET}_${MAX}.log &

wait
echo "DONE."

