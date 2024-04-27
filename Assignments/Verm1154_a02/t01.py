"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
# Constants
from Food_utilities import by_origin, read_foods, Food

with open("foods.txt", "r") as file:
    foods = read_foods(file)

# change origin number from 1-11
origin = 2
o_foods = by_origin(foods, origin)

print(f"Foods with origin {Food.ORIGIN[origin]}:")
for food in o_foods:
    print(f"{food.name} - {Food.ORIGIN[food.origin]}")
