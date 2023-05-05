'''
global = a variable that anything in the program can see
local = specific to block of code or class
'''

# global variables
var = 9
loop = True

def test(x):
    newVar = 7
    
    if x == 5:
        return newVar
    
# newVar is a local variable to test function
# cannot be used/accessed outside of the function
# print(newVar)

def test2():
    # this does not change the global varialbe
    # creates new instance variable with same name
    var = 3
    print(var)
    # use keyword global to access global variables
    global loop
    # then we can modify it
    loop = False

# test 2 function prints 3 (value of local variable instead of global)
# prefers 
test2()

print(loop)