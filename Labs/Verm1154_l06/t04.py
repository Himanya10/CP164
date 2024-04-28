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

#count
contains = "2" in lst
print(f"Does the list contain 2? {contains}")

#index
index_2 = lst.index("2")
print(f"The index of '2' in the list is {index_2}")

#find
found_value = lst.find("2")
if found_value is not None:
    print(f"found element '{found_value}' in the list")
else:
    print("Element not found int he list")
