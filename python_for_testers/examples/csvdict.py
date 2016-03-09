import csv
import os.path

csv_path = os.path.join('examples', 'persons.csv')
with open(csv_path, 'r', encoding='utf-8', newline='') as csv_file:
    for person in csv.DictReader(csv_file, delimiter=';'):
        print(person)
