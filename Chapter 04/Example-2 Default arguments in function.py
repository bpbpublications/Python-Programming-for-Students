# Demonstrating the usage of default arguments:

def enterDetails(age, username = 'Guest'):
    print("Your entered details are : ")
    print("User Name is: ", username)
    print("User Age is: ", age)
# Calling the function and passing only one argument
enterDetails(25) # Default value of username used
# Calling the function and passing both the arguments
enterDetails(30, "Michael")
