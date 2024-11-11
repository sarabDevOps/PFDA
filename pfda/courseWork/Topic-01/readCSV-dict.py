# Author - Sarabjeet Kumar
#Read CSV as a dictionary

import csv

FILENAME = "data.csv"
DATADIR = "../Topic-01/"

with open(DATADIR + FILENAME , "rt") as fp:
    reader = csv.DictReader(fp,delimiter="," , quoting=csv.QUOTE_ALL)
    total = 0
    for line in reader:
            total += int(line['id'])
            print(line)
