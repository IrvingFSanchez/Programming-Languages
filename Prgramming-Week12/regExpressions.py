# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: Regular Expressions - Pattern Matching and String Manipulation

"""
This program demonstrates various regular expression operations in Python:
1. Matching patterns with 'a' followed by zero or more 'b's
2. Finding sequences of uppercase followed by lowercase letters
3. Detecting words containing 'z'
4. Checking for numbers at string endings
5. Swapping between spaces and underscores

Each task is implemented as a separate function with clear test cases.
"""

import re  # Import the regular expressions module

print("""
====================================
    PART 1: THE AB-SEEKER
====================================
""")

def ab_seeker(text):
    """
    Finds patterns where 'a' is followed by zero or more 'b's in a string.
    
    Args:
        text (str): The input string to search
        
    Returns:
        bool: True if pattern found, False otherwise
        
    Explanation:
        The pattern r'a[b]*' means:
        - 'a' must appear
        - followed by any number of 'b's (including zero)
        - The * quantifier means "zero or more occurrences"
    """
    pattern = r'a[b]*'  # Regular expression pattern
    return bool(re.search(pattern, text))  # Returns True if pattern found in text

# Test cases for AB-Seeker
ab_string_data = [
    "ac", "abc", "abbc", "eieio ax zzbb cc a bba",
    "aaaabab aaa", "xxxx abzzzzz", "uuuuuu"
]

for string_data in ab_string_data:
    if ab_seeker(string_data):
        print(f"{string_data} has a match!")
    else:
        print(f"{string_data} not matched!")

print("""
====================================
    PART 2: THE CAPITAL-FOLLOWER
====================================
""")

def capital_follower(text):
    """
    Finds sequences of one uppercase letter followed by lowercase letters.
    
    Args:
        text (str): The input string to search
        
    Returns:
        bool: True if pattern found, False otherwise
        
    Explanation:
        The pattern r'[A-Z][a-z]+' means:
        - [A-Z] matches any single uppercase letter
        - [a-z]+ matches one or more lowercase letters
        - The + quantifier means "one or more occurrences"
    """
    pattern = r'[A-Z][a-z]+'  # Regular expression pattern
    return bool(re.search(pattern, text))  # Returns True if pattern found

# Test cases for Capital-Follower
capital_test_strings = [
    "AaBbGg", "Python", "python", "PYTHON", "aA", "Aa"
]

for string_data in capital_test_strings:
    if capital_follower(string_data):
        print(f"{string_data} has a match!")
    else:
        print(f"{string_data} not matched!")

print("""
====================================
    PART 3: THE Z-DETECTOR
====================================
""")

def z_detector(text):
    """
    Detects words containing the letter 'z' (case insensitive).
    
    Args:
        text (str): The input string to search
        
    Returns:
        bool: True if pattern found, False otherwise
        
    Explanation:
        The pattern r'\w*z\w*' means:
        - \w* matches zero or more word characters (letters, digits, underscores)
        - z matches the literal 'z'
        - \w* matches zero or more word characters after the 'z'
        - text.lower() makes the search case insensitive
    """
    pattern = r'\w*z\w*'  # Regular expression pattern
    return bool(re.search(pattern, text.lower()))  # Case insensitive search

# Test cases for Z-Detector
z_test_strings = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises.",
    "I like pizza.",
    "UC Berkeley courses use Piazza"
]

for string_data in z_test_strings:
    if z_detector(string_data):
        print(f"{string_data} has a match!")
    else:
        print(f"{string_data} not matched!")

print("""
====================================
    PART 4: THE NUMBER-ENDER
====================================
""")

def number_ender(text):
    """
    Checks if a string ends with a number.
    
    Args:
        text (str): The input string to check
        
    Returns:
        bool: True if string ends with number, False otherwise
        
    Explanation:
        The pattern r'.*\d$' means:
        - .* matches any character (except newline) zero or more times
        - \d matches any digit (0-9)
        - $ asserts position at the end of the string
    """
    pattern = r'.*\d$'  # Regular expression pattern
    return bool(re.search(pattern, text))  # Returns True if pattern matches

# Test cases for Number-Ender
number_test_strings = [
    "abcde", "forever21", "george bush", 
    "level 5", "twins2", "lululemon123t good"
]

for string_data in number_test_strings:
    if number_ender(string_data):
        print(f"{string_data} has a match!")
    else:
        print(f"{string_data} not matched!")

print("""
====================================
    PART 5: THE SPACE-SWAPPER
====================================
""")

def space_swapper(original_string):
    """
    Swaps spaces with underscores and vice versa in a string.
    
    Args:
        original_string (str): The input string to transform
        
    Explanation:
        - First replaces spaces with underscores
        - Then replaces underscores in the new string back to spaces
        - Demonstrates both transformations
    """
    # Replace spaces with underscores
    space_to_underscore = original_string.replace(' ', '_')
    
    # Replace underscores with spaces (using the new string)
    underscore_to_space = space_to_underscore.replace('_', ' ')
    
    print(f"Original String:  {original_string}")
    print(f"space by _     :  {space_to_underscore}")
    print(f"_ by space     :  {underscore_to_space}\n")

# Test cases for Space-Swapper
space_test_strings = [
    "Wall Street", "Computer Science", 
    "long long ago", "real-estate"
]

for original_string in space_test_strings:
    space_swapper(original_string)

"""
Final Notes:
1. Regular expressions are powerful for pattern matching in strings
2. The re module provides search() and other functions for regex operations
3. Important regex components used:
   - * for zero or more occurrences
   - + for one or more occurrences
   - \w for word characters
   - \d for digits
   - $ for end of string
4. String methods like replace() are useful for simple transformations
"""