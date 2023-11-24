# Creating and Managing User-defined modules and Built-in modules in Python

# AddNumbers.py
def add(num1, num2):
    print("Addition of numbers: ", num1 + num2)

# Demo.py
import AddNumbers as an  # user-defined module
import math as mt    # built-in module
n1 = 144
n2 = 20
print("The square root of {0} is : ".format(n1), mt.sqrt(n1))
an.add(n1, n2)
