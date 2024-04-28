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

# Insert 
values_to_insert = [10, 5, 20, 15, 8]
for value in values_to_insert:
    pq.insert(value)

# Remove
removed_values = []
while len(pq._values) > 0:
    removed_value = pq.remove()
    removed_values.append(removed_value)

# Print the results
print("Priority Queue after removals:", pq._values)
print("Removed values:", removed_values)
    
    
