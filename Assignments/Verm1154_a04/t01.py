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

from Queue_circular import Queue
q = Queue(3)
q.insert(1)
q.insert(2)
q.insert(3)

q2 = Queue(3)
q2.insert(1)
q2.insert(2)
q2.insert(3)

print(q == q2)
print(q.remove())
print(q.remove())
q.insert(5)
print(q.remove())
print(q.remove())
print(q2.peek())
