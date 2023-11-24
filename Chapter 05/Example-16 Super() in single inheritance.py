# Super() in single inheritance

class Project:
    def project_name(self):
        return 'Software Development'

class Staff(Project):
    def display(self):
        # Calling the superclass method using super()function
        p_name = super().project_name()
        print("Current Project under work: ", p_name)

# Creating object of Staff class
obj1 = Staff()
obj1.display()
