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
from Hash_Set_sorted import Hash_Set
from functions import insert_words, comparison_total
# Constants
fv = open("otoos610.txt", "r", encoding = "utf-8")
hs = Hash_Set(20)


insert_words(fv,hs)

total, max_words = comparison_total(hs)

print("Using array-based Sorted List Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(max_words.word,max_words.comparisons))
