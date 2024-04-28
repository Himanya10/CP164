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
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total
# Constants
fv = open("otoos610.txt", "r", encoding = "utf-8")
hs = Hash_Set(20)

# Process

insert_words(fv,hs)

total, max_words = comparison_total(hs)

print("Using array-based list Hash_Set")
print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{max_words.word}': {max_words.comparisons:,}")
