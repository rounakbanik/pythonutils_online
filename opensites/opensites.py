#Opens a list of websites that you visit regularly
#Upload your list of frequently visited websites in 'list.txt'. Running the script will open all the websites in your default browser.

import webbrowser

with open("list.txt") as f:
	for line in f:
		line = line.split()
		webbrowser.open(line[0])