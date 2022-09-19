# here we explore collections and accessing indexed members
l = [3, True, 'ciao', None, [8,7,6]]
# we can access indexed members
print(l[4][2])
# we can ccess several members
print(l[1:4]) # start at member 1 stop-before member 4
# remember strings are indexed collections
s = 'here is a rather long string'
print(s[5:22:3]) # start:stop-before:step
# same is true for a tuple
t = (l, s, False, [4,3,2], (999,888,777), 3.2, 0.00009)
print(t[0:5:2])

# iterating over a collection
# Python has a 'range' object: start, stop-before, step
for i in range(0, 10, 3): # the colon indicates the start of a code block
    print(i) # every line of a code block is indented
# when the indentation ends, that is the end of the current code block
# for example we may need to populate a tuple with a bunch of numbers
odds = tuple( range(1, 100, 2) )
# odds = ( range(1, 100, 2), ) # the comma makes this a single-member tuple
print(type(odds), odds)
evens = list( range(0, 101, 2) )
print(type(evens), evens)
# we can iterate over tuples, lists and strings
for i in odds:
    print(i, end=' ') # the space will be appended to each print
for i in evens:
    print(i, end=', ')
for i in 'this is a string of characters':
    print(i, end='-')

# Non-indexed collections: the dictionary collection is NOT indexed by number (it is mutable)
d1 = {"name":"Timnit", 'age':42,  'member':True}
d2 = {'name':'Grace' , 'age':82,  'member':True}
d3 = {'name':'Ada'   , 'age':142, 'member':False}

# we can access members of a dictionary by the keys
d1['name'] = 'Gebru'
print(d1['name'], d3['member'], d2['age'])
# we can access all keys and all values
print(d1.keys(), d2.values())
# we can add to dictionary members
d1['famous'] = True

# we can access all members of a dict in a loop
for (k, v) in d1.items():
    print(k, v) # careful - there is no predictable order to the members

# other creational techniques
w = dict() # an empty dictionary
# careful - if we need a one-member tuple, we must include a comma
z =(7,) # a tuple

# there is also a data-type called 'set' - a colection of non-indexed unique values
s = {7, 6, 5, 4, 7, 3, 2, 5} # only unique members survive
s.add(0)
print(s)