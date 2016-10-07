#Use Python 3 to run script
import bs4, requests, os, sys

url = "https://www.google.com/search?tbm=isch&q="

if len(sys.argv) >= 2:
	search_item = ' '.join(sys.argv[1:])
else:
	print("Invalid command")
	sys.exit()

url = url + search_item
os.makedirs(search_item, exist_ok= True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
images = soup.select("img")
print(images)

if images == []:
	print("No images found. Try different keywords.")
else:
	counter = 0
	for image in images:
		img_src = image.get('src')
		print("Dowlaoding image %s"% (img_src))

		image_req = requests.get(img_src)
		image_req.raise_for_status()

		image_file = open(os.path.join(search_item, str(counter)), 'wb')
		for chunk in image_req.iter_content(100000):
			image_file.write(chunk)
		image_file.close()

		counter = counter + 1

	print("Download complete.")


