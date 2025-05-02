# WALRUS OPERATOR
# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to
# variables as part of an expression. This operator, named for its resemblance to the eyes
# and tusks of a walrus, is officially called the "assignment expression."
# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)


# Type hints are added using the colon (:) syntax for variables and the -> syntax for
# function return types.
# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice")) # Output: Hello, Alice!


# ADVANCED TYPE HINTS
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict,
# and Union.
# You can import List, Tuple and Dict types from the typing module like this:
from typing import List, Tuple, Dict, Union

# The syntax of types looks something like this:
from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid


# MATCH CASE
# Python 3.10 introduced the match statement, which is similar to the switch statement
# found in other programming languages.
# The basic syntax of the match statement involves matching a variable against several
# cases using the case keyword.
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status


# DICTIONARY MERGE & UPDATE OPERATORS
# New operators | and |= allow for merging and updating dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}
# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager
with (
open('file1.txt') as f1,
open('file2.txt') as f2  ):
    pass
# Process files


# EXCEPTION HANDLING IN PYTHON
# There are many built-in exceptions which are raised in python when something goes
# wrong.
# Exception in python can be handled using a try statement. The code that handles the
# exception is written in the except clause.
try:
    pass
    # Code which might throw exception
except Exception as e:
    print(e)
# When the exception is handled, the code flow continues without program interruption.
# We can also specify the exception to catch like below:
try:
    pass
    # Code
except ZeroDivisionError:
    pass
    # Code
except TypeError:
    pass
    # Code
except:
    pass
    # Code # All other exceptions are handled here.


# We can raise custom exceptions using the ‘raise’ keyword in python.


# TRY WITH ELSE CLAUSE 
try:
    pass
    # Somecode
except:
    pass
    # Somecode
else:
    pass
    # Code # This is executed only if the try was successful


# TRY WITH FINALLY
# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
# the exception.
try:
    pass
    # Some Code
except:
    pass
    # Some Code
finally:
    pass
    # Some Code # Executed regardless of error!


# IF __NAME__== ‘__MAIN__’ IN PYTHON
# ‘__name__’ evaluates to the name of the module in python from where the program is
# ran.
# If the module is being run directly from the command line, the ‘ __name__’ is set to
# string “__main__”. Thus, this behaviour is used to check whether the module is run
# directly or imported to another file.


# THE GLOBAL KEYWORD
# ‘global’ keyword is used to modify the variable outside of the current scope.


# ENUMERATE FUNCTION IN PYTHON
# The ‘enumerate’ function adds counter to an iterable and returns it
list1 = [1,7,12,11,22]
for i,item in list1:
    print(i,item) # Prints the items of list 1 with index


# LIST COMPREHENSIONS
# List Comprehension is an elegant way to create lists based on existing lists.
list1 = [1,7,12,11,22]
list2 = [i for item in list1 if item > 8]