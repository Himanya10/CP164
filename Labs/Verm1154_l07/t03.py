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

l1 = List()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

even,odd= l1.split_alt_r()
for i in even:
    print(i)
print()
for i in odd:
    print(i)

