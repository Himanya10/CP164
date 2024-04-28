"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Himanya Verma
ID:      169051154
Email:   verm1154@mylaurier.ca
__updated__ = "2024-02-05"
-------------------------------------------------------
"""
# Imports
# Constants
def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x-1, y) + recurse(x,y-1)
    
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        ans = n 
    else:
        ans = gcd(n, m % n)
        
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    if not s:
        count = 0
    elif s[0].lower() in vowels:
        count = 1 + vowel_count(s[1:])
    else:
        count = vowel_count(s[1:])
    return count

def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power > 0:
        ans = base * to_power(base, power - 1)
    else:
        ans = 1 / to_power(base, -power)
    
    return ans

def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    # Helper function to check if a character is a letter
    is_letter = lambda char: char.isalpha()

    # Helper function to convert a string to lowercase and filter out non-letters
    clean_string = lambda string: ''.join(c.lower() for c in string if is_letter(c))

    # Recursive function to check if the cleaned string is a palindrome
    is_palindrome = (lambda f: lambda s: f(f, s))(lambda self, s: True if len(s) <= 1 else (s[0].lower() == s[-1].lower() and self(self, s[1:-1])))

    # Clean the input string and check if it's a palindrome
    cleaned_string = clean_string(s)
    return is_palindrome(cleaned_string)

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    return [] if not bag else [bag[0]] + bag_to_set([x for x in bag[1:] if x != bag[0]])

        
    



        