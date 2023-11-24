# Binary Search

num_list = [0, 11, 22, 44, 55, 99]
search = int(input('Enter a number to search '))
low = mid = 0
high = len(num_list) - 1
index = -1
while low <= high:
    mid = (high + low) // 2    # mid is the middle index of the list
    if num_list[mid] < search:
        low = mid + 1
    elif num_list[mid] > search:
        high = mid - 1
    else:
        index = mid
        break
if index == mid:
    print("Number found at index ", index)
else:
    print("Number Not Found!!")
