from bs4 import BeautifulSoup
import os
import sys

import urllib.request
import urllib.parse
import re
import requests
import json
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Kaustubh\'sDownloader'))

API_KEY = "b5873c5ba6a1887af8f7314a78801b1"

def get_youtube_id(url1):
  candidate = url1.split("v=")[1]
  try:
    amp = candidate.index('&')
    answer = candidate.split('&')[0]
  except:
    answer = candidate
  return answer

def get_lyrics(query_string):
	target_url = 'https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=jsonp&callback=callback&q_track=' + query_string + '&apikey=cb5873c5ba6a1887af8f7314a78801b1'
	request = requests.get(target_url)
	print(request.text)

search_query_input = input("Search the song you want to download: ")
query_string = urllib.parse.urlencode({"search_query" : search_query_input})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
targetlink = "http://www.youtube.com/watch?v=" + search_results[0]

cmd="youtube-dl -x --audio-format mp3 "+targetlink
os.system(cmd)
print("\n")

if sys.argv[-1] == 'lyrics':
	get_lyrics(search_query_input)


print("*------------------------*")
print("|   DOWNLOAD COMPLETE    |")
print("*------------------------*")

print("\n")