import sys
import os

if len(sys.argv) != 3:
    print "Usage: %s <oldsuffix> <newsuffix>" % sys.argv[0]
    sys.exit(1)

(_, oldsuffix,newsuffix) = sys.argv

for name in os.listdir("."):
    if name.endswith(".%s" % oldsuffix):
        newname = name[:-3] + newsuffix
        print "Renaming %s => %s" % (name,newname)

        os.rename(name,newname)


