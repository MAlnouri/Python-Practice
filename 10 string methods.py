# .strip()
# removes leading/trailing white spaces from string (spaces at front and end of string)
s = '   TESTing something'
print(s)
print(s.strip())

# len()
# len is actually a function not a method (uses len() instead of .len())
# returns length of a container object (string/list)
print(len(s))

# .lower()
# returns string in all lowercase
print(s.lower())

# .upper()
# returns string in all uppercase
print(s.upper())

# .split()
# creates list out of a string
# uses delimeter argument to split the string
splitstring = 'hello.this.is.a.test of.split'
print(splitstring.split('.'))
# by default, splits by spaces
defaultsplit = 'testing a default split'
print(defaultsplit.split())