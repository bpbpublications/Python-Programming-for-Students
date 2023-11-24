class Parent:       # Base class
    def base_info(self):
        print('Inside Parent class method')

class Child1(Parent):  # Child class of Parent
    def child1_info(self):
        print('Inside Child1 class method')

class Child2(Child1):  # Child class of Child1
    def child2_info(self):
        print('Inside Child2 class method')

# Create object of Child2 class
obj1 = Child2()

# Access Parent class info Child class object
obj1.base_info()
obj1.child1_info()
obj1.child2_info()
