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

def fileWrite(t='default'):
    '''this will write chunks of text to an output file'''
    try:
        fout   = open('mylog.txt', 'at')
        size   = len(t)
        offset = 0
        chunk  = 24 # I choose to write 24 characters at a time
        while True:
            if offset > size:
                fout.write('\n') #append a new line character
                break
            else:
                fout.write(t[offset:offset+chunk]) # [start:stop-before]
                offset += chunk
        fout.close()
    except FileExistsError as fe:
        print('The file already exists {}'.format(fe))
    finally:
        print('all done')

def fileRead():
    with open('mylog.txt', 'rt') as fin:
        retrieved = fin.readlines() # readlines will read the whole thing as a list of lines
        print(retrieved)

def main():
    simpleOutput()
    simpleInput()
    fileWrite('this is a long piece of text that will be written in chinks of 24 characters to the log file')
    fileRead()

if __name__ == '__main__':
    main()