terminal-webcam
===============

a webcam that can be run on a bare terminal, please maximize your terminals!

setup
-----

Tested on Ubuntu 12.04

	sudo apt-get install python-opencv libncures5 

usage
-----
	
	python capture.py 
	python capture.py WIDTH_IN_CHARS

	# For colored version which may be slower, needs optimizing
	export TERM=xterm-256color && python color.py 70
