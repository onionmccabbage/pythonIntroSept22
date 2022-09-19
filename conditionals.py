# we can carry out operations based on conditional logic
s = 'text'
if type(s) == str:
    print('its a string')
elif type(s) == int:
    print('its an integer')
else:
    print('not a string')
# see if a number is odd or even
# also see if the number is within a certain range
t = (1,2,3,5,7,11) # primes
q = input('Enter a number ')
q = int(float(q)) # always good to cast
if q/2 == q//2: # double-equals CHECKS equality (single equals SETS equality)
    print('its an even number') 
elif q in t: # the 'in' operator checks a value for existance in a collection
    print('its a prime number')
else:
    print('its an odd number')

# the while loop: cautiom - make sure you can break out of it!!!!
while True:
    print('this will never end')
    a = input('is it lunch yet? ')
    if a == 'yes' or a == 'si': # we can also use 'and'
        break # this breaks out of the loop
