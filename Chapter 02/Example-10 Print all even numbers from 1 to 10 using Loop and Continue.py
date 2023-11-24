# To print all even numbers from 1 to 10
num = 0
print("All even numbers from 1-10 are : ")
while num < 10:
    num += 1
    # Check if num not divisible by 2 i.e., for odd number
    # continue with the next iteration of the loop otherwise
    # for even number print num in Line 11.
    if (num % 2)!= 0:
        continue
    print(num)
