import os, sys
from tkinter.filedialog import askdirectory
from mutagen.mp3 import EasyMP3 as MP3

current_symphony = (' ',' ')

class Symphony(object):
	def __init__(self, initial_name):
		# Define stuffs
		self.initial_name = initial_name
		self.genre = 'Classical'
		self.conductor = ''
		self.composer = ''
		self.album = ''
		self.artist = ''
		self.album_artist = ''
		self.k_number = ''
		self.disc_num = '' # Symphony number
		self.track_num = '' # Movement number
		self.nickname = '' # Ex. Great Symphony, Moonlight Sonata; mostly empty
		self.title = '' # Symphony No. X, Mov. Y (Nickname) - K. Z
		self.name_of_file = '' 
		self.tempo = ''
		self.key = ''


	def set_title(self, file_name): 
		# Symphony No. X, Mov. Y (Nickname) - K. Z
		t = 'Symphony No. %s, Mov. %s %s - K. %s'
		self.title = t % (self.disc_num, self.track_num, self.nickname, self.k_number)

	def set_k_number(self, file_name):
		i = file_name.find(' K ') + 3
		j = file_name.find(' ', i) 
		self.k_number = file_name[i:j]

	def set_disc_track_num(self):
		with open(starting_directory + 'symphonies.txt') as symphonies_data:
			for line in symphonies_data:
				i = line.find('K. ' + self.k_number)
				if i is not -1:
					s = line.find('Symphony No. ') + len('Symphony No. ') + 1
					t = line.find(' ', s + 1)
					self.disc_num = line[s:t]
					# Set track number
					current_symphony.insert(0, self.disc_num)
					current_symphony = current_symphony[:2]
					
					break

	def set_track_num(self):
		# Calculate using the initial disc number in the metadata


	def set_nickname(self):
		# Look at symphonies.txt for " after <br />, has to be less than 15 characters

	def set_composer(self):
		if 'Mozart' in self.initial_name:
			self.composer = 'Mozart, Wolfgang Amadeus'
		elif 'Beethoven' in self.initial_name:
			self.composer = 'Beethoven, Ludwig van'
		elif 'Chopin' in self.initial_name:
			self.composer = 'Chopin, Frédéric'
		else:
			self.composer = ''

#{ 	Dumb set methods
	def set_artist(self):
		self.artist = self.composer
	def set_album_artist(self):
		self.album_artist = self.artist
	def set_album(self):
		if 'Mozart' in self.composer: self.album = 'Mozart Symphonies'
	def set_conductor(self):
		if 'Mozart' in self.composer: self.conductor = 'Hogwood, Schroder'
#}

""" The Main method
"""
def main():
	starting_directory = os.getcwd()
	directory = askdirectory()
	os.chdir(directory)
	file_names = [x for x in os.listdir() if x.endswith('.mp3')]

	for file_name in file_names:
		sym = Symphony(file_name)
		sym.set_composer()
		sym.set_artist()
		sym.set_album_artist()
		sym.set_conductor()
		sym.set_k_number()
		sym.set_disc_track_num()
		sym.set_nickname()


	return 0


#call the "main" function if running this script
if __name__ == '__main__': main()

# for file in files:
# 	audio = MP3(file)
# 	title = ''.join(audio['title'])
# 	artist = ''.join(audio['artist'])
# 	composer = ''.join(audio['composer'])
# 	os.rename(file,'%s__%s__%s.mp3' % (composer, title, artist))
	
# audio = MP3('MozartPianoSong1.mp3')
# title = ''.join(audio['title'])
# artist = ''.join(audio['artist'])
# composer = ''.join(audio['composer'])
# for s in (title, artist, composer): print(s)

# os.rename('MozartPianoSong1.mp3','%s_%s_%s.mp3' % (composer, title, artist))
