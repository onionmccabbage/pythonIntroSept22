# its always a good idea to test each unit of code
import doctest

def cube(x):
    '''This function will take a number 
    and return the cube
    >>> cube(3)
    27
    >>> cube(-3)
    -27
    '''
    return x**3

if __name__ == '__main__': # only run the tests if this is the main module (not if imported elsewhere)
    print( cube(-2) ) # -8
    # we run unit tests liek this
    doctest.testmod(verbose=True) # always show test results 