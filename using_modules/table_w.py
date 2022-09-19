# this encapsulates a web table
def table(rows, columns):
    t = {'rows':rows, 'columns':columns}
    return t

# careful - immediate code ALWAYS runs on import
# we can see the name of this module when imported...
print(__name__)
if __name__ == '__main__':
    trial = table(3,4)
    print('inside furniture module', trial)