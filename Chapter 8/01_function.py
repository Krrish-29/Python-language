def func1():
    print('hello')
func1() # This is called function call.

def greet(name):
    gr = "hello"+ name
    return gr
a = greet ("harry")

def greet(name = "stranger"):
   print(name)
greet() # name will be "stranger" in function body (default)
greet("krrish") # name will be "harry" in function body (passed)

def factorial(n):
    if n == 0 or n==1: # base condition which doesn’t call the function any further
        return 1
    else:
        return n*factorial(n-1) # function calling itself
factorial(5)