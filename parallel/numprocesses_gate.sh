#!/bin/bash

#THE SCRIPT WAITS UNTIL NUMBER OF PROCESSES IS BELOW A THRESHOLD

if [ -z "$1" ]
  then
    echo "ARGUMENT NEEDED: MIN NUMBER OF PROCESSES"
    exit
fi
if [ -z "$2" ]
  then
    echo "ARGUMENT NEEDED: PROCESS NAME"
    exit
fi

while :
do
    NUMPROC=`ps -A -u $USER | grep $2 | wc -l`
    if [ "$1" -gt "$NUMPROC" ];
    then
	    break       	   #Abandon the loop.
    fi
	sleep 1
done
DATE=`date`
#echo "[$DATE] PASSING NEXT"
