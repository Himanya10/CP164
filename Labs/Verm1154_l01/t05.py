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
from Food_utilities import read_foods
if __name__ == "__main__":
    with open("foods.txt", "r") as file:
        foods_list = read_foods(file)

    for food in foods_list:
        print(food)
