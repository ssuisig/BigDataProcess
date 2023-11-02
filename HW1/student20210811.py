#!usr/bin/python3
from openpyxl import load_workbook
wb = load_workbook(filename='student.xlsx')

list1=[]
list2=[]
listGrade=[]

ws = wb.active
for row in range(2, 76):
    i = 0
    sum = 0
    for col in range(3, 7):
        ratio = [0.3, 0.35, 0.34, 0.01]
        sum += ws.cell(column=col, row=row).value*ratio[i]
        ws.cell(row=row, column=7, value=sum)
        i += 1
    list1.append(sum)
list2 = list1.copy()
list1.sort(reverse=True)
print(list1)

for i in range(len(list1)):
    if list1[i] < 40:
        listGrade.append((list1[i], 'F'))
        if listGrade[i][0] in list2:
            ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
    else:
        if i <= int(len(list1) * 0.15):
            listGrade.append((list1[i], 'A+'))
            if listGrade[i][0] in list2:
                ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
        elif i <= int(len(list1) * 0.3):
            listGrade.append((list1[i], 'A0'))
            if listGrade[i][0] in list2:
                ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
        elif i <= int(len(list1) * 0.5):
            listGrade.append((list1[i], 'B+'))
            if listGrade[i][0] in list2:
                ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
        elif i <= int(len(list1) * 0.7):
            listGrade.append((list1[i], 'B0'))
            if listGrade[i][0] in list2:
                ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
        elif i <= int(len(list1) * 0.85):
            listGrade.append((list1[i], 'C+'))
            if listGrade[i][0] in list2:
                ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
        else:
            listGrade.append((list1[i], 'C0'))
            if listGrade[i][0] in list2:
                ws.cell(row=list2.index(listGrade[i][0])+2, column=8, value=listGrade[i][1])
wb.save('student.xlsx')
