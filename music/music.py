#Use Python 3 to run script.
from __future__ import unicode_literals
import bs4, requests, os, sys, time
import youtube_dl

if len(sys.argv) == 1:
	print("Invalid Command. Enter Search Terms.")
	sys.exit()

home_url = "https://www.youtube.com"

os.makedirs("Music", exist_ok=True)
search_term = ' '.join(sys.argv[1:])
url = "https://www.youtube.com/results?search_query=" + search_term

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

search_results = soup.select("h3 a")
video_title = search_results[0].get("title")
video_url = home_url + search_results[0].get("href")

print("Downloading audio from %s"%(video_url))

os.chdir("Music")
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Dowload Complete.")


