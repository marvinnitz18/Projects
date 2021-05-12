#!/bin/bash


while :
do
	sleep 60
	if ping -c 1 1.1 &> /dev/null
		then
  			echo "connected" >> ./data
		else
  			date >> ./data
  			echo "not connected" >> ./data
	fi
done

