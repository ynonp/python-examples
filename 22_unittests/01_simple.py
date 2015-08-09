"""
Unit Tests

1. Write a simple test
2. Test Files and Directories
"""

import unittest

class TestStuff(unittest.TestCase):

    def test_upper(self):
        name = 'ynon'
        self.assertEqual(name.upper(), 'YNON')

unittest.main()

