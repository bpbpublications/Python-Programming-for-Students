# Built-in attributes in python class

class Project:
    """This class contains current project details"""
    def __init__(self, name, id, duration):
        self.pname = name
        self.pid = id
        self.duration = duration

    def display(self):
        print("Name: %s, ID: %d, Duration: %d " %(self.pname, self.pid, self.duration))

proj1 = Project("Website", 1001, 180)
print("proj1.__doc__    => ", proj1.__doc__)
print("proj1.__dict__   =>", proj1.__dict__)
print("proj1.__module__ =>", proj1.__module__)
print("proj1.__class__  =>", proj1.__class__)
