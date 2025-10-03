#!/bin/bash

# created by: luxe0x64
# For lxtoolkit
# Version is Alpha2

check_ff() {
	check=$(ls .a | grep ".no_update_required.txt")
	if [[ "$check" =~ ".no_update_required.txt" ]]; then
		echo "No updates required. "
	else
		try_to_update
	fi
}

try_to_update(){
	clear
	echo "Checking for updates..."
	sleep 0.3
	check_for_update=$(curl https://github.com/luxe0x64/lxtoolkit/blob/main/version.txt | grep "VERSION")
	if [[ "$check_for_update" =~ "Alpha2" ]]; then
		clear
		touch .no_update_required.txt && echo "No update required. " > .no_update_required.txt
		echo "No update required. "
		exit
	else
		clear
		install_the_update=$(git clone https://github.com/luxe0x64/lxtoolkit.git)
		if [[ "$install_the_update" =~ "100" ]]; then
			echo "Update installed. "
			exit
		else
			echo "Something went wrong. "
			exit
		fi
	fi

}

main(){
	check_ff
}

main
