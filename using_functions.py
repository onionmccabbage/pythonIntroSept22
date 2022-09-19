# we can import our own modules
import using_modules.table_f # runs any immediate code
import using_modules.table_w as web_mod # we can assign a short name

# from random import randint as ra 

# Python uses the keyword 'def' to define a function
def makeSquare(x=4): # we may optionally provide a default - overridden by any call
    return x*x

def hypot(x=3, y=4):
    h = (x**2 + y**2)**0.5 # anything raised to power of half is the square root
    return h

# in Python it is VERY common to write a 'main' function
def main(): # there is nothing special about the word 'main' here
    # we can call our function
    result = makeSquare() # call the function with the default value
    print(result)
    result = makeSquare(5) # call the function with a passeed-in value
    print(result)

    print(hypot(-3, -4))
    # every module will be given a name by Python
    print(__name__) # Python has many built-ins, including __name__
    # we can invoke methods from our imported modules
    furniture = using_modules.table_f.table(60, 50)
    web       = web_mod.table(4, 8) # use the short name
    print(furniture, web)

# we then invoke the 'main' method like this
if __name__ == '__main__':
    main()