"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
# Constants
from functions import matrix_stats
test_matrix = [[3.5, 1.2, 4.8], [2.1, 5.7, 6.3], [8.2, 0.9, 2.4]]
small, large, total, average = matrix_stats(test_matrix)
print(f"Smallest: {small}, Largest: {large}, Total: {total}, Average: {average}")