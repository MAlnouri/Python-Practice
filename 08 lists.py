'''
list is a data type
list is a collection of data types, can be same or different data types
lists are 0 indexed
lists are useful for storing large amounts of information

tuple is another data type
used for coordinates
also used for colors and rectangles
can also be used to hold data
'''

fruits = ['apple', 'pear', 'orange', 5]
print(fruits)

# print item at index of list
print(fruits[1])

# add to list end of list
fruits.append('watermelon')

# modify indexed item
fruits[1] = 'strawberry'

print(fruits)

# tuples
position = (2, 3)
color = (255, 255, 255)
# type returns the data type of the argument
print(type(color))