"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-02-14"
-------------------------------------------------------
"""
# Imports
# Constants
from List_linked import List

lst = List()

#prepend
lst.prepend("2")
lst.prepend("1")

#append
lst.append("4")
lst.append('5')

#insert
lst.insert(2,"3")

#print
current = lst._front
while current is not None:
    print(current._value)
    current = current._next
