"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------



# Combine stacks
target = stack_combine(source1, source2)

# Print the target stack
while not target.is_empty():
    print(target.pop())
"""
# Imports
# Constants
from functions import stack_combine
from Stack_array import Stack


s1 = Stack()
s2 = Stack()


s1.push(8)
s1.push(12)
s1.push(8)
s1.push(5)

s2.push(14)
s2.push(9)
s2.push(7)
s2.push(1)
s2.push(6)
s2.push(3)
print(s1.peek(), s2.peek())
print()
print(stack_combine(s1, s2))
   


    