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
from Food_utilities import food_search, read_foods, Food


with open("foods.txt", "r", encoding="utf-8") as file:
    lines = read_foods(file)
    

    origin = int(input("Origin country (1-11): "))
    max_cals = int(input("Maximum calories: "))
    is_veg = input("Vegetarian? (Yes/No): ").capitalize()
    is_veg = True if is_veg == 'Yes' else False



result = food_search(lines, origin, max_cals, is_veg)

print("{:<35} {:<12} {:<10} {:<8}".format("Food", "Origin", "Vegetarian", "Calories"))
print("{:<35} {:<12} {:<10} {:<8}".format("-"*35, "-"*12, "-"*10, "-"*8))

for results in result:
    
    print("{:<35} {:<12} {:<10} {:<8}".format(results.name, Food.ORIGIN[results.origin], str(bool(results.is_vegetarian)), results.calories))