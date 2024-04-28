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
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

#array to queue
print("Array to Queue:")
queue = Queue()
source_list = [1,2,3,4,5]

print("Inital state of the queue:", list(queue))
print("Inital state of the source list:", source_list)

array_to_queue(queue, source_list)
print("Final state of the queue:", list(queue))
print("Final state of the source list:", source_list)

# queue to array
print("\nQueue to Array:")
target_list = []
for i in range(1, 6):
    queue.insert(i)

print("Initial state of the queue:", list(queue))
print("Initial state of the target list:", target_list)

queue_to_array(queue, target_list)

print("Final state of the queue:", list(queue))
print("Final state of the target list:", target_list)

# Queue testing 
print("\nQueue testing")
a = [1, 2, 3, 4, 5]
queue_test(a)
    


