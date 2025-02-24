# class Employee: # Class name is written in pascal case
    # Methods & Variables 

class Employee:
    company = "Google" # Specific to Each Class
krrish = Employee() # Object Instatiation
krrish.company
Employee.company = "YouTube" # Changing Class Attribute
krrish.name = "krrish"
krrish.salary = "30k" # Adding instance attribute 

krrish.getSalary() # here self is krrish
# equivalent to Employee.getSalary(krrish)
class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is not there")
    @staticmethod # decorator to mark greet as a static method
    def greet():
        print("Hello user")

class Employee:
    def __init__(self, name,salary):#dunder method which is automatically called
        self.name=name
        self.salary=salary
    def getSalary(self):
        print(self.salary)
krrish = Employee("krrish",12000000)