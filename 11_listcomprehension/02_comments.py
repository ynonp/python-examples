"""
Show commnet line count
from file /etc/shells
"""

with open("/etc/shells", "r") as f:
    comments = [line for line in f if line[0] == '#']

    print len(comments)
