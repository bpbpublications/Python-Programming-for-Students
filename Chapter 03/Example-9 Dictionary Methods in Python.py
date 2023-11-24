# Dictionary Methods with Examples

dict1 = {'s_id':101, 's_name':'Charlie', 's_age': 20 }

# get()	This method returns the value corresponding to the given key.
print(dict1.get('s_age'))
# Output: 20

# items() This method returns dictionary elements in the form of a list of tuples for each key-value pair.
print(dict1.items())
# Output: dict_items([('s_id', 101), ('s_name', 'Charlie'), ('s_age', 20)])

# keys() This method returns a list of all keys in the dictionary.
print(dict1.keys())
# Output: dict_keys(['s_id','s_name', 's_age'])

# pop()	This method removes the key: value pair from the dictionary with the key specified as the method argument.
print(dict1.pop('s_age'))
print(dict1)
# Output: 20
# {'s_id': 101, 's_name': 'Charlie'}

# update() This method updates the dictionary with the specified key: value pair. In case the pair is already present, then it gets updated. Otherwise, a new pair is added to the dictionary.
dict1.update({'s_degree':'B.Tech'})
print(dict1)
# Output:
# {'s_id': 101, 's_name': 'Charlie', 's_age': 20, 's_degree': 'B.Tech'}

# values() This method returns a list of all values in the dictionary.
print(dict1.values())
# Output: 
# dict_values([101, 'Charlie', 20])

