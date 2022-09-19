# Python includes a 'generator' object

def main():
    # range
    r = range(0, 22, 3)
    # list
    num_l = [num for num in range(0, 100, 5)] # square brackets return a list in memory
    # generator
    num_g = (num for num in range(0, 100, 5)) # round brackets return a GENERATOR object
    print(r, type(r))
    print(num_l, type(num_l)) # we have a list
    print(num_g, type(num_g)) # we have a generator
    # use the generator to generate values on demand
    print(num_g.__next__()) # 0 is yielded
    print(num_g.__next__()) # 5 is yielded as the next member from the generator
    # we can use a loop to yield the next members of our generator
    for item in num_g:
        print(item, end=', ') # keeps looping until the generator is exhausted

    # we can comprehensively deal with each member of a dictionary
    p = 'are we done yet?'
    chars = {letter:p.count(letter) for letter in p} # this is called dictionary comprehension
    print(chars)


if __name__ == '__main__':
    main()