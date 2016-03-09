import csv
import os.path

csv_path = os.path.join('examples', 'persons.csv')
with open(csv_path, 'r', encoding='utf-8', newline='') as csv_file:
    for items in csv.reader(csv_file, delimiter=';'):
        print(items)
