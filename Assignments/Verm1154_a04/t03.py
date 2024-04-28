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

from Queue_array import Queue
from functions import queue_split_alt


q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)


t1, t2 = queue_split_alt(q)
print(list(t1))
print(list(t2))
