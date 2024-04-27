"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
# Constants
from Food_utilities import calories_by_origin, read_foods, Food

with open("foods.txt", "r") as file:
    foods = read_foods(file)

origin = 2
calories = calories_by_origin(foods, origin)

print(f"Average Calories for {Food.ORIGIN[origin]}: {calories}")