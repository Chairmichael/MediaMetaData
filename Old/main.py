import os, sys
from tkinter.filedialog import askdirectory
from mutagen.mp3 import EasyMP3 as MP3

a_symphony = (' ',' ')
starting_directory = os.getcwd()
directory = askdirectory()

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
		self.key = ''
		self.tempo = ''

	def set_title(self): 
		# Symphony No. X, Mov. Y (Nickname) - K. Z
		t = 'Symphony No. %s, Mov. %s %s - K. %s'
		print('$$$$ In set_title method $$$$')
		self.title = t % (self.disc_num, self.track_num, self.nickname, self.k_number)

	def set_k_number(self):
		print('$$$$ In set_k_number method $$$$')
		i = self.initial_name.find(' K ') + 3
		j = self.initial_name.find(' ', i) 
		self.k_number = self.initial_name[i:j]

	def set_disc_track_num(self):
		# Find disc number (symphony)
		print('$$$$ In set_disc_track_num method $$$$')
		with open(starting_directory + '\\symphonies.txt') as symphonies_data:
			for line in symphonies_data:
				i = line.find('K. ' + self.k_number)
				if i is not -1:
					s = line.find('Symphony No. ') + len('Symphony No. ')
					t = line.find(' ', s)
					self.disc_num = line[s:t]
		# Set track number (movement)
		a_symphony.insert(0, self.disc_num)
		a_symphony = a_symphony[:2]
		if a_symphony[0] is not a_symphony[1]: # If Symphony is not the same as the last one
			self.track_num = '1' # Set track number (movement) to 1
		else: # If we stay in the same movement
			self.track_num = str(int(self.track_num) + 1) # Increment track number (movement) by 1

	def set_nickname(self):
		# Look at symphonies.txt for " after <br />, has to be less than 15 characters
		print('$$$$ In set_nickname method $$$$')
		with open(starting_directory + '\\symphonies.txt') as symphonies_data:
			for line in symphonies_data:
				if line.find('<br />"') is not -1:
					i = line.find('<br />"') + line.find('<br />"')
					j = line.find('"', i)
					name = line[ i : j ]
					if len(name) < 15:
						self.nickname = '(%s)' % name

	def set_key(self):
		print('$$$$ In set_key method $$$$')
		with open(starting_directory + '\\symphonies.txt') as symphonies_data:
			for line in symphonies_data:
				i = line.find('K. ' + self.k_number)
				if i is not -1:
					s = line.find('Symphony No. ') + len('Symphony No. ')
					t = line.find(' ', s)
					sym_num = line[s:t]
					if sym_num is self.disc_num:
						i = line.find('||[[') + len('||[[')
						j = line.find(']]')
						self.key = line[j : i]

	def set_tempo(self):
		###
		return 0

	def set_composer(self):
		print('$$$$ In set_composer method $$$$')
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
		print('$$$$ In set_artist method $$$$')
		self.artist = self.composer
	def set_album_artist(self):
		print('$$$$ In set_album_artist method $$$$')
		self.album_artist = self.artist
	def set_album(self):
		print('$$$$ In set_album method $$$$')
		if 'Mozart' in self.composer: self.album = 'Mozart Symphonies'
	def set_conductor(self):
		print('$$$$ In set_conductor method $$$$')
		if 'Mozart' in self.composer: self.conductor = 'Hogwood, Schroder'
#}

""" The Main method
"""
def main():
	# starting_directory = os.getcwd()
	# directory = askdirectory()
	os.chdir(directory)
	file_names = [x for x in os.listdir() if x.endswith('.mp3')]

	for file_name in file_names:
		sym = Symphony(file_name)
		sym.set_composer()
		print(sym.composer)
		sym.set_artist()
		print(sym.artist)
		sym.set_album_artist()
		print(sym.album_artist)
		sym.set_conductor()
		print(sym.conductor)
		sym.set_k_number()
		print(sym.k_number)
		sym.set_disc_track_num()
		print(sym.disc_num)
		print(sym.track_num)
		sym.set_nickname()
		print(sym.nickname)
		sym.set_title()
		print(sym.title)
		sym.set_key()
		print(sym.key)
		sym.set_tempo()

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
