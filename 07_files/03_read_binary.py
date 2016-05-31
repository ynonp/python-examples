"""
Reading from a binary file

Use f.read(bufsize) to read a buffer
"""

bufsize = 20

import binascii

with open("/bin/ls", "rb") as fin:
    buf = fin.read(bufsize)
#
# can also use: buf != bytes()
    while buf != b"":
        print(binascii.hexlify(buf))
        buf = fin.read(bufsize)




