# Author Sarabjeet Kumar


FILENAME = "data.txt"
DATADIR = "../Topic-01/"
#Topic-01\data.txt

print(DATADIR +  FILENAME)

with open(DATADIR + FILENAME , "rt") as fp:
    total = 0
    for line in fp:
        print(line, end="")  
        try:
            total = total+ int(line)
        except ValueError:
         print("variable did not contain a number! " + line)
    print(total)