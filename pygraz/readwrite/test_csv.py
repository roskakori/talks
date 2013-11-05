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

    sourceCsvPath = 'personen.csv'
    with open(sourceCsvPath, 'r', encoding='utf-8') as sourceCsvFile:
        csvReader = csv.reader(sourceCsvFile, delimiter=';')
        for rowNumber, row in enumerate(csvReader, start=1):
            if len(row) != 3:
                message = 'row {} in CSV file {} must have 4 columns but is: {}'.format(
                    rowNumber, sourceCsvPath, row)
                raise ValueError(message)
            firstName, surName, dateOfBirthText, weightText = row
            dateOfBirth = datetime.datetime.strptime(dateOfBirthText, '%Y-%m-%d')
            weight = float(weightText)
            print(firstName, surName, dateOfBirth, weight)


class CsvTest(unittest.TestCase):
    def testCanWriteAndReadCsv(self):
        writeCsv()
        readCsv()
        readAndValidateCsv()


if __name__ == '__main__':
    unittest.main()
