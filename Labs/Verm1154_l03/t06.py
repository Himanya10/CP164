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
from Food import Food

pq = Priority_Queue()
file_path = 'foods.txt'

with open(file_path, 'r') as file:
    for line in file:
        data = line.strip().split('|')
        name, calories, is_vegetarian, origin = data
        food = Food(name, int(calories), is_vegetarian == 'True', int(origin))
        
        pq.insert(food)
is_empty_result = pq.is_empty()
print("Is priority queue empty?", is_empty_result)

peeked_value = pq.peek()
print("Peeked at the highest priority value:", peeked_value)

removed_values = []
while not pq.is_empty():
    removed_value = pq.remove()
    removed_values.append(removed_value)
print("\nPriority Queue after removals:")
for food in removed_values:
    print(food)
