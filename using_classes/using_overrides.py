# we can override many of the built-in features of Python
# we already saw __str__ to override print

class Word():
    '''
    This class overrides the equality operator so it ignores case
    '''
    def __init__(self, text):
        self.text = text
    # here we override '=='
    def __eq__(self, other_word):
        return self.text.lower() == other_word.text.lower()

# use with great care!!!!!!
# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    # currently
    w1 = 'lunch'
    w2 = 'Lunch'
    print(w1 == w2) # False
    w3 = Word('lunch')
    w4 = Word('Lunch')
    print(w3 == w4) # True - our __eq__ method decides what equality means

    # we can access some of the intrinsic parts of our class
    print(Word.__doc__)