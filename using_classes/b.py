# we can import our class then extend it using inheritance
from a import Person

# a Coder is a person that has a 'language' parameter
class Coder(Person):
    def __init__(self, n, a, e, l):
        super().__init__(n, a, e) # call the __init__ method of the parent
        self.__language = l
    def __str__(self):
        s = super().__str__()
        s += ' {} codes in {}'.format(self.getName(), self.__language)
        return s

if __name__ == '__main__':
    timnit = Coder('Timnit', 32, 'timnit@nasa.ie', 'Python')
    print(timnit)

    import this