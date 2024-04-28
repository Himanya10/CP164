"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
# Constants

from Deque_linked import Deque

d = Deque()

d.insert_front(1)
d.insert_rear(2)

# peek
print(d.peek_front())
print(d.peek_rear())
print()

# remove
print("Remove front: ")
print(d.remove_front())
print("Remove rear: ")
print(d.remove_rear())
print()
# is empty
print("Is the queue empty: ")
print(d.is_empty())
print()

# _len_
print("Length: ")
print(d.__len__())
print()

# eq
other = Deque()
print("IS both queue equal: ")
print(d == other)
print()


# insert with the other value, for the future method
d.insert_front(1)
d.insert_rear(2)
other.insert_front(1)
other.insert_rear(2)

# test for the eq
print("Equal:", d == other)
print() 

# Iter
print("Values in Deque:")
for value in d:
    print(value)
    
print()
    

# swap:
d._swap(d._front, d._rear)

print("Front after swap: ", d.peek_front())
print("Rear after swap: ", d.peek_rear())
    
    
    
    
