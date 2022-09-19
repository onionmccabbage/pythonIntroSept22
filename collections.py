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