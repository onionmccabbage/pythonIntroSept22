# What is __name__ and __main__
# function parameters, args and keyword args
# unit testing

def makeInt(value): # document your code using '''docstring'''
    '''This function will take a value and return the integer part
    If the value is not numeric, a default integer will be returned
    For example, if 1.23 is passed in, we return 1
    If -3.2 is passed in we return -3
    If any other string, list tuple etc. is passed in we return 0'''
    # here are some sets of data types
    simple = {int, float, bool}
    comp   = {list, tuple, dict, set}
    # check if the value is numeric or if it is a plain numeric string value
    # if type(value)==list or type(value)==tuple or type(value)==dict:
    if type(value) in comp:
        return 0
    # careful - simple data types have no 'isintance' method, so use 'type'
    # if type(value)==int or type(value)==float or value.isnumeric():
    if type(value) in simple or value.isnumeric:
        return int(float(value))
    else:
        return 0 # careful - at the moment this will also return 0 for decimal strings

# exercise the code
my_int = 3
my_float = 4.5
my_str = '6'
my_list = [8,7,6]
print(makeInt(my_int))
print(makeInt(my_float))
print(makeInt(my_str))
print(makeInt(my_list))



