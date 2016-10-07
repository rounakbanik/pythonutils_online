#Use Python 3 to run script
import bs4, requests, os, sys

home = "http://sarahcandersen.com"
url = "http://sarahcandersen.com/"
os.makedirs("sarahscribbles", exist_ok=True)

while True:
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	checker = soup.select("article")

	image_list = soup.select("article img")
	#print(image_list)

	if image_list == []:
		print("Could not find an image.")
	else:
		image = image_list[0]
		img_src = image.get("src")

		image_req = requests.get(img_src)
		image_req.raise_for_status()
		print("Downloading image %s"% (img_src))

		image_file = open(os.path.join('sarahscribbles', os.path.basename(img_src)), 'wb')
		for chunk in image_req.iter_content(100000):
			image_file.write(chunk)
		image_file.close()

	url_list = soup.select("#pagination a")

	if len(url_list) == 2 and url != home + "/":
		print("Download Complete")
		sys.exit()

	url = home + url_list[0].get("href")
	print("URL: " + str(url))

print("Download complete.")
