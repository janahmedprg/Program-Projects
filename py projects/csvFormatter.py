import csv
import re

with open('formated.csv', 'w', newline='') as g:
    writer = csv.writer(g)
    with open('new1log.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            s = []
            if re.search("2022-[0-9][0-9]-[0-9][0-9].[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]",row[1][1:24]):
                s.append(row[1])
                x=reader.__next__()
                s.append(x[1])
                while(x[1][:16]!="last_time_stamp:"):
                    if x[1][:6]=="dummy:":
                        print('dummy')
                        break
                    x=reader.__next__()
                    s.append(x[1])
                x=reader.__next__()
                s.append(x[1])
                x=reader.__next__()
                s.append(x[1])
                x=reader.__next__()
                s.append(x[1])
            writer.writerow(s)
