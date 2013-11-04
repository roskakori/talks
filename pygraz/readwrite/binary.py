'''
Examples to read and write binary files.
'''
import unittest

def writeBinary():
    targetPath = 'data.bin'
    with open(targetPath, 'wb') as targetFile:
        targetFile.write(bytes(range(16)))
        targetFile.write(bytes([17, 83, 194]))
        targetFile.write(b'some text bytes')


def readBinary():
    sourcePath = 'data.bin'
    with open(sourcePath, 'rb') as sourceFile:
        hasData = True
        while hasData:
            dataBlock = sourceFile.read(16)
            if dataBlock == b'':
                # Cause loop to finish.
                hasData = False
            else:
                print(dataBlock)


def readBinaryWithBreak():
    sourcePath = 'data.bin'
    with open(sourcePath, 'rb') as sourceFile:
        while True:
            dataBlock = sourceFile.read(16)
            if dataBlock == b'':
                # Terminate loop.
                break
            print(dataBlock)

    
class BinaryTest(unittest.TestCase):
    def testCanWriteBinary(self):
        writeBinary()

    def testCanReadBinary(self):
        readBinary()

    def testCanReadBinaryWithBreak(self):
        readBinaryWithBreak()


if __name__ == '__main__':
    unittest.main()
