# Super() in multiple inheritance

class First:
    def __init__(self, num):
        print("In First class num = ", num)
        # In MRO hierarchy call __init__() of class Second
        super().__init__(num+10)

class Second:
    def __init__(self, num):
        print("In Second class num = ", num)
        # In MRO hierarchy call __init__() of object class
        super().__init__()

class Third(First, Second):
    def __init__(self, num):
        print("Starting in class Third num = ", num)
        super().__init__(num+10)
        print("Back in Third class num = ", num)

obj1 = Third(10)
print(Third.__mro__)
