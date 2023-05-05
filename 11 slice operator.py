fruits = ['apple', 'pear', 'orange']
text = 'hello i like python'

# can access chars in a string using indexes like a list
print(text[1])

# slice operator
# [::] using 2 colons, start stop and step similar to range function
# [start:stop:step]
# default start = 0, stop = end (inclusive), step = 1
print(text[::2])

# insert using slice
fruits[1:1] = 'b'
print(fruits)

# using -1 as step reverses the string
# starts from end and stops at beginning
print(text[::-1])