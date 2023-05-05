
# setting text parameter as 7 creates a default for the optional parameter
def func(x, text='7'):
    print(x)
    if text == '1':
        print('one')
    else:
        print(text)

func('hello', '67')

# cannot change the 2nd optional parameter without setting the first
def func2(x='1', text='test'):
    print(x, text)
func('9', 'cannot')