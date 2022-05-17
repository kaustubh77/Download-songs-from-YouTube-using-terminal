import os
import sys

import urllib.request
import re
from bs4 import BeautifulSoup
import os
import sys

import urllib.request
import urllib.parse
import re
import requests
import json

def download_song(name):
	# print(name)
	search_keyword=name
	search_keyword = search_keyword.split()
	search_keyword = "+".join(search_keyword)
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	# print("https://www.youtube.com/watch?v=" + video_ids[0])
	targetlink = "http://www.youtube.com/watch?v=" + video_ids[0]
	cmd="youtube-dl -x --audio-format mp3 "+targetlink
	os.system(cmd)
	print("Song downloaded: "+name)
	print("******")

file = sys.argv[1]
with open(file) as f:
	song_list = f.readlines()
for song in song_list:
	download_song(song)
	
