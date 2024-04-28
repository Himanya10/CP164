"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
# Constants
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()

array = [88, 23, 54, 13, 87, 999, 100, 5]

for i in array:
    a.insert_rear(i)

Sorts.gnome_sort(a)
array = []
for i in a:
    print(i)
