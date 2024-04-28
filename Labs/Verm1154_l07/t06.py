"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
# Constants
from List_linked import List

l = List()
l.append(1)
l.append(2)
l.append(3)
for i in l:
    print(i)
l.reverse_r()
print()
for j in l:
    print(j)
print()
print(l._rear._value)
