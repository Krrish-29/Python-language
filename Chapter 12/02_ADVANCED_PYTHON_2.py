# VIRTUAL ENVIRIONMENT
# An environment which is same as the system interpreter but is isolated from the other
# Python environments on the system.
# INSTALLATION
# To use virtual environments, we write:
# pip install virtualenv 
# We create a new environment using:
# virtualenv myprojectenv # Creates a new venv
# The next step after creating the virtual environment is to activate it.
# We can now use this virtual environment as a separate Python installation.


# # PIP FREEZE COMMAND
# ‘pip freeze’ returns all the package installed in a given python environment along with
# the versions.
# pip freeze > requirements .txt
# The above command creates a file named ‘requirements.txt’ in the same directory
# containing the output of ‘pip freeze’.
# We can distribute this file to other users, and they can recreate the same environment
# using:
# pip install –r requirements.txt


# LAMBDA FUNCTIONS
# Function created using an expression using ‘lambda’ keyword.
# Syntax:
expressions=10
lambda arguments:expressions
# can be used as a normal function
# Example:
square = lambda x:x*x
square(6) # returns 36
sum = lambda a,b,c:a+b+c
sum(1,2,3) # returns 6


# JOIN METHOD (STRINGS)
# Creates a string from iterable objects.
l = ["apple", "mango", "banana"]
result = ", and, ".join(l)
print(result)
# The above line will return “apple,and,mango,and,banana”.
# FORMAT METHOD (STRINGS)
# Formats the values inside the string into a desired output.
# template.format(p1,p2...)
# Syntax:
"{} is a good {}".format("harry", "boy") #1.
"{} is a good {o}".format("harry", "boy") #2.
# output for 1:
# harry is a good boy
# output for 2:
# boy is a good harry


# MAP, FILTER & REDUCE
# Map applies a function to all the items in an input_list.
# Syntax.
input_list=[]
map(function, input_list)
# the function can be lambda function
# Filter creates a list of items for which the function returns true.
list(filter(function))
# the function can be lambda function
# Reduce applies a rolling computation to sequential pair of elements.
from functools import reduce
val=reduce (function, input_list)
# the function can be lambda function