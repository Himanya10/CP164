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

previous, current, index = lst._linear_search("2")

if current is not None:
    print(f"Found element '{current._value}' ar index {index}")
else:
    print("Element not found in the list")