"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Food import Food
# Constants
food_list = List()

# Process

# test for the append
food_list.append(Food("Moo Goo Guy Pan", 1, False, 272))
food_list.append(Food("Shark Fin Soup", 1, False, 46))

print("Appended Foods: ")
for food in food_list:
    print(food)
    
print()
    
    
# test for the clean 
food_list.clean()
print("Cleaned foods: ")
for food in food_list:
    print(food)

print()
    
# Combine method
food_list_1 = List()
food_list_1.append(Food("Moo Goo Guy Pan", 1, False, 272))
food_list_1.append(Food("Shark Fin Soup", 1, False, 46))

food_list_2 = List()
food_list_2.append(Food("BBQ Pork",1,False,920))
food_list_2.append(Food("Orange Chicken",1, False, 800))

food_list.combine(food_list_1, food_list_2)

print("Combined Foods: ")
for food in food_list:
    print(food)
    
print()
    
    
    
# Intersection method
food_list_1 = List()
food_list_1.append(Food("Moo Goo Guy Pan", 1, False, 272))
food_list_1.append(Food("Shark Fin Soup", 1, False, 46))

food_list_2 = List()
food_list_2.append(Food("BBQ Pork",1,False,920))
food_list_2.append(Food("Moo Goo Guy Pan", 1, False, 272))
food_list.intersection(food_list_1, food_list_2)

print("Intersection of foods: ")
for food in food_list:
    print(food)
    
print()
    
    
# Prepend method
food_list.prepend(Food("Spring Rolls", 1, True, 200))
print("Prepended foods: ")

for food in food_list:
    print(food)
    
print()
# Remove front
removed_food = food_list.remove_front()
print("Removed front food:")
print(removed_food)
print()

# Remove many 
food_to_remove = Food("Moo Goo Guy Pan", 1, False, 272)
food_list.remove_many(food_to_remove)
print("Removed foods: ")
for food in food_list:
    print(food)
    
print()
    
# For the split
food_list_1, food_list_2 = food_list.split()
print("Split list 1:")
for food in food_list_1:
    print(food)
print("Split list 2:")
for food in food_list_2:
    print(food)
    
print()
# For the split-alt
food_list_1, food_list_2 = food_list.split_alt()
print("Split alt list 1:")
for food in food_list_1:
    print(food)
print("Split alt list 2:")
for food in food_list_2:
    print(food)

print()

# Union
food_list_1 = List()
food_list_1.append(Food("Moo Goo Guy Pan", 1, False, 272))
food_list_1.append(Food("Shark Fin Soup", 1, False, 46))

food_list_2 = List()
food_list_2.append(Food("BBQ Pork",1,False,920))
food_list_2.append(Food("Orange Chicken",1, False, 800))
food_list.union(food_list_1, food_list_2)

print("Union for food:")
for food in food_list:
    print(food)



