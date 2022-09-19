# Python has several built-in libraries
# import random # this iports the entire 'random' library
from random import randint # this import only the 'randint' member from the 'random' library

for i in range(1, 100):
    # r = random.randint(-10, 10) # use this syntax when the whole library was imported
    r = randint(-10, 10) # use this syntax if you have imported just a member from a library
    print(r, end=', ')
