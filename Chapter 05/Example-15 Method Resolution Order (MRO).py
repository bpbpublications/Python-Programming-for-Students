# Method Resolution Order (MRO) Demo

class First:
    def __init__(self):
        print("In First class")
        super().__init__()  # In MRO hierarchy call __init__()

class Second(First):
    def __init__(self):
        print("In Second class")  # In MRO hierarchy call __init__()
        super().__init__()

class Third(Second):
    def __init__(self):
        print("In Third class")
        super().__init__()

obj1 = Third()
print(Third.__mro__)
