"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-15"
-------------------------------------------------------
"""
# Imports
# Constants
from Stack_array import Stack

stack = Stack()
values = [55, 44, 33, 22, 11]
for i in values:
    print(stack.is_empty())
    stack.push(i)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())

