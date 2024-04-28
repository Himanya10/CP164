"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports

# Constants

# pylint: disable=protected-access

from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(capacity)
        Use: target = Queue()  # uses default capacity
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        # make the capacity greater than 0
        assert capacity > 0, "Queue size must be > 0"

        #setting capacity equal to self._capacity
        self._capacity = capacity
        # setting self._values to None multiplied by the capacity of the stack
        self._values = [None] * self._capacity
        # setting self._front equal to None
        self._front = None   
        # setting self._rear to 0
        self._rear = 0       
        # setting self._count to 0
        self._count = 0      

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # if the stack is empty set self count to 0
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        # if stack is full then set the count to the capcity of the stack
        return self._count == self._capacity

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        #returning the length of the count
        return self._count

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        # setting the variable equals to True
        equals = True
        
        # if count is not equal to the length of the target
        if self._count != len(target):
            # set equals to False
            equals = False
        
        # for the index in the range of the length of the target 
        for i in range(len(target)):
            # if the values in the stack does not equal the target values 
            if self._values[(self._front+i) % self._capacity] != target._values[(target._front + i) % target._capacity]:
                # setting equals to False
                equals = False
        # return equals
        return equals

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # rear is somehthing 
        assert self._rear is not None, "Cannot add to a full queue"
        # in values check the rear and deepcopy its value 
        self._values[self._rear] = deepcopy(value)
        # find the modulus of rear and capacity 
        self._rear = (self._rear + 1) % self._capacity
        # adding one to count 
        self._count = self._count + 1
        
        # if front is equal to None
        if self._front == None:
            # set front equal to 0
            self._front = 0
        # reutrn None
        return None

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        # 
        assert self._front is not None, "Cannot remove from an empty queue"

        # your code here

        value = self._values[self._front]
        self._values[self._front] = None

        self._front = (self._front + 1) % self._capacity
        self._count = self._count - 1
        if self._count == 0:
            self._front = None

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        # your code here

        return self._values[self._front]

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._capacity


