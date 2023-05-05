'''
in classes there are attributes and methods
methods are created using def (look like functions, except they must be called using an object)
attributes are variables that belong to an object
'''

class Dog(object):

    # constructor method of the class
    # runs anytime you create a new dog object
    def __init__(self, name, age):
        # to create an attribute, must use self keyword
        self.name = name
        self.age = age

    def speak(self):
        # accesses the attribute of the object
        print('my name is ' + self.name + ' and my age: ' + str(self.age))

    # you can add/create an attribute outside of the constructor
    def add_weight(self, weight):
        self.weight = weight

tim = Dog('tim', 19)
fred = Dog('fred', 10)
tim.speak()
fred.speak()
print(tim.age)
tim.add_weight(70)
print(tim.weight)