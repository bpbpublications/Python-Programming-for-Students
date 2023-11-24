# Finding factorial of a number using Recursion

def func_fact(num):
    if num == 0:
        return 1
    else:
        return num * func_fact(num - 1)  # Recursive call
number = int(input("Enter a number to find factorial : "))
print("The factorial of {0} is: ".format(number), func_fact(number))
