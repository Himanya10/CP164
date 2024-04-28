"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
# Imports
# Constants
from Stack_array import Stack
from utilities import array_to_stack

my_stack = Stack()
my_source = [1, 2, 3, 4, 5]
array_to_stack(my_stack, my_source)
print("Stack after transferring elements from the source list:", my_stack._values)


