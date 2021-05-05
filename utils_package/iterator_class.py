import cv2
import csv

class FileIter:
    def __init__(self, filename):
        file = open(filename)
        self.reader = file.read()

    def __iter__(self):
        return self

    def __next__(self):
        yield self.reader