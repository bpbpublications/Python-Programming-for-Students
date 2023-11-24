# To create a dictionary
new_dict1 = {1: "January", 2: "February", 3: "march", 4: "April", 5: "May"}
# To display dictionary
print("Dictionary new_dict1 is: ",new_dict1)  
# To create a dictionary using a dict class
new_dict2 = dict({6: "June", 7: "July", 8: "August", 9: "September"})
# To display new dictionary
print("Dictionary new_dict2 is: ", new_dict2)
# To view the type of Dictionaries
print("Type of new_dict1: ", type(new_dict1))
print("Type of new_dict2: ", type(new_dict2))
# To access values 'January' and 'February' using their keys
print("Value of key 1: ", new_dict1[1])
print("Values in key 2: ", new_dict1[2])
# To change the value of a key and display updated value
new_dict1[3] = "March"
print("Updated value for key 3: ", new_dict1[3])
