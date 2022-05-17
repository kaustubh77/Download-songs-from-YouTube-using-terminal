import urllib.request
import re

search_keyword=input("Type the name of the song: ")
search_keyword = search_keyword.split()
search_keyword = "+".join(search_keyword)
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])
