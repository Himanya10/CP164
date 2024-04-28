"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
# Constants

from Stack_array import Stack
from utilities import stack_to_array

my_stack = Stack()
my_stack.push(11)
my_stack.push(22)
my_stack.push(33)
my_stack.push(44)
my_stack.push(55)

my_target = []
stack_to_array(my_stack, my_target)

print("Target list after transferring elements from the stack:", my_target)