# indentation
for i in range(0,6):
    print(i) # 4 spaces is pep-8 recoomended, but any consistent style will work

value = input('enter a value: ')
# is the string a numeric value?
if value.isnumeric(): # isnumeric is a function
    print('you entered a numeric string')
else:
    print('not numeric')

# By reference and by value
a = 9
b = a # both a and b reference the value 9 (by value - they take the same value)
print(b)
b = 8
print(a) # what is the value of a? It still refers to the memory location containing the integer value 9

# what about complex data types - passed by reference (they refer to the same thing)
a = [6,5,4]
b = a # both b and a are identifiers which reference the memory location containing the list
print(b) # yep they are the same
b[0] = -6
print(a[0]) # what is this value?

# how big can python go?
# bign = 10**1000000

# print(bign)

# global scope and local scope
g = 'this is in the global scope'
# we tend to try to avoid putting anything in the global scope

def myFn():
    global g # this now refers to the 'g' in the global scope
    g = 'this is in the local scope of a function'
    print(g)
myFn()
print(g)