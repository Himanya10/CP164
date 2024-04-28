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
# Constants

from List_array import List
from utilities import array_to_list, list_to_array

# Function to test array_to_list
source_list = [1, 2, 3, 4, 5]
llist = List()

print("Source List:")
print(source_list)

array_to_list(llist, source_list)

print("\nList after array_to_list:")
print(llist._values)  # Replace this line with your actual method to access the list contents

# Function to test list_to_array
source = List()
source.insert(0, 10)
source.insert(1, 20)
source.insert(2, 30)
source.insert(3, 40)
source.insert(4, 50)

print("\nOriginal List:")
print(source._values)  # Replace this line with your actual method to access the list contents

target_list = []
list_to_array(source, target_list)

print("\nTarget List after list_to_array:")
print(target_list)


