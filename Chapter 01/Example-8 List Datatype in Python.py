student_list = [ 'Sumit', 'Aman' , 'Priya', 'Rohit', 'Raman', 'Namita', 'Aman']
# To display list elements and type of the list object
print("Original Student List : ", student_list)  
print("Type of object : ", type(student_list))
# Accessing first element of list
print("First element in List : ", student_list[0])  
# To modify 2nd element of the list from "Aman" to "Aman Sharma"
student_list[1] = "Aman Sharma"
# Display updated list elements
print("Updated List : ", student_list)
# To create new list of students' marks using a list() class method
new_list = list([50, 45.5, 89, 72, 76.5, 49, 81])
print("Marks List : ", new_list)
