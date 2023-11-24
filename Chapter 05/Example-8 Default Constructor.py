# Default Constructor

class Product:
    quantity = 0
    color = 'None'
    
    # No user defined constructor given
    def display(self):
        print("The value of quantity : ", self.quantity)
        print("The value of color : ", self.color)

obj = Product()
obj.display()
