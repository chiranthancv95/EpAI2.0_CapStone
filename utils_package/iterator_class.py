'''
This is the custom iterator class file where the data is read from csv file using as a generator.
'''


import cv2
import csv


class FileIter:
	'''
	This custom iterator yields a generator object of the csv file given by user.
	'''
    def __init__(self, filename):
        file = open(filename)
        self.reader = file.read()

    def __iter__(self):
        return self

    def __next__(self):
        yield self.reader