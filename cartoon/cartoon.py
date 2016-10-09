#Use Python 3 to run script.
import bs4, requests, os, sys, time
from selenium import webdriver

home_url = "*************"
print("Enter the Series' URL: ")
#cartoon_url = "http://kisscartoon.me/Cartoon/Dexter-s-Laboratory-Season-01"
cartoon_url = input()
os.makedirs(os.path.basename(cartoon_url), exist_ok=True)

browser = webdriver.Firefox()
browser.get(cartoon_url)
time.sleep(8)
res = browser.page_source


soup = bs4.BeautifulSoup(res)
videos = soup.select("tr td a")

for video in videos:
	video_url = home_url + video.get("href")
	browser.get(video_url)
	time.sleep(5)
	video_url_source = browser.page_source
	video_soup = bs4.BeautifulSoup(video_url_source)

	vid = video_soup.select("video")
	vid_src = vid[0].get("src")

	print("Downloading from %s"% (vid_src))
	episode = requests.get(vid_src)
	episode.raise_for_status()

	epi_file = open(os.path.join(os.path.basename(cartoon_url), os.path.basename(video_url)), 'wb')
	for chunk in episode.iter_content(100000):
		epi_file.write(chunk)
	epi_file.close()
	print("Download of %s complete"%(os.path.basename(video_url)))

webdriver.quit()
print("COngratulations! The Series has been downloaded. Have fun!")