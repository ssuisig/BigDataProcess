#!usr/bin/python3
import datetime
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

uberDayDic = dict()
uberTripsDic = dict()


with open(inputFile, "rt") as f:
    for line in f:
        tempList = (line.rstrip('\n')).split(',')
        tempList[2] = int(tempList[2])
        tempList[3] = int(tempList[3])

        dayList = tempList[1].split('/')
        dayInt = datetime.date(int(dayList[2]), int(dayList[0]), int(dayList[1]))
        if dayInt.isoweekday() == 1:
            tempList[1] = 'MON'
        elif dayInt.isoweekday() == 2:
            tempList[1] = 'TUE'
        elif dayInt.isoweekday() == 3:
            tempList[1] = 'WED'
        elif dayInt.isoweekday() == 4:
            tempList[1] = 'THU'
        elif dayInt.isoweekday() == 5:
            tempList[1] = 'FRI'
        elif dayInt.isoweekday() == 6:
            tempList[1] = 'SAT'
        elif dayInt.isoweekday() == 7:
            tempList[1] = 'SUN'

        uberTup = (tempList[0], tempList[1])

        if uberTup in uberDayDic and uberTup in uberTripsDic:
            uberDayDic[uberTup] += tempList[2]
            uberTripsDic[uberTup] += tempList[3]
        else:
            uberDayDic[uberTup] = tempList[2]
            uberTripsDic[uberTup] = tempList[3]  

with open(outputFile, "wt") as fp:
    for i in uberDayDic:
        fp.write("%s,%s %d,%d\n"%(i[0],i[1],uberDayDic[i], uberTripsDic[i]))

