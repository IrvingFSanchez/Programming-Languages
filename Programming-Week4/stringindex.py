# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: String Indexing, Index Location, Parentheses Checker, Tower Printer, Missing Number

"""
This particular program exctracts characters from the input string in a patter of 3 on, 3 off.

Meaning the pattern selects the first three characters, skips the next three, then selects the next three, so on and so forth.
This is essentially the same as taking every block of three characters starting at position 0, 6, 12, etc.
"""

print("""
====================================
    PART 1: STRING INDEXING
====================================
""")

# this just declares a function named extract_pattern that takes a string s as input
def extract_pattern(s): # a single parameter s
    select_chunks = [] # This just creates an empty list to store chunks of the string we extract hence = [] assigns an empty list to the variable select_chunks
    # the for loop below iterates through the string indices in steps of 6 (0, 6, 12, ...) 
    for start in range(0, len(s), 6): # for is the keyword to start loop, range (0, len(s), 6) generates numbers from 0 to len(s) -1, stepping by 6
        chunk = s[start:start + 3] # this uses slicing to grab a substring, starting at index start up to start + 3 (not inclusive)
        select_chunks.append(chunk) # this is a method that adds "chunk" to the end of the list select_chunks but using .append(chunk) method
    # this just exits the function and gives a value back. 
    return ''.join(select_chunks) # '' is an empty string, and .join(select_chunks) glues all the strings in the list select_chunks into a single string

# Print Test
input_string = "abcdefghijklmnopqrstuvwxyz" # input_string is just the variable assigned to the string "abcdefghijklmnopqrstuvwxyz"
output = extract_pattern(input_string) # this calls the extract_pattern function above with input_string as the argument and assigns the result to output
print(f"Input String: {input_string}") # just prints the input string to the console and (f" ") is an f-string which lets you insert variables inside curly braces {} 
print(f"Output String: {output}")


print("""
====================================
    PART 2: INDEX LOCATION
====================================
""")

"""
This code block finds all starting indices of the given pattern in a string.

Args:
    s (str): The input string to search in.
    pattern (str): The pattern to find in the string.
    
Returns:
    list: A list of starting indices where the pattern is found in the string. Empty list if it's not found.

"""

def index_pattern_locator(s, pattern): # creates a function called index_pattern_locator that takes two parameters: s and pattern, pattern is the string we are looking for in s
    
    indices = [] # this just creates an empty list to store the indices of the pattern found in the string s 
    pattern_length = len(pattern) # this just determines the length of the pattern string and saves it to the variable pattern_length
    
    # This just iterates over each possible starting index in the string where the pattern could fit
    for i in range(len(s) - pattern_length + 1): # this just iterates over the string s from 0 to len(s) - pattern_length + 1, so it doesn't go out of bounds
        # This is saying extract the substring of length equal to the pattern starting at index i
        substring = s[i:i + pattern_length]
        # This just checks if the substring matches the pattern
        if substring == pattern:
            indices.append(i) # this adds the index to the list if there is a match
            
    return indices # this just returns the list of indices where the pattern was found in the string s

# Print Test
input_string = "abaaababbbbaaabbabababababbbaaaaabababababbbbb"
pattern = "abb" # this just assigns the pattern to the variable pattern
result = index_pattern_locator(input_string, pattern) # this calls the index_pattern_locator function above with input_string and pattern as arguments and assigns the result to result
print (f"Input String: {input_string}") # just prints the input string to the console and (f" ") is an f-string which lets you insert variables inside curly braces {}
print (f"Pattern: {pattern}") 
print (f"Pattern Indices: {result}")



print("""
====================================
    PART 3: PARENTHESES CHECKER
====================================
""")

"""
For this code block we are checking if an expression has a proper balance of parentheses.

Args:
    expression (str): The input string containing parentheses to check.
    
Returns:
    bool: True if the parentheses are balanced, False otherwise.
"""

def paranth_balance(expression): # creates a function called paranth_balance that takes a single parameter 'expression'

    balance = 0  # Here the line starts a counter at 0
    for char in expression: # this translates to for each character in the expression
        if char == '(': # this translates to if the character is an opening parenthesis. == is a comparison operator that checks if the left side is equal to the right side
            balance += 1 # this means balance = balance + 1, so it adds 1 to the balance counter if it finds an opening parenthesis
        elif char == ')': # else if the character is a closing parenthesis then do the following:
            balance -= 1 # this means balance = balance - 1, so it subtracts 1 from the balance counter if it finds a closing parenthesis
            # If balance goes negative, a closing parenthesis has no matching opener
            if balance < 0: # this translates to if the balance is less than 0 then do the following below:
                return False # in other words if at any point there are more closing ) than opening ( then it is unbalanced so return False meaning the parantheses are unbalanced
    
    return balance == 0 # Here we are saying if balance is exactly 0, then all opening parentheses have been matched with closing ones

