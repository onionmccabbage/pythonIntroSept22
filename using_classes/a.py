# use the built-in structures when they meet your need
person1 = {'n':'Ada', 'a':42}

# if the built in structures don't suit your purpose then you write a class
class Person(): # unless we say otherwise, the class inherits from 'object'
    '''
    You can explain your class in a docstring
    This class encapsulates a 'Person'
    Parameters: name, age and email
    'age' must be a positive integer
    '''
    # every method of a class MUST take 'self' as a parameter
    # 'self' refers the class itself - similar to 'this' in other languages
    def __init__(self, n, a, e): # this is similar to a constructor
        self.__name  = n
        self.__age   = a # name mangling - this means we CANNOT access __age from class instances
        self.email = e
    # we can declare methods of this class as functions
    def setAge(self, new_age):
        if int(float(new_age)) > 0:
            self.__age = new_age
        else:
            self.__age = 42
    def getAge(self):
        return self.__age # we can only access 'mangled' members from within the class itself
    def setName(self, new_name): # mutator method ('setter')
        if type(new_name) == str and new_name != '':
            self.__name = new_name # we only set the property when we are sure it is valid
        else:
            self.__name = 'Default'
    def getName(self): # accessor method ('getter')
        return self.__name
    # we can write our own print method
    def __str__(self): # the __str__ method is ALWAYS used by the print statement
        return '{} age {} email {}'.format(self.__name, self.__age, self.email)

if __name__=='__main__':
    # we can create instances of our class
    ada = Person('Ada', 42, 'ada@babbage.co.uk') # Python does not use the 'new' keyword
    # mutate the 'age' of this instance
    ada.setAge(99)
    ada.__age = -3 # this is just some arbitrary property - NOT the actual age
    print(ada.getName(), ada.getAge(), ada.__age)
    print(ada)