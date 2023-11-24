# calculate the square root of an input entered by a user an infinite number of times
# import the math module 
import math 
while True:
    num = int(input("Enter a number to see its square root: "))
    # calculate square root using math.sqrt() and print the result
    sqroot = math.sqrt(num)
    print("The square root of ",num," is : ",sqroot)
    # We must press Ctrl+c to exit from the loop
