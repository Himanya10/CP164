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
from Food_utilities import food_table, read_foods

with open("foods.txt", "r") as file:
    foods = read_foods(file)
    
    food_table(foods)