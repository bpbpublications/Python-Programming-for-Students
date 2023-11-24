# check for Even and Odd numbers between 1 and 10 using a while loop

start = 1
end = 20
# while loop to check for even/ odd numbers from start to end
print("Checking for Even/ Odd numbers in range 1-10..")
num = start
while num <= end:
    if(num%2 == 0):
        print(num, " is even number")
    elif num==0:
        print(num, " is zero")
    else:
        print(num, " is odd number")
    num = num + 1
else:
    print("End of Loop!!")
