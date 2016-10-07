#Use Python 3 to run script
import bs4, requests, os, sys

url = "https://www.pexels.com/search/"

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
images = soup.select("article a img")

if images == []:
	print("No images found. Try different keywords.")
else:
	for image in images:
		img_src = image.get('src')
		print("Dowlaoding image %s"% (img_src))

		image_req = requests.get(img_src)
		image_req.raise_for_status()

		image_file = open(os.path.join(search_item, os.path.basename(img_src)), 'wb')
		for chunk in image_req.iter_content(100000):
			image_file.write(chunk)
		image_file.close()

	print("Download complete.")


