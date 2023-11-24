# Demonstrating the use of variable-length arguments:

def func1(*args):  # Here args can take any number of parameters
    list1 = []
    for i in args:
        list1.append(i.upper())
    return list1
output = func1() # Calling function with no arguments
print("The updated output of *args : ", output)
output = func1("Apple", "Mango") # Calling function with 2 arguments
print("The updated output of *args : ", output)

def func2(**kwargs):  # Here kwargs can take any number of keyword parameters
    list1 = []
    for key, value in kwargs.items():
        list1.append([key, value])
    return list1
# Calling function with 'n' number of keyword arguments
output = func2(num1=10,num2=20, num3=30, num4=40, num5=50)
print("The updated output of **kwargs: ", output)
