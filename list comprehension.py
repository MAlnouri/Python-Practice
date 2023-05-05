# convert basic for loop into list comprehension
fruits = ['apples', 'bananas', 'strawberries']
'''
for fruit in fruits:
    print(fruit)
'''
# converts basic for loop to print
[ print(f) for f in fruits ]

'''
new_fruits = []
for fruit in fruits:
    fruit = fruit.upper()
    new_fruits.append(fruit)
'''
# converts each element to all uppercase
[ fruit.upper() for fruit in fruits ]


# list of booleans to represent bits
bits = [False, True, False, True, True, False]
'''
new_bits = []
for b in bits:
    if b == True:
        new_bits.append(1)...
'''
# b is a boolean value
new_bits = [ 1 if b else 0 for b in bits ]
print(new_bits)
# booleans can also be converted to integers using int()
print(int(False))
print(int(True))


'''
String manipulation
Pascalcase/Uppercamelcase = no spaces, uppercase indicates new word
'''

mystring = "HelloMyNameIsBob"
# converts string into a list
# mystring = [ i for i in mystring ]
# joins string from list separating by uppercase chars, [1:] slices to remove first empty space
mystring = "".join([ char if char.islower() else " " + char for char in mystring ])[1:]
print(mystring)
'''
cannot use elif keyword in list comprehension
else action condition
'''
mystring = "".join(
    [ char if char.islower()
      # special else statement
      else " " + char.lower() if char in ['N', 'I']
      else " " + char
      for char in mystring ]
    )[1:]
print(mystring)

# reverse string
s = "thisisateststring"
print(s[::-1])