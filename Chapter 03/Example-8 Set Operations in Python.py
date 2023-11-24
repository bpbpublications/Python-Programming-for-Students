# Demonstration of various Set operations:

# Declare two sets
X = {11, 33, 55, 66, 77}
Y = {22, 33, 44, 66}

print('Union with |:', X | Y)
print('Union with union():', X.union(Y))
print('Intersection with &:', X & Y)
print('Intersection with intersection():', X.intersection(Y))
print('Difference with - :', X - Y)
print('Difference with difference():', X.difference(Y))
print('Symmetric Difference with ^:', X ^ Y)
print('Now with symmetric_difference():', X.symmetric_difference(Y))
