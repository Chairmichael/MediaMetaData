from song import get_between
from song import Song

class Mozart_Symphony(Song):
	def __init__(self, file_name, aid):
		super(Mozart_Symphony,self).__init__()
		self.file_name = file_name
		self.aid = aid
		# Use helper methods for readability
		self.nickname = self.__get_nickname()
		# Set some data
		self.data['genre'] = 'Classical'
		self.data['composer'] = 'Mozart, Wolfgang Amadeus'
		self.data['artist'] = 'Mozart, Wolfgang Amadeus'
		self.data['album'] = 'Mozart Symphonies'
		# Use some more helper methods for readability
		self.data['catalognumber'] = self.__get_catalog_number()
		self.data['tracknumber'] = self.__get_movement_number()
		self.data['discnumber'] = self.__get_symphony_number()

	# Helper method to get the nickname from the aid file
	def __get_nickname(self):
		if self.get_line_with(self.aid, 'K. ' + self.data['catalognumber'])
			name = get_between(line, '<br />"', '"')
			if len(name) < 15:
				self.nickname = '(%s)' % name

	# Helper method to get the kochel catalog number from the aid file
	def __get_catalog_number(self):
		return get_between(file_name, ' K ', ' ')

	# Helper method to get the symphony number
	def __get_symphony_number(self):
		with open(os.getcwd() + '\\symphonies.txt') as symphonies_data:
			for line in symphonies_data:
				i = line.find('K. ' + self.k_number)
				if i is not -1:


	# Helper method to get the movement number
	def __get_movement_number(self):
		return None


Mozart_Symphony('', '')