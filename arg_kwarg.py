# functions can take arguments positionally or as keywords
def fn(x, y): # here the arguments are positional, x comes before y
    ''' raise the first argument to the power of the second argument'''
    return x**y

# here is a function that only expects positional arguments
def postitionalArg( *args ): # the asterisk tells python to expect positional arguments
    print(type(args), args) # the positional arguments exist in a tuple
    # we can act differently depending on how many arguments
    if len(args) == 0:
        print('function called with no arguments')
    elif len(args)==1:
        print('function called with a single argument')
    else:
        print('more than one argument passed in')

def keywordArgs( **kwargs ): # the double-asterisk indicates we expect keyword arguments
    print(type(kwargs)) # the keyword arguments are gathered into a dictionary
    for (k, v) in kwargs.items():
        print(k, v)

if __name__ == '__main__':
    result = fn(y=2,x=3) # here we pass the arguments as keywords (not positional)
    print(result)
    # exercise the positional arguments function
    postitionalArg()
    postitionalArg(3)
    postitionalArg(3, 2, 1, True, [], (), {})# we can pass as many or few positonal arguments as we like
    # exercise the keyword-arguments function
    keywordArgs(x=1)# a single keyword argument
    keywordArgs(y=2, z= True) # two keyword arguments
    keywordArgs(a=(5,4,3)) # a single keyword argument
