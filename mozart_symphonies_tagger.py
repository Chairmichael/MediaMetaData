import sys, os
from mutagen.easyid3 import EasyID3


# The file that will help tag some stuff
#aid_file = os.getcwd() + '\\symphonies.text'

def main():

	# Gets a list the supported EasyID3 keys
	keys = str(EasyID3.valid_keys.keys())[12:-3].split("', '")
	# Puts the supported keys into a dictionary with 'None' values
	tags = {}.fromkeys(keys)


	# Need to keep track of each file's name, to help tag the files correctly
	tags['file_name'] = '' 

	# Tags that apply to all files
	tags['genre'] = 'Classical'
	tags['artist'] = 'Mozart, Wolfgang Amadeus'
	tags['albumartist'] = 'Mozart, Wolfgang Amadeus'
	tags['composer'] = 'Mozart, Wolfgang Amadeus'
	tags['album'] = 'Mozart Symphonies - Hogwood, Schroder'
	tags['conductor'] = 'Hogwood, Schroder'
	# Tags that have different content for each file
	tags['discnumber'] = '' # Will be used for the symphony number
	tags['tracknumber'] = '' # Will be used for the movement number in regards to the specific symphony
	tags['catalognumber'] = '' # This is the "K" number, ie: K. 69
	tags['title'] = 'Symphony No. %s, Mov. %s (%s) - K. %s' # Symphony No. X, Mov. Y (Nickname) - K. Z
	tags['bpm'] = '' # The tempo of the piece

	# Change the working directory to the directory with the music
	os.chdir( os.getcwd() + '\\MozartSymphonies' )

	# Helper variable to help find the movement number
	what_symphony = [ '', '' ]

	# Gets a list of mp3 files from a directory
	file_names = [ x for x in os.listdir( os.getcwd() ) if x.endswith('.mp3') ]

	for file in file_names:
		# Set the file name
		tags['file_name'] = file
		print('File=%s' % file)

		# Get the catalog number from the file name
		tags['catalognumber'] = get_between( s = file, first = ' K ', last = 'isNaN')
		print( 'K. %s' % tags['catalognumber'] )

		# Find the Discnumber (Symphony) in the aid file using the 
		line = get_line_with( 'K. %s' % tags['catalognumber'] )
		print(line)
		tags['discnumber'] = get_between( s = line, first = 'Symphony No. ', last = 'isNaN' )

		#print( '%s == K.%s - Sym.%s' %  ( tags['file_name'], tags['catalognumber'], tags['discnumber'] ) )


	return 0

# Gets a substring between <a> and <b> 
# Mode: The tuple is if it should use rfind to find <first> and <last> respectively
def get_between( s, first, last):
	#print('*   s=%s, first=%s, last=%s' % (s, first, last))
	if last is not 'isNaN': 
		start = s.index(first) + len(first)
		end = s.index(last, start)
		return s[start : end]
	elif last is 'isNaN':
		start = s.index(first) + len(first)
		num = ''
		for x in s[start:]:
			if x.isdigit():
				num += x
			else:
				return num

# Returns a line from a file containing <s>
def get_line_with( s ):
	file_aid = 'symphonies.txt'
	with open(file_aid) as file:
		for line in file:
			# Find the line that has the s
			i = line.find(s)
			if i is not -1: # If right line...
				return line
		# If <s> is not in file
		print('')
		raise IndexError('Not in file')


main()