#Use Python 3 to run script
import bs4, requests, os, sys

url = 'http://xkcd.com/'
home = 'http:'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)

	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find an image.')
	else:
		comicUrl = home + comicElem[0].get('src')

		if os.path.exists(os.path.join('xkcd', os.path.basename(comicUrl))):
			print("Repository up to date.")
			sys.exit() 

		print('Downloading image %s...' % (comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()

		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
