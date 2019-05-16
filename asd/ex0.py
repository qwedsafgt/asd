import csv
csvfile=open("ex0_sample.csv",'r')
reader=csv.reader(csvfile)
rows=[row for row in reader]
print(rows)
