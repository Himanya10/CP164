"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  
XRANGE = 1000  
TESTS = 100 

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(SIZE):
        number = Number(i)
        values.append(number)
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    i = SIZE
    values = List()
    while i != 0:
        i -= 1
        number = Number(i)
        values.append(number)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = List()

    for i in range(SIZE):

        col = List()
        for j in range(TESTS):
            a = random.randint(0, XRANGE)
            number = Number(a)
            col.append(number)
        lists.append(col)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    Number.comparisons = 0
    Sorts.swaps = 0

    sorted = create_sorted()
    reversed = create_reversed()
    rand = create_randoms()

    func(sorted)
    comps1 = Number.comparisons
    swaps1 = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0

    func(reversed)
    comps2 = Number.comparisons
    swaps2 = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0

    for i in rand:
        func(i)
    comps3 = Number.comparisons // TESTS
    swaps3 = Sorts.swaps // TESTS
    Number.comparisons = 0
    Sorts.swaps = 0

    print("{:14} {:8} {:8} {:8} {:8} {:8} {:8}".format(
        title, comps1, comps2, comps3, swaps1, swaps2, swaps3))

    return
