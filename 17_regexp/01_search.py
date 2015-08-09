"""
1. Search pattern in text
2. Extract data from text (using regexp)
3. Replace words using regexp
"""

import sys
import re

def istitle(text):
   return not re.search(r'\b[a-z]', text)

def get_key_value(text):
    m = re.search(r'(\w+)\s*=\s*(\w+)', text)
    if m is not None:
        print "[%s] => [%s] " % (m.group(1),  m.group(2))

while True:
    line = sys.stdin.readline()
    if line == '': break

    get_key_value(line)


