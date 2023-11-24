# Parameterized Constructor

class Product:
    quantity = 0
    color = 'None'
    
   # Constructor Type => Parameterized
    def __init__(self, qty, clr):
        print("Demo for parametrized constructor")
        self.quantity = qty
        self.color = clr

    def display(self):
        print("The value of quantity : ", self.quantity)
        print("The value of color : ", self.color)

obj1 = Product(10, 'Red')  # First Object created with parameters
obj1.display()
obj2 = Product(7, 'Blue')  # Second Object created with parameters
obj2.display()
