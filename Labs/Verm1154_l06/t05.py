"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-02-15"
-------------------------------------------------------
"""
# Imports
# Constants
from List_linked import List
lst = List()

lst.append("1")
lst.append("2")
lst.append("3")
lst.append("4")

#peek
peek_value = lst.peek()
print(f"The first element in the list is {peek_value}")

#remove 
remove = lst.remove("2")
if remove is not None:
    print(f"Removed element '{remove}' from the list")
else:
    print("Element not found in the list")

current = lst._front
while current is not None:
    print(current._value)
    current = current._next
