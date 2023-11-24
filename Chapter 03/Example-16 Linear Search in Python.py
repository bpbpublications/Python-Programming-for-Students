# Linear Search

num_list = [11, 22, 44, 0, 11, 99, 55]
index = -1
length = len(num_list)
search = int(input("Enter a number to search : "))
# The range(start, end) function returns a sequence of numbers,
# starting from start value (0 by default) till end value.
for i in range(0, length):
    if num_list[i]==search:
        index = i
        break
if index==-1:
    print('Element not found')
else:
    print('Element found at index ', index)
