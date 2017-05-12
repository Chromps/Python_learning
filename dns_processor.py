import csv
import re


def main():
    #this checks for new IP scope
    ippat = re.compile('cope\ (\d+.\d+.\d+.\d+)')
    #this gets ip, subnet, and name when new scope is found
    ipsubpat = re.compile('(\d+\.\d+\.\d+\.\d+)\ (\d+\.\d+\.\d+\.\d+)\ \"(.+)\"\ ')
    #this gets option 3 value, the default gateway
    op3pat = re.compile('optionvalue\ 3\ IPADDRESS\ \"(\d+.\d+.\d+.\d+)\"')
    #create csv writer
    csv_export = csv.writer(open('../DOT-Export61tst.csv', 'wb'))
    csv_export.writerow(["IP Address", "Subnet Mask", "Name", "Default Gateway"])
    #open import file
    with open('../10.61-uny.txt', 'r') as read_file:
        currip = ""
        line = []
        for i in read_file:
            if ippat.search(i).group(1) == currip:
                pass
            else:
                #print 'new ip'
                csv_export.writerow(line)
                currip = ippat.search(i).group(1)
                line = []
            if ipsubpat.search(i):
                line.append(ipsubpat.search(i).group(1))
                line.append(ipsubpat.search(i).group(2))
                line.append(ipsubpat.search(i).group(3))
            elif op3pat.search(i):
                line.append(op3pat.search(i).group(1))

print 'Finished'



if __name__ == "__main__":
    main()
