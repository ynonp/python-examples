"""
Writing to a textfile:
1. open the file as either "w" or "a"
   (write or append)

2. write the data
"""

with open("hello.txt", "w") as fout:
    fout.write("Hello World\n")

with open("/etc/shells", "r") as fin:
    with open("hello.txt", "a") as fout:
        for line in fin:
            fout.write(line)
