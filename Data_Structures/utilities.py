"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from List_array import List
from Food import Food
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
# Constants

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        stack.push(source.pop())
    return None

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        item = stack.pop()
        target.append(item)
    target.reverse()
    return None

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    my_stack = Stack()
    print(f"Is the stack empty? {my_stack.is_empty()}")
    array_to_stack(my_stack, source)
    my_stack.push(Food("Macaroni", 3, True, 1900))
    for i in my_stack:
        print(i)
    top_value = my_stack.peek()
    print(f"Top Stack Value: {top_value}")
    my_stack.pop()
    popped_value = my_stack.peek()
    print(f"New Top Stack Value: {popped_value}")
    print("Is the stack empty?:", my_stack.is_empty())
  
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in source:
        queue.insert(value)
    source.clear()

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        front_value = queue.remove()
        target.append(front_value)

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("Is queue empty:", q.is_empty())
    
    q.insert(10)
    print("Queue after inserting 10:", q.is_empty())
    
    q.insert(20)
    print("Queue after inserting 20:", list(q))
    
    front_value = q.peek()
    print("Front value of the queue:", front_value)

    # Test len on a non-empty queue
    queue_length = len(q)
    print("Length of the queue:", queue_length)

    # Test remove on a non-empty queue
    removed_value = q.remove()
    print("Removed value from the front of the queue:", removed_value)
    print("Queue after removal:", list(q))

    # Test is_empty on an empty queue after removal
    print("Is queue empty after removal:", q.is_empty())

    # Test remove on an empty queue (should raise an exception)
    try:
        removed_value = q.remove()
        print("Removed value from the front of the queue:", removed_value)
    except Exception as e:
        print(f"Error: {e}")

    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))
    return None

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return None 

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # Test is_empty on an empty priority queue
    is_empty_result = pq.is_empty()
    print("Is priority queue empty?", is_empty_result)

    # Test insert on a non-empty priority queue
    values_to_insert = [10, 5, 20, 15, 8]
    for value in values_to_insert:
        pq.insert(value)
    print("Priority Queue after insertions:", pq._values)

    # Test is_empty on a non-empty priority queue
    is_empty_result = pq.is_empty()
    print("Is priority queue empty?", is_empty_result)

    # Test peek on a non-empty priority queue
    peeked_value = pq.peek()
    print("Peeked at the highest priority value:", peeked_value)

    # Test remove on a non-empty priority queue
    removed_values = []
    while not pq.is_empty():
        removed_value = pq.remove()
        removed_values.append(removed_value)
    print("Priority Queue after removals:", pq._values)
    print("Removed values:", removed_values)

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        # Pop the last element from source and insert it at the front of llist
        llist.insert(0, source.pop())
        
def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.append(llist.remove_front())

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    print("the list should be empty",lst.is_empty())
    lst.append(source[0])
    print("is empty false now:",lst.is_empty())
    print()
    print("append and peek the value", lst.peek())
    print()
    lst.append(source[1])
    lst.insert(0,source[2])
    print("insert a food at index 0")
    print()
    for v in lst:
        print(v)
    print()
    print("What is the maximum food?",lst.max())
    print()
    print("What is the minimum food?",lst.min())
    print()
    key = Food("Spring rolls wrong", 2, True, 653)
    print("find any instances spring rolls wrong:")
    print("does it contain key?",key in lst)
    print("how many times?",lst.count(key))
    
    r = lst.remove(key)
    print("remove spring rolls wrong",r)
    print()
    lst[1] = Food("Chickie Nuggies",1,False,66)
    hmm = lst[0]
    print("update the list at index 1")
    print("the first variable in the list is",hmm)
    for v in lst:
        print(v)
    n = lst.index(Food("Chickie Nuggies",1,False,66))
    print("the index Chickie Nuggies is",n)
    print()
    print("finding chickie nuggies...")
    print(lst.find(Food("Chickie Nuggies",1,False,66)))
    
    return

    
