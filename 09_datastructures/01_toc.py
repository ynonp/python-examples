"""
1. Tuples
2. Lists
3. Dictionaries
4. Sets
5. Default dict
"""

email = {
    "bob" : "bob@gmail.com",
    "jane" : "jane@walla.co.il",
}

for (key, value) in email.items():
    print "%s => %s" % (key, value)

print email["bill"]

