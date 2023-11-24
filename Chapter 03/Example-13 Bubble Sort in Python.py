# Bubble Sort in Python

num_list = [30,9,6,3,2]
n = len(num_list)
for i in range(n-1):
    for j in range(n-1-i):
        if num_list[j]>num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
print('Array after sorting')
print(num_list)
