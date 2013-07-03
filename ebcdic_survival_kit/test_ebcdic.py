'''
Example to read EBCDIC.
'''
import os

with open('some.txt', 'wb'):
    # Create an empty test file.
    pass

try:
    import codecs
    
    with codecs.open('some.txt', 'r', 'cp500') as dataFile:
        for line in dataFile:
            print(line)
    
    # Note: This will fail with Python 2.7.
    with codecs.open('some.txt', 'r', 'cp1141') as dataFile:
        for line in dataFile:
            print(line)
finally:
    os.remove('some.txt')