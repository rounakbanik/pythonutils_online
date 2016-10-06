import webbrowser

with open("list.txt") as f:
	for line in f:
		line = line.split()
		webbrowser.open(line[0])