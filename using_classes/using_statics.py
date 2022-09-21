# statics and class methods belong to the class not to any instance of the class

class Duck():
    count = 0 # this property belongs to the class, not to any particular instance
    def __init__(self, n):
        self.name = n
        Duck.count += 1 # increment the count every time an instance is created
    # we can expose the 'count' property through a class method
    @classmethod # class methods do NOT take self
    def numDucks(cls): # by convention we use 'cls' to represent the current class
        return cls.count
    # we can declare static methods like this
    @staticmethod
    def promo(): # no self, no cls...
        return ' this promotional content will encourage the purchase of ducks'

if __name__ == '__main__':
    # we can call static methods even if there are NO instances
    print(Duck.promo())
    donald = Duck('Donald')
    howard = Duck('Howard')
    ella   = Duck('Ella')
    print(Duck.numDucks()) # or Duck.count