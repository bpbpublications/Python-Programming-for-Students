# Demonstration of Bitwise Operators
a = 10 
b = 4 
print(a & b)
# Output: 0 (0000 0000)
print(a | b)
# Output: 14 (0000 1110)
print(a ^ b)
# Output: 14 (0000 1110)
print(~a)
# Output: -11
For unsigned number
Let a = 10 = 0000 1010 (Binary)
a >> 1 = 0000 0101 = 5
a >> 2 = 0000 0010 = 2
For signed numbers use 2’s complement form
Let a = -10 
print(a >> 1) 
# Output:  -5
print(a >> 2) 
# Output: -3
# For unsigned number.
c = 5 
print(c << 1)
# Output: 10
print(c << 2)
# Output: 20 
d = –10 
print(d << 1) 
# Output: –20
print(d << 2) 
# Output: –40
