# Author Sarabjeet Kumar


FILENAME = "data.txt"
DATADIR = "../Topic-01/"
#Topic-01\data.txt

print(DATADIR +  FILENAME)

with open(DATADIR + FILENAME , "rt") as fp:

    for line in fp:
        print(line )