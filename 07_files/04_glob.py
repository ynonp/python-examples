"""
Glob example

glob.glob(...) returns a list of files/directories
matching a shell glob pattern
"""

import glob

files = glob.glob("*.txt")
print files


