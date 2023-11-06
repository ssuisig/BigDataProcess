#!usr/bin/python3
import datetime

uberDayDic = dict()
uberTripsDic = dict()

f = open("uber_exp.dat", "rt")
f2 = open("uberoutput.txt", "wt")

for line in f:
    tempList = line[:-1].split(',')
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

for i in uberDayDic:
    f2.write("%s,%s %d,%d\n"%(i[0],i[1],uberDayDic[i], uberTripsDic[i]))

f.close
f2.close