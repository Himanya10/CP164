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
from utilities import stack_test
from Food_utilities import read_foods

fh = open("foods.txt", "r")
food_list = read_foods(fh)
stack_test(food_list)
fh.close()