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
# Constants\
from Queue_array import Queue

queue = Queue()
queue.insert(10)
queue.insert(20)
queue.insert(30)

while not queue.is_empty():
    removed_value = queue.remove()
    print("Removed from the front of the queue:", removed_value)
    
queue.insert(99)
peeked_value = queue.peek()
print("Peeked at the front of the queue:", peeked_value)
    

