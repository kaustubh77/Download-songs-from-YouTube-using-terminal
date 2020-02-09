from bs4 import BeautifulSoup
import os
import sys

import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input("Search the song you want to download: ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
targetlink = "http://www.youtube.com/watch?v=" + search_results[0]

cmd="youtube-dl -x --audio-format mp3 "+targetlink
os.system(cmd)
print("\n")

print("#######################")
print("   DOWNLOAD COMPLETE   ")
print("#######################")

print("\n")