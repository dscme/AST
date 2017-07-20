#!/usr/bin/env python

import os
import time

print('Auto Screen Shotter / Ebook Generator\nCreates a pdf from screenshots of an ebook\n\n')

pgs = input("Number of Pages: ")
name = raw_input("Name of Book: ").replace(" ", "");

print("Switch to the ebook App that can accept the right arrow key to move pages")

for i in range(10):
	print("Starting in {0} sec...".format(10-i))
	time.sleep(1)

print("Ready or not, here we gooooo")

os.system("mkdir ~/Desktop/{0}".format(name))

for i in range(pgs):
	# Send Arrow Key
	os.system('osascript -e "tell application \\"System Events\\" to key code 124"')

	# Take And Save Screenshot
	os.system('screencapture -x -t PDF -T 2 ~/Desktop/{0}/{0}_pg{1}.pdf'.format(name, i+1))

	print("Got Page {0}/{1}...".format(i+1, pgs))
	time.sleep(2)

# Put it all together
print('Joining all the pages...')

os.system('"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o ~/Desktop/{0}/{0}_ebook.pdf ~/Desktop/{0}/*.pdf'.format(name))

print("Donzos.\nEbook Saved in folder on desktop:\n~/Desktop/{0}/{0}_ebook.pdf".format(name))

if raw_input('Delete tmp files? (yes/no): ') in "YESYesyes":
        os.system('mv ~/Desktop/{0}/{0}_ebook.pdf ~/Desktop/{0}_ebook.pdf && rm -rf ~/Desktop/{0}'.format(name))


