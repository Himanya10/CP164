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
from Hash_Set_array import Hash_Set


file = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(file)

hashset = Hash_Set(10)

for i in range(2):
    for val in foods:
        hashset.insert(val)

print(hashset.debug())
