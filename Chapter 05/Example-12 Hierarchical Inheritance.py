# Hierarchical Inheritance

class Parent:       # Base class
    def base_info(self):
        print('Inside Parent class method')

class FirstChild(Parent):  # First Child class of Parent
    def first_child_info(self):
        print('Inside First Child class method')

class SecondChild(Parent):  # Second Child class of Parent
    def sec_child_info(self):
        print('Inside Second Child class method')

# Create object of Child classes
obj1 = FirstChild()
obj2 = SecondChild()
# Access Parent class info Child class object
obj1.base_info()
obj1.first_child_info()
obj2.base_info()
obj2.sec_child_info()
