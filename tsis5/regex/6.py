# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

kxkx = input()

signs = [' ', ',', '.']

for i in signs:
    s = s.replace(i, ':')

print(s)