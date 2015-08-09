"""
Write code to make the following unit test pass
"""

import re

class InvalidImageExt(Exception): pass

class ImageFile(object):
    def __init__(self, fname):
        if re.search(r'([.]png|[.]jpe?g|[.]gif)$', fname):
            self.name = fname
        else:
            raise InvalidImageExt("Extension should be .png")

import unittest

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()


