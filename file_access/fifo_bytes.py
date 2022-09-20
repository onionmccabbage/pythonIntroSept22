# Python can read and write byte files

b = bytes( range(0, 256) ) # 0-255 are the first 256 characters in UTC
# print(b)

# write to a byte file
def writeBytes(b):
    # we should use try-except here...
    fout = open('bfile', 'wb') # 'w' to (over)write 'b' for bytes
    fout.write(b)
    fout.close()

def readBytes():
    fin = open('bfile', 'rb') # 'r' to read 'b' for bytes
    r = fin.read()
    fin.close()
    print(r)


if __name__ == '__main__':
    writeBytes(b)
    readBytes()