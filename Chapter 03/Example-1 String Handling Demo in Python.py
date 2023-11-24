str1 = "Hello, Trainees!"
str2 = "Welcome to learn Python."
str3 = "Hello, Trainees!"
# Compare str1 and str2
print(str1 == str2)
# Compare str1 and str3
print(str1 == str3)
# Concatenation using + operator
result = str1 + str2
print(result)
# Slice str1 from 1st index to 10th index with skip of 2 characters
print(str1[1:10:2])
# Membership test using in and not in
print('a' in 'Java')      # returns True
print('n' not in 'Python')  # returns False
# String formatting using %
print("His name is %s and age is %d years!" % ('John', 25))
# Raw string using r or R
print(r'C:\Folder\SubFolder\File1')
# Repeat the string "Bye" 2 times
result = "Bye" * 2
print(result)
