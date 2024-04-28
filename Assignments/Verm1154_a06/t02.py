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

from Priority_Queue_linked import Priority_Queue

pq = Priority_Queue()


#Insert
pq.insert(3)
pq.insert(1)
pq.insert(4)
pq.insert(2)
# Peek
print("Highest priority: ")
print(pq.peek())
print()

# Remove
print("Remove element")
print(pq.remove())
print()

# len
print("Queue lenght: ")
print(pq.__len__())
print()

# Is empty
print("Is the queue empty")
print(pq.is_empty())
print()

# Split_key
pq1, pq2 = pq.split_key(3)

print(f"After splitting, pq1 is: {list(pq1)}, pq2 is: {list(pq2)}") 
print()

# Equal
print(f"Are pq1 and pq2 equal? {pq1 == pq2}")
