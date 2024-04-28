"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports

# Constants

from Priority_Queue_array import Priority_Queue
q = Priority_Queue()


q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

t1, t2 = (q.split_key(2))

print(list(t1), list(t2))
