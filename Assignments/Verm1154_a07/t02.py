"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# testing_sorted_list.py

from Sorted_List_linked import Sorted_List  # Replace with your module name
from Food import Food  # Replace with your Food class import statement

def load_food_data(file_name):
    """
    Load food data from a file.
    """
    foods = []
    with open(file_name, 'r') as file:
        for line in file:
            food = line.strip().split(',')
            food = Food(food[0], food[1], food[2] == 'True', int(food[3]))
            foods.append(food)
    return foods

# Load food data from file
food_data = load_food_data('foods.txt')

# Create a Sorted_List and add food objects
sorted_list = Sorted_List()
for food in food_data:
    sorted_list.insert(food)

# Test methods
print(f"List: {sorted_list}")
print(f"Count: {sorted_list.count()}")
print(f"Max: {sorted_list.max()}")
print(f"Min: {sorted_list.min()}")
print(f"Index of 'Banana': {sorted_list.index(Food('Banana'))}")
print(f"Contains 'Apple': {'Apple' in sorted_list}")
print(f"Peek: {sorted_list.peek()}")
print(f"Remove 'Banana': {sorted_list.remove(Food('Banana'))}")
print(f"List after removal: {sorted_list}")




