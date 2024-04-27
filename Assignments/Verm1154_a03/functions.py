"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
# Constants
from Stack_array import Stack


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    #stating that target is a stack 
    target = Stack()

    # while source 1 and source 2 are not empty:
    while not(source1.is_empty() and source2.is_empty()):
        # if source 1 is not empy:
        if not(source1.is_empty()):
            #pop the object out of the stack and push the next one in (LIFO)
            target.push(source1.pop())
        # if source 2 is not empty
        if not(source2.is_empty()):
            #pop the object our of the stack and push the next one in (LIFO)
            target.push(source2.pop())
          
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    # stating that s is a stack
    s = Stack()
    # while source is not empty
    while not source.is_empty():
        # pop the object and then push the next one in (LIFO)
        s.push(source.pop())
    # while stack is not empty 
    while not s.is_empty():
        # pop the object and then push the next one in (LIFO)
        source.push(s.pop())
    
    return None


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    # stating that s is a stack
    s = Stack()
    # set palindrome equal to true by default
    palindrome = True
    # for the characters in string
    for char in string:
        # if said characters are within the alphabet (is.aplha() = true if a-z)
        if char.isalpha():
            #make the characters lowecase and then push them into the stack
            s.push(char.lower())
    # for character in string 
    for char in string:
        # if character is within the alphabet
        if char.isalpha():
            # if the character is lowercase then dont take the stack and pop the value
            if char.lower() != s.pop():
                # setting palindrome to false if all parameters are met 
                palindrome = False
    return palindrome


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    # Defining s as Stack 
    s = Stack()
    #splitting the string
    string = string.split()
    # for characters in the string 
    for char in string:
        # if the character is a digit
        if char.isdigit():
            # push the character into the stack
            s.push(char)
        # if the character in operators 
        if char in OPERATORS:
            # if character is "+"
            if char == "+":
                #set right to the interger that is popped from the stack
                right = int(s.pop())
                # set left that is popped from the stack next
                left = int(s.pop())
                # adding left and right together
                s.push(left + right)

            if char == "-":
                #set right to the interger that is popped from the stack
                right = int(s.pop())
                # set left that is popped from the stack next
                left = int(s.pop())
                # subtarcting left and right together
                s.push(left - right)

            if char == "*":
                #set right to the interger that is popped from the stack
                right = int(s.pop())
                # set left that is popped from the stack next
                left = int(s.pop())
                # multiplying left and right together
                s.push(left * right)

            if char == "/":
                #set right to the interger that is popped from the stack
                right = int(s.pop())
                # set left that is popped from the stack next
                left = int(s.pop())
                #dividng left and right together
                s.push(left / right)
    # setting the answer to the stack whose values would be popped           
    answer = s.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    # setting s equal to stack
    s = Stack()
    # defining path as an index
    path = []
    #defining visited as an index
    visited = []
    #pushing the stack 
    s.push("Start")
    
    # while stack is not empty
    while not(s.is_empty()):
        #definign point as the stacks poppped values
        point = s.pop()
        
        # if point is X
        if point == "X":
            #append the point to the path index
            path.append(point)
            break
        # if the point isn't in visited
        if point not in visited:
            #append the point to the visited index
            visited.append(point)
            #append the point to the path index
            path.append(point)
            
            # if the point is in maze
            if point in maze:
                # for the value in maze at the point
                for value in maze[point]:
                    #push the value of the stack 
                    s.push(value)
      
    # if the path and path at -1 are not equal to X              
    if path and path[-1] != "X":
        # this indicates that there is no path 
        path = None
    return path