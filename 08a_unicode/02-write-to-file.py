# -*- coding: utf-8 -*-

import codecs

text = u"שלום לכולם"

with codecs.open('output.txt', 'w', encoding='utf-8') as f:
    for _ in range(10):    
        f.write(text)

