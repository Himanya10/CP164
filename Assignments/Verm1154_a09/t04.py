"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-24"
-------------------------------------------------------
"""

# Imports
from BST_linked import BST
# Constants
bst = BST()
# Process
# Insert some values
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

# Test __contains__
print(bst.__contains__(50))
print(bst.__contains__(100))

# Test node_counts
zero, one, two = bst.node_counts()
print(f"Zero-child nodes: {zero}, One-child nodes: {one}, Two-child nodes: {two}")

# Test parent (iterative)
print(bst.parent(20)) 
print(bst.parent(50))  

# Test parent_r (recursive)
print(bst.parent_r(20))  
print(bst.parent_r(50))  