from song import get_between
from song import Song

class Mozart_Symphony(Song):
	def __init__(self, file_name):
		super(Mozart_Symphony,self).__init__()
		self.data['genre'] = 'Classical'
		print(self.data['genre'])


Mozart_Symphony('')