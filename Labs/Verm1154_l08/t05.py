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

from BST_linked import BST
from morse import encode_morse,fill_letter_bst
bst = BST()
text = "My name is David Brown."
data1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))
fill_letter_bst(bst, data1)

code = encode_morse(bst, text)
print(f"English: {text}")
print(f"Morse Code: {code}")