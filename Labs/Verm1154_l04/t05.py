"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
# Imports
# Constantsx

from List_array import List 

# Create an instance of List with some initial values
source = List()

source.insert(0, 10)
source.insert(1, 20)
source.insert(2, 30)
source.insert(3, 40)
source.insert(4, 50)

# Display the original list
print("Original List:")
print(source._values)

# Test accessing elements at different indices
index_to_access = 2
try:
    value_at_index = source[index_to_access]
    print(f"\nValue at index {index_to_access}: {value_at_index}")
except AssertionError as e:
    print(f"Attempted to access an invalid index: {e}")
# Try accessing an invalid index (out of range)
invalid_index = 10
try:
    value_at_invalid_index = source[invalid_index]
    print(f"Value at index {invalid_index}: {value_at_invalid_index}")
except AssertionError as e:
    print(f"Attempted to access an invalid index: {e}")
except IndexError as e:
    print(f"IndexError: {e}")
    
# Test setting values at different indices
index_value_pairs = [(2, 35), (4, 55), (10, 100)]

for index, new_value in index_value_pairs:
    try:
        source[index] = new_value
        print(f"\nAfter setting value {new_value} at index {index}:")
        print(source._values)
    except (AssertionError, IndexError) as e:
        print(f"Attempted to set value at an invalid index: {e}")
    
    
    