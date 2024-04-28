"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
# Constants
from BST_linked import BST
from morse import decode_morse,fill_code_bst
bst = BST()
text = "... --- ..."
values = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))
fill_code_bst(bst, values)

english = decode_morse(bst, text)
print(f"Morse Code: {text}")
print(f"Morse Code: {english}")
