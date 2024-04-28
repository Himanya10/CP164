"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-29"
-------------------------------------------------------
"""
# Imports
# Constants
from List_array import List 

source = List()

print("Original List:")
print(source._values)  

# Testing for Inserting
source.insert(2, 10)  
print("\nAfter inserting 10 at index 2:")
print(source._values)

source.insert(-1, 20)  
print("\nAfter inserting 20 at index -1 (appending):")
print(source._values)

source.insert(10, 30)  
print("\nAfter inserting 30 at index 10 (appending):")
print(source._values)


# Testing for Appending
source.append(10)
print("\nAfter appending 10:")
print(source._values)

source.append(20)
print("\nAfter appending 20:")
print(source._values)

source.append(30)
print("\nAfter appending 30:")
print(source._values)


#Testing for removing 
value_removed = source.remove(30)
if value_removed is not None:
    print(f"\nValue {value_removed} removed:")
    print(source._values)
else:
    print("\nKey not found.")

value_removed = source.remove(60)
if value_removed is not None:
    print(f"\nValue {value_removed} removed:")
    print(source._values)
else:
    print("\nKey not found.")