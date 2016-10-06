#A Simple Mutliuser clipboard.

import shelve
import pyperclip
import sys

clipboard_shelf = shelve.open('clipboard')

if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'delete':
		if sys.argv[2] in clipboard_shelf:
			del clipboard_shelf[sys.argv[2]]
			print str(sys.argv[2]) + " has been deleted."
		else:
			print "The given keyword doesn't exist!"
	elif sys.argv[1].lower() == 'save':
		clipboard_shelf[sys.argv[2].lower()] = pyperclip.paste()
		print str(sys.argv[2]) + " has been added to yor multiclipboard."
	else:
		print "Invalid command."

elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		print "List of keywords: " + str(list(clipboard_shelf.keys()))
	elif sys.argv[1].lower() in clipboard_shelf:
		pyperclip.copy(clipboard_shelf[sys.argv[1]])
	else:
		print "Keyword does not exist."

else:
	print "Invalid command."



