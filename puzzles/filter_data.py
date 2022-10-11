import csv
from random import randint

with open('novice.csv', 'r') as f:
    fout = open('test.csv', 'w')
    reader = list(csv.reader(f))
    header = reader[0]
    writer = csv.writer(fout)
    writer.writerow(header)
    counter = 0
    for i in range(1):
        counter += 1
        id = randint(1, len(reader) - 1)
        row = reader[id]
        row[0] = counter
        writer.writerow(row)
