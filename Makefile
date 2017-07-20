# Simple Make to Run Commands from Directory

.PHONY:	update AutoST

AutoST: AutoScreenShotter.py
	sudo python AutoScreenShotter.py

update:
	git pull origin testing



