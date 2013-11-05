'''
Examples for reading and writing comma separated value (CSV) files.
'''
import unittest

def writeCsv():
    import csv

    targetCsvPath = 'personen.csv'
    with open(targetCsvPath, 'w', newline='', encoding='utf-8') as targetCsvFile:
        csvWriter = csv.writer(targetCsvFile, delimiter=';')
        csvWriter.writerow(['Vorname', 'Nachname', 'Geburtsdatum', 'Gewicht'])
        csvWriter.writerow(['Josef', 'Huber', '1981-02-27', 76.3])
        csvWriter.writerow(['Paul', 'Müller', '1967-05-18', 64.8])
        csvWriter.writerow(['Maria', 'Schäfer', '1976-10-08', 82.5])


def readCsv():
    import csv

    sourceCsvPath = 'personen.csv'
    with open(sourceCsvPath, 'r', encoding='utf-8') as sourceCsvFile:
        for row in csv.reader(sourceCsvFile, delimiter=';'):
            print(row)


def readAndValidateCsv():
    import csv
    import datetime

    EXPECTED_COLUMN_COUNT = 4

    sourceCsvPath = 'personen.csv'
    rowNumber = 0
    columnNumber = 0
    row = None
    with open(sourceCsvPath, 'r', encoding='utf-8') as sourceCsvFile:
        csvReader = csv.reader(sourceCsvFile, delimiter=';')
        try:
            for rowNumber, row in enumerate(csvReader, start=1):
                if rowNumber > 1:  # Skip header row.
                    columnNumber = 1
                    if len(row) != EXPECTED_COLUMN_COUNT:
                        raise ValueError('row must have {} columns but is: {}'.format(
                                EXPECTED_COLUMN_COUNT, row))
                    firstName, surName, dateOfBirthText, weightText = row
                    columnNumber = 3
                    dateOfBirth = datetime.datetime.strptime(dateOfBirthText, '%Y-%m-%d')
                    columnNumber = 4
                    weight = float(weightText)
                    print(firstName, surName, dateOfBirth, weight)
        except ValueError as error:
            raise ValueError('{} ({}, {}): {}'.format(sourceCsvPath, rowNumber, columnNumber, error))


class CsvTest(unittest.TestCase):
    def testCanWriteAndReadCsv(self):
        writeCsv()
        readCsv()
        readAndValidateCsv()


if __name__ == '__main__':
    unittest.main()
