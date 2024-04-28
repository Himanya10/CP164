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
from functions import letter_table, do_comparisons, comparison_total
from Letter import Letter
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"


bst2 = BST()


for a in DATA2:
    letter = Letter(a)
    bst2.insert(letter)

file = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(file, bst2)
total = comparison_total(bst2)


letter_table(bst2)


