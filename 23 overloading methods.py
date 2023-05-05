'''
function overloading
process where multiple functions of different types are defined with the same name
ex: 2 functions with same name, but execute different code
    based on the type of parameter recieved (int/str)
here we are overriding default python methods for our point class
default python methods have underscores: '__method__' simiilar to init
'''

class Point():
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    # method to add 2 points together by their x,y values
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    # method subtracts 2 points
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    # method multiplies 2 points to return scalar product
    def __mul__(self, p):
        return self.x * p.x + self.y * p.y
    
    # converts point object into string
    # run when print on object is called
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p5, p6, p7)