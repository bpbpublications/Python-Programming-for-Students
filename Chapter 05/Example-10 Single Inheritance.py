# Single Inheritance

class Parent:       # Base class
    def base_info(self):
        print('Inside Base class method')

class Child(Parent):  # Child class
    def child_info(self):
        print('Inside Child class method')

# Create object of Child class
obj1 = Child()

# Access Parent class info Child class object
obj1.base_info()
obj1.child_info()
