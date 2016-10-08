import os, sys, shutil

counter = 0
volume = 0
for filename in os.listdir("xkcd"):
	if counter%200 == 0:
		volume = volume + 1
		os.makedirs("xkcd_" + str(volume), exist_ok=True)

	shutil.copy2("xkcd/" + str(filename), "xkcd_" + str(volume) + "/" + str(filename))
	counter = counter + 1

print("Done.")
print(volume)

for i in range(1, volume+1):
	os.chdir("xkcd_" + str(i))
	pdf_name = "xkcd_" + str(i) + ".pdf"
	os.system("convert *.jpg *.gif *.png " + str(pdf_name))
	os.chdir("..")
	print(pdf_name + " is complete.")


