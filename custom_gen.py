# generators are built in to Python
my_gen = (num for num in range(0, 100, 5))
# we use the generator to yield values as we need them
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())

# functions can return a single value
def normalFn():
    return 'normal functions can only return ONCE'

# we can write our own generator functions to yield values repeatedly
def genSquares(n=0, stop=10, step=1):
    '''
    Generate the squares of numbers from n to stop every step
    '''
    number = n
    stop_at = stop
    while number < stop_at:
        number += step
        yield number**2 # yield instead of return

if __name__ == '__main__':
    # we need an instance of the generator
    g = genSquares()
    # how many members in our cutom generator?
    print('There are {} members in the generator'.format(len(list(genSquares()))))
    # g = genSquares(-10, 100, 10) # we could override the defaults
    print(g.__next__()) # 1
    print(g.__next__()) # 4
    print(g.__next__()) # 9
    # we can iterate over a custom generator
    for x in g:
        print(x, end=', ')
        # when all the values have been yielded, the generator is exhausted
    # print(g.__next__()) # nothing left to yield
    