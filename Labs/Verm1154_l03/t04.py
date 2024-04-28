"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# Imports
# Constants

from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

#Insert
values_to_insert = [10, 5, 20, 15, 8]
for value in values_to_insert:
    pq.insert(value)
    
#peek
highest_priority_value = pq.peek()

print("Priority Queue after insertions:", pq._values)
print("Peeked at the highest priority value:", highest_priority_value)