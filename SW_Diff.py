import csv
import datetime
export_filename = 'SW_test_' + str(datetime.date.today())+'.csv'
new = []
with open('Solarwinds_Issue_By_Report_0417.csv', 'rb')as f1, open('SW_errors_2017-05-09.csv', 'rb')as f2:
    reader = csv.reader(f1)
    master = list(reader)
    reader = csv.reader(f2)
    report = list(reader)
with open(export_filename, 'wb') as out:
    csvout = csv.writer(out)
    total = 0
    for i in report:
        found = False
        for j in master:
            if i[1] in j:
                found = True
                j[0] = i[0]
                j[2] = i[2]
                csvout.writerow(j)
        if found is False:
            new.append(i)
    csvout.writerow(["These", "Are", "New", "Entries"])
    for i in master:
        found = False
        for j in report:
            if i[1] in j:
                print "found"
                found = True
        if found is not True:
            total = total+1
            print "Missing -- why"
    print str(total) + " Entries Missing!!!"
    for add in new:
        csvout.writerow(add)
with open('solar_remidated.csv', 'ab') as rem:
    remwrite = csv.writer(rem)
    remwrite.writerow(["These", "Are", "New", "Entries"])
    for i in master:
        if i[3] == 'Fixed' or i[3] == 'fixed':
            print i
            remwrite.writerow(i)
