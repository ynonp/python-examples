"""
Replace words using regexp

re.sub(regexp, replacement, text)
returns text with regexp replaced by replacement

re.sub(regexp, lambda, text)
returns text with regexp replaced by result of lambda
"""

import re
text = "baby let me     follow you down"


print re.sub(r'\s+',' ', text)

print re.sub(r'\b([a-z])', lambda m: m.group(1).upper(), text)


