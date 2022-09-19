# indentation
for i in range(0,6):
    print(i) # 4 spaces is pep-8 recoomended, but any consistent style will work

value = input('enter a value: ')
# is the string a numeric value?
if value.isnumeric(): # isnumeric is a function
    print('you entered a numeric string')
else:
    print('not numeric')
