#!/bin/bash		
#This simple script should create an empty C++ file that uses the OpenCV library #
#Name of the file will vary by the name input					 #
#ncount is the name check counter						 #
#fcount is the file check counter						 #
#I'm sure theres more elegant ways to do this					 #
#Also I refuse to let this script delete any file				 #
#				Created By: Asim Shamim				 #
#					Friday, March 04 2016			 #
##################################################################################

let ncount=0
let fcount=0
while [ $ncount -eq "0" ]
do
	while [ $fcount -lt 1 ]
	do
		read -p "Please enter the name of the file you want to create: " filename
		if [ -f "$filename" ]
		then
			echo "File already exists! Enter a new name."
			let fcount=0
		else
			let fcount=2
		fi
	done
	read -p "Are you sure you want your file to be called $filename? [Y/n]: " conf
	if [ "$conf" == "Y" ]
	then
		let ncount=1
	else
		let fcount=0
		let ncount=0
	fi
done
# Replaces file extension if added

file=${filename%%.*}
echo "Replaced file extension"
cat <<- "EOF" > $file.cpp
	#include <cstdio.h>
	#include <iostream>
	#include <opencv2/opencv.hpp>

	using namespace cv;

	int main( int argc, char **argv ) {
		/*Your Code Here*/
		return 0;
	}
EOF
echo "Done."
