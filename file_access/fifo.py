# file input and file output (fifo)

def simpleOutput():
    '''
    Python uses File Access Objects
    If a File Access Object points to a non-existant file
    then Python will create the file, so long as we 'append' '''
    # 'w' will (over)write the file. 'a' will append. 
    # 'x' is exclusive access (fails if the file already exists)
    try: #   by default Python writes text. We can specify this with 't'
        fout = open('output.txt', 'at') # fout is now our File Access Object. 'a' means append
        print('here is some content', file=fout)
        fout.close() # we must tidy up!
    except Exception as err:
        print(err)
    finally:
        pass
def simpleInput(): # read back from a text file    
    try:
        # 'r' means read 't' means text
        fin = open('output.txt', 'rt')
        received = fin.read() # read the whole thing
        print(received)
        fin.close()
    except Exception as err:
        print(err)
    finally:
        pass
def main():
    simpleOutput()
    simpleInput()

if __name__ == '__main__':
    main()