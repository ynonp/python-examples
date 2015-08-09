"""
Reusing code between classes with inheritance

1. Define a base class
2. Use super
"""

import os

class FSThing(object):
    def __init__(self, path):
        self.path = path

    def rename(self, newname):
        os.rename(self.path, newname)
        self.path = newname


class File(FSThing):
    def create(self):
        open(self.path, 'a').close()

class Dir(FSThing):
    def create(self):
        os.makedirs(self.path)


class PngImage(File):
    def __init__(self,path):
        if path.endswith('.png'):
            super(PngImage, self).__init__(path)
        else:
            super(PngImage, self).__init__(path + ".png")


p = PngImage("cat.png")
r = PngImage("dog")

p.create()
r.create()
