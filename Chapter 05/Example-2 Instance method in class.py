# Instance Method in Python class

class Department:
    def __init__(self, dept_id, dname):
        self.dept_id = dept_id  # Instance variable
        self.dept_name = dname  # Instance variable

    # Instance method display() to access instance variable
    def display(self):
        print('DeptID:', self.dept_id, 'Dept Name:', self.dept_name)

    # Instance method to modify instance variable and add new
    def edit(self, dname, dmgr):
        self.dept_name = dname
        self.manager = dmgr # add new attribute to current object

obj1 = Department(1001, "Marketing")   # Create object obj1
obj1.display()  # Call instance method
new_dept_name = input('Enter new Department name')
new_mgr_name = input('Enter Manager name to update')
# call edit() to update instance variable dept_name and add manager
obj1.edit(new_dept_name, new_mgr_name)
print("**** Updated Details ****")
print("Dept ID : ", obj1.dept_id)
print("Dept Name : ", obj1.dept_name)
print("Manager Name : ", obj1.manager)
