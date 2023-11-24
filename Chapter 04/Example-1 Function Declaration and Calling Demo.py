# Declare a function to print welcome message
def welcomeMessage(name):
    username = name
    if username:
        print("Welcome " + str(username) + "!!")
    else:
        print("Welcome Guest!!")
    return
# Calling welcomeMessage() function to execute
# Passing name variable as argument in function
name = input("Enter your name: ")
welcomeMessage(name)
