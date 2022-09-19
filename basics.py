# here is a Python comment
a = 3 # integer
b = 7.2 # float
# primitive data types are int, float, boolean, None
print(a+b) # in Python 2 we can write print a+b
print(b/a) # also multiply *
print(b//a) 
print(b%a) # modulo - is the left over
print(b**a) # raise to the power

# variables do not have a fixed data type
a = 'hello' # string
b = True # or False

# collection data-types
c = 'this is a string of characters' # strings are immutable
# all indexed collections begin at zero
# c[0] = 'T' # nope - str does not support assignment
c = 'altered'
print(c[0]) # square brackets let us access a member of an indexed collection
d = "we can use single, double or tripple quotes"
e = '''tripple quotes let us use line breaks
like this so long lines can contain breaks'''
# other collection types
# lists are mutable indexed collections of any other type
my_list = [3, 2, 1] # square brackets indicte a list
my_list[1] = 'altered'
my_list.append(d)
print(my_list[1], my_list)
# tuples are immutable indexed collections of any other type
my_tuple = (8, 7, 6.3, False, a) # round brackets indicate a tuple
print(my_tuple[0])
# types
print(type(my_list), type(12.8), type(e), type(222), type(my_tuple[3]))
# we will look at casting data types and access members of collections
x = '42' # string
y = 4.2  # float
print( float(x) + y ) # 46.2
# we can receive input from the user
q = input('Please enter a number ') # we ALWAYS receive a str from input
q = int(float(q)) # take the int of the float of the str
print(q, type(q))