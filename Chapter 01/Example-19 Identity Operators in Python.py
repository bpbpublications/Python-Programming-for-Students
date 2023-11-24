# Demonstration of Identity Operators
a = 10
b = 10
str1 = 'Hello'
str2 = 'Hello'
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print(a is b)
#returns True

print(str1 is str2) 
#returns True

print(list1 is list2) 
#returns False

print(a is not b) 
#returns False

print(str1 is not str2) 
#returns False

print(list1 is not list2) 
#returns True
