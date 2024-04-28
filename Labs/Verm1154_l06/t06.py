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

#Get item
print(f"The first element in the list is {lst[0]}")
print(f"The last element in the list is {lst[-1]}")

#Set item
lst[1] = "5"
print(f"After setting, the second element in the list is {lst[1]}")