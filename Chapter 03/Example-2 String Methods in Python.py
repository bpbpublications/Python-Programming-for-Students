# Various String methods with examples

str1 = "Hello to Python World"
print(str1.count(‘Python’))
# Output: 1

print(str1.endswith(‘m’))
# Output: False

print(str1.find('to ', 4, 11))
# Output: 6
#It searches for substring ‘to’ in str1 and returns 6

print(str1.index("python",2,20))
# Output: ValueError: substring not found

str2 = 'hot coffee served hot in hot weather'
# replacing 'hot' with 'cold'
print(str2.replace('hot', 'cold'))
# Output: cold coffee served cold in cold weather

new_str = "abc123"
print(new_str.isalnum())
print(new_str.isalpha())
print(new_str.isdigit())
# Output: True  False  False

print("hello".islower())
# Output: True

print(("HELLO").isupper())
# Output: True

str2 = ‘   Python  Demo ‘
print(str2.strip())
# Output: Python Demo

fruits = 'Apple, Mango, Banana, Peach, Olive'
# When maxsplit is 2
print(fruits.split(',', 2))
# When no maxsplit is given
print(fruits.split(','))

# Output:
# ['Apple', ' Mango', ' Banana, Peach, Olive']
# ['Apple', ' Mango', ' Banana', ' Peach', ' Olive']

str3 = '''I
want to
learn
Python Coding.'''
print(str3.splitlines())

# Output:
# ['I', 'want to', 'learn', 'Python Coding']
