# Non-Parameterized Constructor

class Product:
    quantity = 0
    color = 'None'
    
    # Constructor Type => Non-parameterized
    def __init__(self):
        print("Demo for Non-parametrized constructor")
        self.quantity = 10
        self.color = "Green"

    def display(self):
        print("The value of quantity : ", self.quantity)
        print("The value of color : ", self.color)

# Create object with non-parameterized constructor
obj1 = Product()
obj1.display()  # call display()
obj2 = Product()
obj2.display()  # call display()
