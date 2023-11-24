# Static method in python class

class Department:
    # Define static method in class
    @staticmethod
    def staticmethod1(num):
        print('Inside static method num is : ', num)

    # Define instance method and call static method from inside
    def method2(self):
        print('Inside instance method....')
        print('Calling static method..')
        self.staticmethod1(202)

# Call static method using class name
Department.staticmethod1(101)
# Call instance method using class object
d1 = Department()
d1.method2()
