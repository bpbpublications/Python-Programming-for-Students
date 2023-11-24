# Demonstration  of  if-elif-else  statements  to  find  the correct  datatype  of  the  value  given  by  the user.
value1  =  (1,2,3,4)
print("Let  us  check  the  Datatype  of  value.....")
if  (type(value1)  ==  int):
	print("Type  of  the  variable  is  Integer")
elif  (type(value1)  ==  str):
	print("Type  of  the  variable  is  String")
elif  (type(value1)  ==  tuple):
	print("Type  of  the  variable  is  Tuple")
elif  (type(value1)  ==  dict):
        print("Type  of  the  variable  is  Dictionaries")
elif  (type(value1)  ==  list):
        print("Type  of  the  variable  is  List")
else:
        print("Type  of  the  variable  given  is  Undefined!!")
