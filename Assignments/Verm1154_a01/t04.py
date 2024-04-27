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
from functions import file_analyze
with open("t04_src.txt",'r') as file_var:
    upper_count, lower_count, digit_count, whitespace_count, remaining_count = file_analyze(file_var)
    
print("Uppercase Letters: ", upper_count)
print("Lowercase Letters: ", lower_count)
print("Digits", digit_count)
print("Whitespace Characters: ", whitespace_count)
print("Remaining Characters:", remaining_count)