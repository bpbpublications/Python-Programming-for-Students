# Queue data structure

queue1 = ['one', 'two', 'three']
print(queue1)
queue1.append('four') # Pushing new elements in rear end of Queue
queue1.append('five')
print(queue1)
print("First element : ", queue1[0]) # Print head element of Queue
size = len(queue1) # Print the last or tail element
print("Last element : ",queue1[size - 1])
queue1.remove(queue1[0]) # Popping an element from front queue
print(queue1)
