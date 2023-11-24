# Operator Overloading

class Product:
    def __init__(self, qty, price):
        self.quantity = qty
        self.price = price

    def __lt__(self, obj2):   # overload < operator
        return self.price < obj2.price

    def __add__(self, obj2):   # overload < operator
        return self.quantity + obj2.quantity

prod1 = Product(5, 100)
prod2 = Product(7, 80)

print("Product-1 cheaper than product-2 : ", prod1 < prod2)  # prints False
print("Total products : ", prod1 + prod2)  # print sum of quantities
