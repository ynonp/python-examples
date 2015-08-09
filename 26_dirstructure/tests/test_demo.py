import unittest

import lib.demo as demo

class TestDemo(unittest.TestCase):

    def test_add(self):
        res = demo.add(10, 20)
        self.assertEqual(res, 30)
