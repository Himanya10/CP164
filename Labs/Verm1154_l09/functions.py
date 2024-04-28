"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports
# Constants
from Food import Food

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """

    print(f"Hash     Slot Key")
    print("-------- ---- --------------------")
    for value in values:
        hashVal = hash(value)
        slot = hashVal % 7
        key = value.key()
        print(f"{hashVal}     {slot} {key}")
    return None

