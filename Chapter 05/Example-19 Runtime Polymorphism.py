# Runtime Polymorphism

class Staff():
    def calculate(self):  # Parent class
        print("Inside calculate() of Staff")
    def display(self):
        print("Inside display() of Staff")

class Developer():  # Parent class
    def calculate(self):  # Parent class
        print("Inside calculate() of Developer")
    def display(self):
        print("Inside display() of Developer")

class PythonExpert(Staff, Developer): # Defining child class
    def display(self):  # Child's display method
        print("Inside display() of PythonExpert")

obj = PythonExpert() # Driver's code
obj.display()
obj.calculate()
print(PythonExpert.mro())
