# Encapsulation and Data Hiding

class Product:

    def __init__(self, p, q, n):
        self.__maxSellingPrice = p  # Private data member
        self._quantity = q          # Protected data member
        self.name = n               # Public data member

    # getter method to return __maxSellingPrice
    def getMaxSellingPrice(self):
        return self.__maxSellingPrice

    # setter function to change __maxSellingPrice
    def setMaxSellingPrice(self, price):
        self.__maxSellingPrice = price


obj1 = Product(800, 10, "Commodity")
# Trying to change price outside class
obj1.__maxSellingPrice = 1050
print("The max selling price using direct : ", obj1.getMaxSellingPrice())

# Using setter function to change price
obj1.setMaxSellingPrice(1050)
print("The max selling price using setter : ", obj1.getMaxSellingPrice())

# Direct access protected data member
print('The quantity of product is :', obj1._quantity)
# Direct access public data member
print('The name of product is :', obj1.name)
