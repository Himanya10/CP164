"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
# Constants

from Food_utilities import read_foods, get_vegetarian

with open('foods.txt', 'r') as file:
    foods_list = read_foods(file)  
vegetarian_foods = get_vegetarian(foods_list)
for food in vegetarian_foods:
    print(food)