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
    sourcePath = 'wetterbericht.txt'
    lineNumber = 0
    with open(sourcePath, 'r', encoding='utf-8') as sourceFile:
        for lineNumber, line in enumerate(sourceFile, start=1):
            line = line.rstrip('\n\r')  # Remove trailing linefeed characters
            print('{}: {}'.format(lineNumber, line))
    print('{} line(s) read'.format(lineNumber))


class TextTest(unittest.TestCase):
    def testCanWriteAndReadText(self):
        writeText()
        readText()
        readTextWithLineNumbers()


if __name__ == '__main__':
    unittest.main()
