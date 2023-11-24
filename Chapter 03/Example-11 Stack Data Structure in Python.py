# Stack Data Structure

stack1 = ['one', 'two', 'three']
print(stack1)
top = len(stack1) – 1 # Top position is the last index of stack list
print("Current Top is : ", top)
stack1.append('four') # push element to top position
stack1.append('five')
print(stack1)
top = len(stack1) – 1 # Find updated Top position
print("Updated Top is : ", top)
stack1.pop()   # Pop an element from stack
print(stack1)
top = len(stack1) – 1 # Find updated Top position
print("Updated Top is : ", top)
