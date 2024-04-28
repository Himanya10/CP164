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
from Sorted_List_array import Sorted_List

from Food import Food
# Constants

# Process

# Create sortedlist and food

sl = Sorted_List()

print("__contains__ method test:")
food1 = Food("Lasagna",7,False,135)
food2 = Food("Butter Chicken",2,False,490)
food3 = Food("Moo Goo Guy Pan",1,False,272)

sl.insert(food1)
sl.insert(food2)

print(food1 in sl)  
print(food3 in sl)  
print()


# Test __eq__ method
print("__eq__ method test:")
sl2 = Sorted_List()
sl2.insert(food1)
sl2.insert(food2)

print(sl == sl2) 

print()

# for the getitem
print("__getitem__ method test:")
print(sl[0])  
print(sl[-1])
print()

# Clean
print("Cleaning test:")
sl.insert(food3)
sl.insert(food3)
sl.insert(food3)
sl.clean()
for food in sl:
    print(food)
    
print()


# Test count
print("count method test:")
print(sl.count(food3)) 
print(sl.count(food1))
print(sl.count(food2))  
print()

# Test find 
print("find method test:")
print(sl.find(food1))  
print(sl.find(food2))  
print(sl.find(food3))  
print()

# Test index 
print("index method test:")
print(sl.index(food1))  
print(sl.index(food2))  
print(sl.index(food3))  
print()

#  Test intersection 
print("intersection method test:")
sl2 = Sorted_List()
sl2.insert(food1)
sl2.insert(food3)
sl.intersection(sl, sl2)
for food in sl:
    print(food)
print()

# Test max 
print("max method test:")
print(sl.max())  
print()

# Test min 
print("min method test:")
print(sl.min())  
print()

# Test peek
print("peek method test:")
print(sl.peek())  
print()

# Test remove method
print("remove method test:")
sl.remove(food1)
for food in sl:
    print(food)
print()

# Test remove_front method
print("remove_front method test:")
sl.insert(food1)
sl.insert(food2)
sl.remove_front()
for food in sl:
    print(food)
print()

# Test remove_many method
print("remove_many method test:")
sl.insert(food3)
sl.insert(food3)
sl.remove_many(food3)
for food in sl:
    print(food)
print()

# Test split method
print("split method test:")
sl2 = Sorted_List()
sl2.insert(food1)
sl2.insert(food2)
sl2.insert(food3)
sl1, sl2 = sl2.split()
for food in sl1:
    print(food)
print()
for food in sl2:
    print(food)
print()

# Test split_alt method
print("split_alt method test:")
sl2 = Sorted_List()
sl2.insert(food1)
sl2.insert(food2)
sl2.insert(food3)
sl1, sl2 = sl2.split_alt()
for food in sl1:
    print(food)
print()
for food in sl2:
    print(food)
print()

# Test split_key method
print("split_key method test:")
sl2 = Sorted_List()
sl2.insert(food1)
sl2.insert(food2)
sl2.insert(food3)
sl1, sl2 = sl2.split_key(food2)
for food in sl1:
    print(food)
print()
for food in sl2:
    print(food)
print()

# Test union method
print("union method test:")
sl2 = Sorted_List()
sl2.insert(food1)
sl2.insert(food3)
sl.union(sl, sl2)
for food in sl:
    print(food)
print()

