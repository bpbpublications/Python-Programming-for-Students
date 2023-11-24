# calculate the sum of items declared in a tuple using For Loop
numbers = (10, 20, 30, 40, 50)
sum = 0
count = 1
for var in numbers:
    print("In iteration count ", count, "value of var is = ", var)
    sum = sum + var
    count = count + 1
else:
    print('The Sum of numbers is : ', sum)
