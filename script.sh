#!/bin/bash

while true; do
	echo "Sending file @ $(date)"
	rsync -e ssh ~/Pictures/wallhaven-146070.jpg babs:~/Pictures
	echo "Sent! @ $(date)"
	sleep 15
done
