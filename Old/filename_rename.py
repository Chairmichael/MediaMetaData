import os
from tkinter.filedialog import askdirectory
from mutagen.mp3 import EasyMP3 as MP3

directory = askdirectory()
os.chdir(directory)
files = [x for x in os.listdir() if x.endswith('.mp3')]
for file in files:
	audio = MP3(file)
	title = ''.join(audio['title'])
	artist = ''.join(audio['artist'])
	composer = ''.join(audio['composer'])
	os.rename(file,'%s__%s__%s.mp3' % (composer, title, artist))
	
'''
audio = MP3('MozartPianoSong1.mp3')
title = ''.join(audio['title'])
artist = ''.join(audio['artist'])
composer = ''.join(audio['composer'])
for s in (title, artist, composer): print(s)

os.rename('MozartPianoSong1.mp3','%s_%s_%s.mp3' % (composer, title, artist))
'''
