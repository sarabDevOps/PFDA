# Author - Sarabjeet Kumar

import csv

FILENAME = "data.csv"
DATADIR = "../Topic-01/"

with open(DATADIR + FILENAME , "rt") as fp:
    reader = csv.reader(fp,delimiter="," , quoting=csv.QUOTE_ALL)
    lineCount =  0
    total = 0
    for line in reader:
        if not lineCount:
            # first row
            print(f"{line}\n--------------")
        else:
            total +=int(line[0])
            print(line)
        lineCount+=1
    print(total)