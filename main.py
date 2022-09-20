# here we ask the user for input then return the integer part of that input
from using_more_fn import makeInt


user_input = input('please type something: ')

# use our imported function to make an integer
user_int = makeInt(user_input)

print(user_int)
