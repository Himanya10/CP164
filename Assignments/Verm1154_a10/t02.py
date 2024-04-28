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

from Sorts_List_linked import Sorts
from List_linked import List


a = List()

array = [12, 34, 41, 425, 63, 2739, 9999, 32, 1]

for i in array:
    a.append(i)
array = []

Sorts.radix_sort(a)

for i in a:
    print(i)

