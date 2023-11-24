# Demo of append() : This method appends a new element at the end of the current list.
countries = [‘India’, ‘Australia’, ‘Dubai’]
countries.append(‘US’)
print(countries)
# Output: [‘India’, ‘Australia’, ‘Dubai’, ‘US’]

# Demo of clear(): This method returns an empty list after removing all elements in the current list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
numbers.clear()
print(‘List after clear(): ’, numbers)
# Output: List after clear(): []

# Demo of copy(): This method creates and returns a copy of the current list.
list1 = [1, 2, 3, 4, 5]
copy_list = list1.copy()
print(‘Copied List is : ‘, copy_list)
# Output: Copied List: [1, 2, 3, 4, 5]

# Demo of count(): This method returns the count of occurrences of an element within the list.
numbers = [12, 33, 51, 12, 61, 12, 7, 9]
count = numbers.count(12)
print(‘Count of 12 is ’, count)
# Output: Count of 12 is 3

# Demo of extend(): It adds one or more elements present in another list to the end of the current list.
numbers = [1, 2, 3]
new_numbers = [4, 5]
new_numbers.extend(numbers)
print('List after extend() :', new_numbers)
# Output: List after extend(): [1, 2, 3, 4, 5]

# Demo of index(): Returns the index of the first occurrence of the element with the specified value.
countries = [‘India’, ‘Australia’, ‘Dubai’]
index = countries.index(‘Dubai’)
print(index)
# Output: 2

# Demo of insert(): Adds an element at the specified position.
vowels = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
vowels.insert(3, 'o')
print('New List:', vowel)
# Output: New List: ['a', 'e', 'i', 'o', 'u']

# Demo of pop(): It removes the element at the specified position in the current list.
numbers = [22, 33, 55, 77]
rem_element = numbers.pop(2)
print('Removed Element: ', rem_element)
print('Updated List: ', numbers)
# Output: 
# Removed Element: 55
# Updated List: [22, 33, 77]

# Demo of remove(): It removes the first occurrence of an element with the specified value from the current list.
numbers = [22, 77, 33, 55, 77, 99, 111, 77]
numbers.remove(77)
print('Updated List: ', numbers)
# Output: Updated List: [22, 33, 55, 77, 99, 111, 77]

# Demo of reverse(): Reverses the order of the list.
numbers = [22, 33, 5, 77, 99, 111]
numbers.reverse()
print('Reversed List:', numbers)
# Output: Reversed List:[111, 99, 77, 5, 33, 22]

# Demo of sort(): Sorts the list.
numbers = [17, 11, 33, 77, 55, 22, 9]
numbers.sort()
print(numbers)
# Output: [9, 11, 17, 22, 33, 55, 77]

