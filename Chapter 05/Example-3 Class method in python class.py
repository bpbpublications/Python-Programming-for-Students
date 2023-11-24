# Class method in a python class

class Department:
    location = 'None'  # class variable for dept location

    def __init__(self, dname, dmgr):
        self.dname = dname
        self.manager = dmgr

    # Define class method to change dept_loc
    @classmethod
    def change_loc(cls, new_loc):
        # class_name.class_variable
        cls.location = new_loc

    # Instance method to display()
    def display(self):
        print('Department: ', self.dname, ',Manager:', self.manager)
        print('Location:', Department.location)

obj1 = Department('Sales', 'Kartik Kumar')
obj1.display()
# To update department location
new_loc = input("Enter dept location to update")
Department.change_loc(new_loc)
obj1.display()
