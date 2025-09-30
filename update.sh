#!/bin/bash

try_to_update(){
	clear
	echo "Checking for updates..."
	sleep 0.3
	check_for_update=$(cat lxtoolkit.py | grep -i ReleaseVersion)
	if [[ $check_for_update == *"1.2" ]]; then
		clear
		touch .no_update_required.txt && echo "No update required. " > .no_update_required.txt
		echo "No update required. "
		exit
	else
		clear
		install_the_update=$(git clone https://github.com/luxe0x64/lxtoolkit.git)
		if [[ $install_the_update == *"100" ]]; then
			echo "Update installed. "
			exit
		else
			echo "Something went wrong. "
			exit
		fi
	fi

}

main(){
	try_to_update
}

main
