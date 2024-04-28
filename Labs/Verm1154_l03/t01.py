"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-23"
-------------------------------------------------------
"""
# Imports
# Constants
from Queue_array import Queue

queue = Queue()
values_to_insert = [22, 33, 11, 55, 44]

for value in values_to_insert:
    queue.insert(value)
    
print("Queue after insertions:", list(queue))
print("Current length of the queue:", len(queue))


