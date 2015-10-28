#!/bin/sh

cd ../index/
echo "The script reads bursts and correlates them (naive approach)."
echo "[processes enitites with 1-1200 bursts]"

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
echo "JI=$JI NUMPROC=$NUMPROC"


MIN="1"
MAX="1"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="2"
MAX="2"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="3"
MAX="3"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="4"
MAX="4"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="5"
MAX="5"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="6"
MAX="6"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="7"
MAX="7"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="8"
MAX="8"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="9"
MAX="9"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="10"
MAX="10"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="11"
MAX="13"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="14"
MAX="17"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="18"
MAX="22"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="23"
MAX="28"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="29"
MAX="35"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="36"
MAX="45"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="46"
MAX="60"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="61"
MAX="80"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="81"
MAX="120"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="121"
MAX="160"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="161"
MAX="200"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="201"
MAX="250"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="251"
MAX="300"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="301"
MAX="400"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="401"
MAX="600"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="601"
MAX="800"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="801"
MAX="1000"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

MIN="1001"
MAX="1200"
echo "LOG = $1.noindex_${JI}_${MIN}_${MAX}.log"
python bursts_noindex.py $1 $JI $MIN $MAX 2> $1.noindex_${JI}_${MIN}_${MAX}.log &
sh ../parallel/numprocesses_gate.sh $NUMPROC python

wait