# Example usage with additional test cases
sample1 = "((a+b)"
sample2 = "(((a+b)+c)+d)+e"
sample3 = ")("          # Unbalanced: starts with closing parenthesis
sample4 = "(a + (b * c) - (d / e))"

print(f"Sample 1: {sample1}")
print(f"Balanced? {paranth_balance(sample1)}")  # Output: False

print(f"\nSample 2: {sample2}")
print(f"Balanced? {paranth_balance(sample2)}")  # Output: True

print(f"\nSample 3: {sample3}")
print(f"Balanced? {paranth_balance(sample3)}")  # Output: False

print(f"\nSample 4: {sample4}")
print(f"Balanced? {paranth_balance(sample4)}")  # Output: True

print("""
====================================
    PART 4: TOWER PRINTER
====================================
""")

def tower(n): # this function takes one input called n
    """Generates a tower pattern where each subsequent segment has increasing spaces.
    
    For each segment i (0-indexed):
    - Top line: '/' followed by i spaces, then doubleslashes. Note single-slash in Python is an escape character, so we use double backslash to print a single backslash.
    - Next two lines: '*' followed by i spaces, then '*'.
    """
    segments = [] # this will collect all the lines and symbols of the tower to build it 
    for i in range(n): # for i in range(n) means it will loop from 0 to n-1, so if n = 4, it will loop 4 times (0, 1, 2, 3)
        top_line = '/' + (' ' * i) + '\\' # this creates the top line of the tower, with i spaces in between the slashes. The (' ' * i) means it will create a string of spaces of length i
        star_line = '*' + (' ' * i) + '*' # this creates the star line of the tower, with i spaces in between the stars. The (' ' * i) means it will create a string of spaces of length i
        segments.append(top_line) # this adds the top line to the segments list
        segments.append(star_line) # this adds the star line to the segments list
        segments.append(star_line) # this adds the star line to the segments list again, so it appears twice in the tower
    print('\n'.join(segments)) # this prints the segments list as a single string, with each element separated by a newline character. 
    # The '\n' is the newline character in Python, so it will print each segment on a new line

# Print Test
print("tower(1)")
tower(1) # this calls the tower function with 1 as the argument, so it will print a tower with 1 segment
print("\ntower(2)")
tower(2) # this calls the tower function with 2 as the argument, so it will print a tower with 2 segments so on and so forth
print("\ntower(3)")
tower(3)
print("\ntower(4)")
tower(4)

# Note, the bigger the tower number the wider the tower gets so it'll adjust the spaces accordingly. I use i to adjust the spaces in between the symbols.

print("""
====================================
    PART 5: MISSING NUMBER
====================================
""")

"""
Finds the missing number in a list of integers from 1 to N (one missing).
"""

def find_missing_num(nums): # define the function find_missing_num that takes a list of numbers as input

    n = len(nums) + 1  # the length of how many numbers are in a list, but since one is missing we add 1 to the length of the list
    expected_sum = n * (n + 1) // 2  # Sum of first N natural numbers
    actual_sum = sum(nums)  # Sum of the given list
    return expected_sum - actual_sum  # The difference is the missing number

# Example usage
sample_input = [3, 5, 2, 1]
print(f"Sample Input: {sample_input}")
print(f"Missing Number: {find_missing_num(sample_input)}")  # Output: 4
second_input = [1, 2, 3, 4, 6]
print(f"Second Input: {second_input}")
print(f"Missing Number: {find_missing_num(second_input)}")  # Output: 5

# Super important note: This only functions if there is only one number missing from the list. If there are multiple numbers missing, this will not work.

'''
Note to self-
Why does this work:
If you pair up every number from start to end, the sum of each pair is the same.
For example, in the list [1, 2, 3, 4, 6], the pairs are (1, 6), (2, 5), and (3, 4). The sum of each pair is 7.
If n is odd, the middle number is unpaired, but the sum of all pairs is still equal to the expected sum.
If n is even, the missing number is the average of the two middle numbers.
This is why the formula works. It calculates the expected sum of all numbers from 1 to n, and then subtracts the actual sum of the numbers in the list to find the missing number.
Cool Fact to Self:
This was formula was founded by a guy named Carl Friedrich Gauss. n + (n + 1) / 2 
'''