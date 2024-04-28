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

q1 = Queue()
q2 = Queue()

q1.insert(1)
q1.insert(2)
q1.insert(3)
q2.insert(1)
q2.insert(2)
q2.insert(3)

print(q1.__eq__(q2))
