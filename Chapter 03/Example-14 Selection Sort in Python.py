# Selection Sort

num_list = [30,10,17,4,6]
n = len(num_list)
for i in range(n-1):
    smallest = i
    for j in range(i+1, n):
        if (num_list[j] < num_list[smallest]):
            smallest = j
    num_list[i], num_list[smallest] = num_list[smallest], num_list[i]
print('Array after sorting')
print(num_list)
