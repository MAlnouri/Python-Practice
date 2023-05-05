class Dog(object):

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def speak(self):
        # accesses the attribute of the object
        print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('bark')

'''
this a copy paste of the dog class, adding color attribute for cats

class Cat(object):

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
'''
'''
here Cat is inheriting from the dog class
dog is the parent class, cat is the child class

when you inherit from another class, you inherit all attributes/properties/methods of that class

'''
class Cat(Dog):

    def __init__(self, name, age, color):
        # when cat is initialized, we call to initialize dog first
        # sets the self.name,age of the object
        super().__init__(name, age)
        self.color = color
    
    '''
    override method
    anything done in our class overrides the properties from inheriting the dog class
    '''
    def talk(self):
        print('meow')

tim = Cat('tim', 5, 'orange')
# speak belongs to dog class but is inherited by the cat class so it can be called
tim.speak()
# meow instead of bark because cat class overrides the talk method
tim.talk()