# Demonstrating Scope of variables in Python

def outer_func():  # Outer Function
    lvar = "local variable of outer_func()"
    global gvar
    gvar = "Global variable"
    print("Inside outer_func() lvar: ", lvar)
    def inner_func():  # Nested Function
        mvar = "Local variable of inner_func()"
        nonlocal lvar  # Declare mvar as nonlocal variable
        lvar = "NonLocal variable of inner_func()"  # Change lvar value
        print("Inside inner_func() lvar : ", lvar)
        print("Inside inner_func() gvar : ", gvar)
        print("Inside inner_func() mvar : ", mvar)
    inner_func() # Call inner_func()
    print("Inside outer_func() mvar: ", lvar)
    print("Inside outer_func() gvar: ", gvar)
    # print("Inside outer_func() mvar: ", mvar)   # mvar inaccessible
outer_func()
print("Outside outer_func() gvar: ", gvar)
# print("Outside outer_func() mvar: ", lvar) # It will raise an error: Error lvar inaccessible
# print("Outside outer_func() mvar: ", mvar) # It will raise an error: Error mvar inaccessible
