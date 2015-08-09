import os
import unittest
import tempfile
import shutil

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


class TestFS(unittest.TestCase):
    
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        print "Created dir: " , self.dir

    def tearDown(self):
        shutil.rmtree(self.dir)
        print "Deleted dir: ", self.dir

    def test_rename(self):
        f = File(self.dir + '/test.txt')
        f.create()

        f.rename(self.dir + '/test2.txt')

        self.assertFalse(os.path.isfile(self.dir + '/test.txt'))
        self.assertTrue(os.path.isfile(self.dir + '/test2.txt'))


unittest.main()



















