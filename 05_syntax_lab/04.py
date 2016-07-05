"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""

text = ""

while True:
    line = raw_input()
    text = line + "\n" + text
    if len(line) == 0: break

print text

