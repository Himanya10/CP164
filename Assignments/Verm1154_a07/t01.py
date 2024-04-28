"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
# Constants
from List_linked import List

class Food:
    def __init__(self, name, origin, is_vegetarian, calories):
        self.name = name
        self.origin = origin
        self.is_vegetarian = is_vegetarian
        self.calories = calories

    def __eq__(self, other):
        return (isinstance(other, Food) and 
                self.name == other.name and 
                self.origin == other.origin and 
                self.is_vegetarian == other.is_vegetarian and 
                self.calories == other.calories)

# Function to print test results
def print_test_result(test_name, result):
    print(f"Test {test_name}: {'Passed' if result else 'Failed'}")

# Read Food objects from 'food.txt' file
foods_from_file = []
with open('foods.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        food = Food(data[0], data[1], data[2] == 'True', int(data[3]))
        foods_from_file.append(food)

# Test the List_linked module methods

# Test __eq__ method
lst1 = List(foods_from_file.copy())
lst2 = List(foods_from_file.copy())
print_test_result('__eq__', lst1 == lst2)

# Add more tests for other methods as needed...

# Test append method
new_food = Food('Orange', 'Spain', True, 60)
lst1.append(new_food)
print_test_result('append', lst1[-1] == new_food)

# Example: Test __eq__ method after append
lst2.append(new_food)
print_test_result('__eq__ after append', lst1 == lst2)

# Continue testing other methods...

# Save test results to 'testing.txt'
with open('testing.txt', 'w') as test_file:
    test_file.write("Test Results:\n")
    test_file.write(f"__eq__: {'Passed' if lst1 == lst2 else 'Failed'}\n")
    # Add more test results...

print("Testing completed. Results saved to 'testing.txt'")


