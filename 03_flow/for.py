"""
For loops demo
- Iterate over a sequence
- Iterate over numbers
"""

sentence = "Got two reasons why I cry"
words = sentence.split()

for word in words:
    print("The word is: ", word, "And its length:", len(word))

total = 0
for i in range(101):
    total += i

print("1 + 2 + 3 + 4 + ... + 100 = ", total)


