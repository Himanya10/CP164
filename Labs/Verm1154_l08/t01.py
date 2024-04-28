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
from morse import ByLetter

# eq testing code
by_letter1 = ByLetter('A', '.-')
by_letter2 = ByLetter('A', '.-')
by_letter3 = ByLetter('B', '-...')

assert by_letter1 == by_letter2, f"Equality test failed: {by_letter1} != {by_letter2}"
assert not by_letter1 == by_letter3, f"Equality test failed: {by_letter1} == {by_letter3}"

# lt testing code
by_letter1 = ByLetter('A', '.-')
by_letter2 = ByLetter('B', '-...')

assert by_letter1 < by_letter2, f"Less than test failed: {by_letter1} >= {by_letter2}"
assert not by_letter2 < by_letter1, f"Less than test failed: {by_letter2} < {by_letter1}"

# le testing code
by_letter1 = ByLetter('A', '.-')
by_letter2 = ByLetter('A', '.-')
by_letter3 = ByLetter('B', '-...')

assert by_letter1 <= by_letter2, f"Less than or equal test failed: {by_letter1} > {by_letter2}"
assert by_letter1 <= by_letter3, f"Less than or equal test failed: {by_letter1} > {by_letter3}"
assert not by_letter3 <= by_letter1, f"Less than or equal test failed: {by_letter3} <= {by_letter1}"

print("All tests passed!")



