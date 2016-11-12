import os, sys
from tkinter.filedialog import askdirectory

from song import Song
#from databuilder import Databuilder

def main():
	# Starting directory for reference
	starting_directory = os.getcwd()
	# Get directory for the files to change
	directory = askdirectory()
	# Take only .mp3 files
	file_names = [x for x in os.listdir() if x.endswith('.mp3')]


if __name__ == '__main__': main()