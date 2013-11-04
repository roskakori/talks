'''
Examples for reading and writing text files.
'''
import unittest

def writeText():
    import os

    targetPath = 'wetterbericht.txt'
    with open(targetPath, 'w', encoding='utf-8') as targetFile:
        targetFile.write('Vorwiegend bewölkt, vom Süden böhiger Wind.' + os.linesep)
        targetFile.write('Die Temperaturen liegen zwischen 10 und 15 Grad' + os.linesep)
        targetFile.write('Die Schneefallgrenze steigt auf 2300 Meter.' + os.linesep)


def readText():
    sourcePath = 'wetterbericht.txt'
    with open(sourcePath, 'r', encoding='utf-8') as sourceFile:
        for line in sourceFile:
            line = line.rstrip('\n\r')  # Remove trailing linefeed characters
            print(line)


def readTextWithLineNumbers():
    lineNumber = 0
    sourcePath = 'wetterbericht.txt'
    with open(sourcePath, 'r', encoding='utf-8') as sourceFile:
        for lineNumber, line in enumerate(sourceFile, start=1):
            line = line.rstrip('\n\r')  # Remove trailing linefeed characters
            print('%(lineNumber)d: %(line)s' %
                  {'lineNumber': lineNumber, 'line': line})
    print('{0} line(s) read'.format(lineNumber))


class TextTest(unittest.TestCase):
    def testCanWriteText(self):
        writeText()

    def testCanReadText(self):
        readText()

    def testCanReadTextWithLineNumbers(self):
        readTextWithLineNumbers()


if __name__ == '__main__':
    unittest.main()
