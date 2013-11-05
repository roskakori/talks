'''
Examples for reading and writing JavaScript object notation (JSON) files.
'''
import unittest

def writeJson():
    import json

    items = [
        'some text',
        17,
        123.45,
        ['red', 'green', 'blue'],
        {
            'Josef': '0664/1234567',
            'Paul': '0650/2345678',
            'Maria': '0699/9876543'
        }
    ]
    targetPath = 'items.json'
    with open(targetPath, 'w', encoding='utf-8') as targetFile:
        json.dump(items, targetFile)


def readJson():
    import json

    sourcePath = 'items.json'
    with open(sourcePath, 'r', encoding='utf-8') as sourceFile:
        items = json.load(sourceFile)
        # Print using Python's internal object representation.
        print(items)

        # Print using easier to read JSON format with indentation.
        print(json.dumps(items, indent=4))


class JsonTest(unittest.TestCase):
    def testCanWriteAndReadJson(self):
        writeJson()
        readJson()


if __name__ == '__main__':
    unittest.main()
