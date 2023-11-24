# update(): It updates a set with the union of this set and unique elements of other collection types, such as lists, tuples, sets, and so on. 

set1 = {'Zara', 'Lacoste', 'Fossil'}
list1 = ['Apple', 'Meta', 'Google', 'Apple']
set1.update(list1)
print(set1)
# Output: {'Zara', 'Fossil', 'Apple', 'Google', 'Lacoste', 'Meta'}

# add()	It adds an element to a set.	numbers = {7, 2, 11, 3, 4, 5}

print('The Initial Set:',numbers)
numbers.add(22)
print('The Updated Set:', numbers)
# Output: 
# The Initial Set: {2, 3, 4, 5, 7, 11}
# The Updated Set: {2, 3, 4, 5, 7, 11, 22}

# discard()	It removes a specified item.	set1 = {'Zara', 'Lacoste', 'Fossil'}
value = set1.discard('Lacoste')
print('Set after discard(): ', set1)
# Output: 
# Set after discard(): {'Fossil', 'Zara'}

# remove()	It removes a specified element. If the element is not a member, it raises a KeyError.	set1 = {'Zara', 'Fossil'}
removedValue = set1.remove('Lacoste')
print('Set after remove():', set1)
# Output: KeyError: 'Lacoste'

