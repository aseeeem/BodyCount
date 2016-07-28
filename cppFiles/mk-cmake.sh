#!/bin/bash
# This file should create a CMakeLists.txt file so I don't have to
# I'm really getting tired of doing it
# And isn't that how all great scripts start?
# -Asim Shamim
# Date Started: Sat Mar 12 17:08:39 EST 2016
# Date Completed: Sat Mar 12 17:54:54 EST 2016

let count=0
read -p "This will create a CMakeLists.txt file. Press [Enter] to continue..."

while [ $count -eq 0 ]
do
	if [ -f "CMakeLists.txt" ]
	then
		read -p "File already exists. Would you like to overwrite? [Y/n]: " conf
		if [ "$conf" == "n" ]
		then
			echo "Exiting..."
			exit
		elif [ "$conf" == "Y" ]
		then
			echo "Continuing with overwrite..."
			let count=1
		else
			echo "Please enter a valid response"
		fi
	else
		let count=1
	fi
done

read -p "Please enter in the name of your project: " projectName
read -p "Please enter in the name of your source file: " sourceFile

cat <<- EOF > CMakeLists.txt
	cmake_minimum_required( VERSION 2.8 )
	project( $projectName )
	find_package( OpenCV REQUIRED )
	add_executable( $projectName $sourceFile )
	target_link_libraries( $projectName ${OpenCV_LIBS} )
EOF
echo "Done."
