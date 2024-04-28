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
l.append(3)


p,c,i = l._linear_search_r(3)
print("recursively there is a 3 found at index:",i)