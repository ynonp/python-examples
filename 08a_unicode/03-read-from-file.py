# -*- coding: utf-8 -*-

import codecs
import sys


with codecs.open('output.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sys.stdout.write(line)

