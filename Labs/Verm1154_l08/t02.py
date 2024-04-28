"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-04"
-------------------------------------------------------
"""
# Imports
# Constants
from morse import ByCode

# eq testing code
code_a = ByCode('.-', 'A')
code_b = ByCode('-...', 'B')
code_c = ByCode('-.-.', 'C')

# lt testing code
print(f"Code for A: {str(code_a)}")
print(f"Code for B: {str(code_b)}")
print(f"Code for C: {str(code_c)}")

# le testing code
print(f"Is the Code for A equal to the Code for B? {'True' if code_a == code_b else 'False'}")
print(f"Does the Code for A come before the Code for B? {'True' if code_a < code_b else 'False'}")
print(f"Is the Code for A less than or equal to the Code for C? {'True' if code_a <= code_c else 'False'}")
