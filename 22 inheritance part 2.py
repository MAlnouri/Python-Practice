'''
can inherit multiple times
the way you typically want to inherit
you want to have a general class that applies to different classes
for ex: vehicle class applies to different classes (cars/trucks)
'''

class Vehicle():

    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color
    
    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0
    
    def gasLeft(self):
        return self.gas
    
class Car(Vehicle):
    
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('beep beep')

class Truck(Vehicle):
    
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
    
    def beep(self):
        print('honk honk')