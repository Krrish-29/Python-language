class Employee: # Base class
    pass
class Programmer(Employee): # Derived or child class
    pass 

super().__init__()
# __init__() Calls constructor of the base class

class Employe:
    # @classmethod decorator is used to create a class method    
    @classmethod
    def s(cls,p1,p2):
        pass
class Employee:
    @property
    def name(self):
        return self.ename
    
    # The method name with ‘@property’ decorator is called getter method.
    @name.setter
    def name (self,value):
        self.ename = value

# Operators in Python can be overloaded using dunder methods.
p1+p2 # p1.__add__(p2)
p1-p2 # p1.__sub__(p2)
p1*p2 # p1.__mul__(p2)
p1/p2 # p1.__truediv__(p2)
p1//p2 # p1.__floordiv__(p2)
str__() # used to set what gets displayed upon calling str(obj)
__len__() # used to set what gets displayed upon calling.__len__() or len(obj)