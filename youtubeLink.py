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
print(f.renderText('Kaustubh\'s Downloader'))

API_KEY = "b5873c5ba6a1887af8f7314a78801b1"

def get_youtube_id(url1):
  candidate = url1.split("v=")[1]
  try:
    amp = candidate.index('&')
    answer = candidate.split('&')[0]
  except:
    answer = candidate
  return answer

import urllib.request
import re

search_keyword=input("Type the name of the song: ")
search_keyword = search_keyword.split()
search_keyword = "+".join(search_keyword)
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])
targetlink = "http://www.youtube.com/watch?v=" + video_ids[0]

cmd="youtube-dl -x --audio-format mp3 "+targetlink
os.system(cmd)
print("\n")

print(f.renderText('Download Complete'))

# print("*------------------------*")
# print("|   DOWNLOAD COMPLETE    |")
# print("*------------------------*")

print("\n")
