#!/usr/bin/env python
# coding: utf-8

#import pytube library to download the video
import pytube

#Ask for the url of video
url = input("Enter video url: ")
#we can take path as well, just uncomment the following line
#path = input("Enter path of storage")
 
#specify the starage path of video
path="Videos Descargados"

#magic line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)
