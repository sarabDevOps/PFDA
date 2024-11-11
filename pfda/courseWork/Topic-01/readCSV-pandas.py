# Read CSV as a pandas
# Author Sarabjeet 


import pandas

FILENAME = "data.csv"
DATADIR = "../Topic-01/"

df = pandas.read_csv(DATADIR+FILENAME)
print(df)