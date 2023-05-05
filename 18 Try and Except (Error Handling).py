'''
Try and Except keywords
'''

text = input('username:')

# trys to execute after input is recieved
try:
    number = int(text)
    print(number)
# executes if try statement returns an error
except:
    print('invalid')