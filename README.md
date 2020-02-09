# Download songs from Youtube using terminal

This script just takes the song name as input and downloads the song in current working folder. Note that this script runs only in Python3. It wont work on python2. You can make it work on Python2 as well by making some minor changes. Send a pull request if you make the script Py2-3 compatible.

Steps to use the above program-

1. Download [youtube-dl](http://ytdl-org.github.io/youtube-dl/download.html) in your system. <br/>
  1 . 1. Using pip: ```sudo pip install --upgrade youtube_dl```<br/>
  1 . 2. Using Homebrew: ```brew install youtube-dl```<br/>
  
2. Download this script in any of your folder.

3. This is an optional step. If you want to be able to download songs from any of your working directories then do the following changes in .bash_profile<br/>
  3 . 1. Type ```vi ~/.bash_profile``` on your terminal.<br/>
  3 . 2. In the vi editor append the following line to the file. Save and close the file later.<br/>
    ```alias dy="python3 ~/path_where_you_have_stored_the_downloaded_python_script.py"```

4. Now you can type ```dy``` in any directory on the terminal. Now just enter the name of the song you want to Download. This will download the song in the current working directory.NOTE: The program might show an error after downloading, just ignore that message, your song would have been downloaded.

5. You can now play the song through terminal using ```open song_name.webm```
