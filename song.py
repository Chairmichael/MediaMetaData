from mutagen.easyid3 import EasyID3
#print(EasyID3.valid_keys.keys())

class Song(object):
	def __init__(self):
		print('  ^^In Song __init__^^')
		#self.data = { }
		# Gets a list the supported EasyID3 keys
		keys = str(EasyID3.valid_keys.keys())[12:-3].split("', '")
		# Puts the supported keys into a dictionary with 'None' values
		self.data = {}.fromkeys(keys)
		print('  ^^Set self.data^^')

# Gets a substring between <a> and <b> 
# Mode: The tuple is if it should use rfind to find <a> and <b> respectively
def get_between(s, first, last, mode = (False, False)):
	if mode is (False, False): # Use find for both
		try:
			start = s.index(first) + len(first)
			end = s.index(last, i)
			return s[i:j]
		except ValueError:
			return ''
	if mode is (False, True): # Use rfind for last
		try:
			start = s.index(first) + len(first)
			end = s.rindex(last)
			return s[i:j]
		except ValueError:
			return ''
	if mode is (True, False): # Use rfind for first
		try:
			start = s.rindex(first) + len(first)
			end = s.index(last, i)
			return s[i:j]
		except ValueError:
			return ''
	if mode is (True, True): # Use rfind for both
		try:
			start = s.rindex(first) + len(first)
			end = s.rindex(last)
			return s[i:j]
		except ValueError:
			return ''