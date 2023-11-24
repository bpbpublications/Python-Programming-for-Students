# Usage of instance and class variables in Class 

class Department:
    location = 'None'  # Class variable ‘location’

    def __init__(self, dname, dmgr):  # constructor
        self.dname = dname   # Instance variable dname 
        self.manager = dmgr  # Instance variable manager
        Department.location = "India" # Class variable location 
        
    # Instance method display()
    def display(self):
        print('Inside instance method display()')
        # To access using all variables using self
        print(self.dname, self.manager, self.location)
        # To access class variable using class name
        print(Department.location)

# Now create objects d1 and d2
d1 = Department("Marketing", "Raman")
d2 = Department("Finance", "Anil")
# To access instance variable and class variable using object
print('**** Details of First Object ****')
print('Name -> ', d1.dname, ', Manager ->', d1.manager)
print('Location : ', d1.location)
d1.display()
print('**** Details of Second Object ****')
# To access instance variable using getattr() 
print('Name -> ', getattr(d2, 'dname'))
print('Manager ->', getattr(d2, 'manager'))
# Access class variable using class name
print('Location : ', Department.location)  
d2.display()
