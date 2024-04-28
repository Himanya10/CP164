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

from Food_utilities import write_foods, read_foods


with open("foods.txt", "r") as foods:
    foods_list = read_foods(foods)
    with open("new_foods.txt", "x") as new_foods:
        write_foods(new_foods, foods_list)