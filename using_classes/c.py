# modern Python provides 'decorator' syntax for use in classes
# This allows methods to behave like properties

class Todo(object):
    '''
    Encapsulate the id, userId, title and completed of a 'Todo' item
    the title and completed will be mutable
    '''
    def __init__(self, id, userId, title, completed):
        self.id        = id
        self.userId    = userId
        self.title     = title # here we call the 'title' setter method
        self.completed = completed
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.userId, self.title, self.completed) # inject the actual values from this class
    # we can use 'decorator' syntax to declare getter and setter methods
    @property # this is a getter method
    def title(self):
        return self.__title
    @title.setter # this is a setter method
    def title(self, new_title):
        if type(new_title)==str and new_title != '':
            self.__title = new_title
    @property
    def completed(self):
        return self.__completed
    @completed.setter
    def completed(self, status):
        if type(status) == bool:
            self.__completed = status
        else:
            raise Exception # raise an exception because the value is not a boolean

if __name__ == '__main__':
    job1 = Todo(1, 2, 'write a class', False)
    job1.title = 'learn Python' # this will call the 'setter' method for 'title'
    job1.completed = True # this will work fine
    job1.completed = 'wrong' # this will raise an exception
    print(job1)
    print(job1.title) # here 'title' looks like a property - but it calls the getter method