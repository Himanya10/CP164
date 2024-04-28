"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
# Constants
from Food_utilities import read_foods
from functions import hash_table


file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)

hash_table(9, foods)