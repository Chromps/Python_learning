import re
import csv
import os
import datetime

def main():
    ipfinder = re.compile('(\S+)\ \((\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\)')
    errorfinder = re.compile('(ERROR\:)\ ([\w\d\s]+)\ \:\ (.+)')
    newhost = re.compile('\ +\_+')
    export_filename = 'SW_errors_' + str(datetime.date.today())+'.csv'
    export = csv.writer(open(export_filename, 'wb'))
    export.writerow(['Host Name', 'IP Address', 'Error'])
    with open('../sw_export_0509.txt') as emails:
        line = []
        for i in emails:
            if newhost.match(i):
                if len(line) == 3:
                    export.writerow(line)
                line = []
            elif ipfinder.search(i):
                host = ipfinder.search(i).group(1)
                addr = ipfinder.search(i).group(2)
                line.append(host)
                line.append(addr)
            elif errorfinder.search(i):
                line.append(errorfinder.search(i).group(3))
            else:
                pass

    print "Finished - File can be found at " + os.path.dirname(os.path.abspath(__file__)) +"\\"+ export_filename
    
if __name__ == "__main__":
    main()
