# Insertion Sort

num_list = [30,10,17,4,6]
n = len(num_list)
for i in range(1,n):
    temp = num_list[i]
    j = i - 1
    while(j >= 0 and temp < num_list[j]):
        num_list[j + 1] = num_list[j]
        j -= 1
    num_list[j + 1] = temp
print('Array after sorting')
print(num_list)
