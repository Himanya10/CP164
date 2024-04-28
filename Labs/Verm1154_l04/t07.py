"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
# Imports
# Constants
from utilities import list_test
from Food import Food

f1 = Food("not spring rolls",1,False,66)
f2 = Food("spring rolls wrong",2,True,653)
f3 = Food("good spring rolls",1,True,7)
source = [f1,f2,f3]
source2 = [6,8,2]
list_test(source)

