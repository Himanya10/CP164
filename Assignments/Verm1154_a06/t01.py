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
# Imports
from Queue_linked import Queue

q = Queue()

# Insert method
q.insert("A")
q.insert("B")
q.insert("C")

# Peek method
print(f"Check the first element in the queue: {q.peek()}")
print()

# Remove method
print(f"The removed element from queue is: {q.remove()}")
print()

# Len
print(f"The length of the queue is")
print(q.__len__())
print()

# is_empty
print("Is the queue empty")
print(q.is_empty())
print()

# is full
print("Is the queue full?")
print(q.is_full())
print()

source1 = Queue()
source2 = Queue()
source1.insert("E")
source1.insert("G")
source2.insert("F")
source2.insert("H")

# Combine
q.combine(source1, source2)
print(f"After combining, the queue is: {list(q)}")
print()

# Split_alt
source1, source2 = q.split_alt()
print(f"After splitting, source1 is: {list(source1)}, source2 is: {list(source2)}") 
print()

# If they're equal
print(f"Are source1 and source2 equal? {source1 == source2}") 


