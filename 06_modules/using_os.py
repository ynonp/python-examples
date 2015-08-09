"""
Using functions from module os.

1. os.walk
2. os.access
3. os.rename
4. os.listdir
"""
import os

for root,dirs,files in os.walk('/etc'):
    for name in files:
        if os.access(name, os.W_OK):
            print "File is writable: %s/%s" % (root,name)



# .txt => .old

for name in os.listdir("."):
    if name.endswith(".txt"):
        newname = name[:-3] + "old"
        print "Renaming %s => %s" % (name,newname)

        os.rename(name,newname)

