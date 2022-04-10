import csv

with open(r"D:\Users\janah\Desktop\Projects\Program-Projects\py projects\optData.txt") as fin, open("hmwk3table.csv", 'w') as fout:
    o=csv.writer(fout)
    for line in fin:
        o.writerow(line.split())
