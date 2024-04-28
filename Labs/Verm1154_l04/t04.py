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

# Test inserting values
source.insert(0, 10)
source.insert(1, 20)
source.insert(2, 30)
source.insert(3, 40)
source.insert(4, 50)

# Display the original list
print("Original List:")
print(source._values)

# Test finding values
key_to_find = 30
found_value = source.find(key_to_find)

if found_value is not None:
    print(f"\nFound value for key '{key_to_find}': {found_value}")
else:
    print(f"\nKey '{key_to_find}' not found.")

# Test checking if values are in the list
value_to_check = 50
if value_to_check in source:
    print(f"\n{value_to_check} is in the list.")
else:
    print(f"\n{value_to_check} is not in the list.")
    
# Test counting occurrences of values
value_to_count = 30
occurrences = source.count(value_to_count)
print(f"\nNumber of occurrences of {value_to_count}: {occurrences}")

value_to_count = 60
occurrences = source.count(value_to_count)
print(f"Number of occurrences of {value_to_count}: {occurrences}")

# Test finding the maximum value
max_value = source.max()
print(f"\nMaximum value in the list: {max_value}")

# Test finding the minimum value
min_value = source.min()
print(f"\nMinimum value in the list: {min_value}")
