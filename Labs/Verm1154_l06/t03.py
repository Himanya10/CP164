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

lst.append(4)
lst.append(30)
lst.append(52)
lst.append(500)
lst.append(30)

#Max
max_value = lst.max()
print(f"The maximum value in the list is {max_value}")

#Min 
min_value = lst.min()
print(f"The minimum value in the list is {min_value}")

#Count
count = lst.count(20)
print(f"The number appears {count} times in the list")
