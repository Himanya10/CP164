"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
# Constants

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

file = open("miserables.txt", "r", encoding="utf-8")
for a in DATA1:
    letter = Letter(a)
    bst1.insert(letter)

for b in DATA2:
    letter = Letter(b)
    bst2.insert(letter)

for c in DATA3:
    letter = Letter(c)
    bst3.insert(letter)

do_comparisons(file, bst1)
print(comparison_total(bst1))
file = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(file, bst2)
print(comparison_total(bst2))
file = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(file, bst3)
print(comparison_total(bst3))
