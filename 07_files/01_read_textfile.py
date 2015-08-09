
import sys

with open("/etc/shells", "r") as fin:
    for line in fin:
        sys.stdout.write(line)

# no need to close fin
#

