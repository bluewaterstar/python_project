# encoding: utf-8
"""
@file: movie_to_mp3.py
@version: 1.0
@author: Atlantis
@time: 2021/10/26 18:25
@DESC: 
"""

#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 提取视频中的音频
# pip install moviepy
from moviepy.editor import AudioFileClip

input_file = "C:/Users/Blue water star/Downloads/Video/8.flv"

audio = AudioFileClip(input_file)
# audio.write_audiofile("D:/test1.wav") #提取的是无损文件,很大，比视频还大
audio.write_audiofile("D:/test.mp3")  #提取的是有损文件

