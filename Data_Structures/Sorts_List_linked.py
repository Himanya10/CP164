"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-04"
-------------------------------------------------------
"""
from List_linked import List


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  


    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Selection Sort algorithm.
        Finds maximum value each pass.
        Use: selection_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (List)
        Returns:
            None
        -------------------------------------------------------
        """

        unsorted = a._front
        a._front = None
     
        while unsorted is not None:
            max_prev = None
            max_node = unsorted
            prev = unsorted
            curr = max_node._next

            while curr is not None:
                if curr._value > max_node._value:
                    max_prev = prev
                    max_node = curr
                prev = curr
                curr = curr._next
            Sorts.swaps += 1

            if max_prev is None:
                unsorted = max_node._next
            else:
                max_prev._next = max_node._next
            if a._front is None:
                a._rear = max_node
            max_node._next = a._front
            a._front = max_node
        return

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Bubble Sort algorithm.
        Use: bubble_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        done = False
        last = None

        while not done:
            done = True
            prev = None
            curr = a._front
            swapped = a._front

            while curr is not last and curr._next is not None:

                if curr._value > curr._next._value:
                    done = False
                    Sorts.swaps += 1
                    a._swap(prev, curr)
                    swapped = curr
                    if prev is None:
                        prev = a._front
                    else:
                        prev = prev._next
                else:
                    prev = curr
                    curr = curr._next
            last = swapped
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an List using the Comb Sort algorithm.
        Use: comb_sort(a)
        -------------------------------------------------------
        Parameters:
          a - a linked list of comparable elements (?)
        Returns:
          None
        -------------------------------------------------------
        """
        n = len(a)

        if n > 0:
            gap = n
            done = False

            while gap > 1 or not done:
                done = True
                prev = None
                curr = a._front
                gap = int(gap / 1.3)

                if gap < 1:
                    gap = 1

                i = 0
                prev_far = curr
                far = curr._next
                while i < gap - 1 and far is not None:
                    prev_far = far
                    far = far._next
                    i += 1

                while curr is not None and far is not None:
                    if curr._value > far._value:
                        Sorts.swaps += 1
                        a._swap(prev, prev_far)
                        done = False
                    prev_far = far
                    far = far._next
                    prev = curr
                    curr = curr._next
        return

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Insertion Sort algorithm.
        Use: insertion_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        unsorted = a._front
        a._front = None

        while unsorted is not None:
            key_node = unsorted
            unsorted = unsorted._next
            prev = None
            curr = a._front

            while curr is not None and curr._value < key_node._value:
                prev = curr
                curr = curr._next
            Sorts.swaps += 1

            if prev is None:
                key_node._next = a._front
                a._front = key_node
            else:
                key_node._next = curr
                prev._next = key_node

            if key_node._next is None:
                a._rear = key_node
        return

    @staticmethod
    def merge_sort(a):
        if a._count >= 2:
            left, right = Sorts._merge_split(a)
            Sorts.merge_sort(left)
            Sorts.merge_sort(right)
            Sorts._merge(a, left, right)
        return

    @staticmethod
    def _merge_split(source):
        count = source._count // 2
        curr = source._front

        for _ in range(count - 1):
            curr = curr._next

        left = List()
        left._front = source._front
        left._rear = curr
        left._count = count
        right = List()
        right._front = curr._next
        right._rear = source._rear
        right._count = source._count - count
        left._rear._next = None
        source.clear()
        return left, right

    @staticmethod
    def _merge(target, left, right):
        while left._front is not None and right._front is not None:

            if left._front._value <= right._front._value:
                target._move_front_to_rear(left)
            else:
                target._move_front_to_rear(right)

        if left._front is not None:
            target._append_list(left)
        elif right._front is not None:
            target._append_list(right)
        return

    @staticmethod
    def to_array(a):
        """
        -------------------------------------------------------
        Copies list values to a Python list.
        Use: values = to_array(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            values - the contents of a in a Python list.= (list of ?)
        -------------------------------------------------------
        """
        values = []
        curr = a._front

        while curr is not None:
            values.append(curr._value)
            curr = curr._next
        return values

    @staticmethod
    def is_sorted(a):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            srtd - True if contents of a are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        curr = a._front

        while srtd and curr is not None and \
                curr._next is not None:

            if curr._value <= curr._next._value:
                curr = curr._next
            else:
                srtd = False
        return srtd

    @staticmethod
    def bucket_sort(a):
        if len(a) > 0:
            buckets = []
            for _ in range(a.max() + 1):
                buckets.append(List())

            while a._front is not None:
                v = a._front._value
                buckets[v]._move_front_to_rear(a)

            for bucket in buckets:
                if not bucket.is_empty():
                    a._append_list(bucket)
        return

    @staticmethod
    def pr(a):
        print(a._count, "-", [v for v in a], "-",
              a._front._value, "-", a._rear._value)
        return

    @staticmethod
    def quick_sort(a):
        if a._front is not None:
            lesser, equals, greater = Sorts._partition(a)
            Sorts.quick_sort(lesser)
            Sorts.quick_sort(greater)
            if lesser._front is not None:
                a._append_list(lesser)
            a._append_list(equals)
            if greater._front is not None:
                a._append_list(greater)
        return

    @staticmethod
    def _partition(source):
        lesser = List()
        greater = List()
        equals = List()
        equals._move_front_to_rear(source)
        pivot = equals._front

        while source._front is not None:
            if pivot._value > source._front._value:
                lesser._move_front_to_rear(source)
            elif pivot._value < source._front._value:
                greater._move_front_to_rear(source)
            else:
                equals._move_front_to_rear(source)
        return lesser, equals, greater
    
    
    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: radix_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a List of base 10 integers (List)
        Returns:
            None
        -------------------------------------------------------
        """
        buckets = [[], [], [], [], [], [], [], [], [], []]
        max_len = 0
        current = a._front

        while current is not None:
            num_len = len(str(current._value))

            if num_len > max_len:
                max_len = num_len
            current = current._next

        current = a._front

        for i in range(1, max_len+1):

            while current is not None:

                num_len = len(str(current._value))

                if num_len >= i:
                    digit = str(current._value)[-i]
                    digit = int(digit)

                    buckets[digit].append(current._value)

                else:
                    buckets[0].append(current._value)

                a.remove(current._value)
                current = current._next

            for container in buckets:
                for num in container:
                    a.append(num)

            current = a._front
            buckets = [[], [], [], [], [], [], [], [], [], []]

        return

