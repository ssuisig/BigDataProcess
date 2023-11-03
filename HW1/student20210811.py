#!usr/bin/python3
from openpyxl import load_workbook
wb = load_workbook(filename='student.xlsx')

list1=[]
list2=[]
listGrade=[]
listA1=[]
listB1=[]
listC1=[]
A1=0
B1=0
C1=0
A2=0
B2=0
C2=0
listGrade.append(('0',0))

ws = wb.active
for row in range(2, 76):
    i = 0
    sum = 0
    for col in range(3, 7):
        ratio = [0.3, 0.35, 0.34, 1]
        sum += ws.cell(column=col, row=row).value*ratio[i]
        ws.cell(row=row, column=7, value=sum)
        i += 1
    list1.append(sum)
list2 = list1.copy()
list2.insert(0, 0)
list1.sort(reverse=True)
list1.insert(0, 0)
for i in range(1, len(list1)):
    lenA = int((len(list1)-1)*0.3)
    lenB = int((len(list1)-1)*0.7)
    lenC = len(list1)-1
    if list1[i] < 40:
        listGrade.append((list1[i], 'F'))
        if listGrade[i][0] in list2:
            ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
    else:
        if i <= lenA:
            if i <= lenA //2:
                listGrade.append((list1[i], 'A+'))
                ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
                listA1.append(list1[i])
                A1 += 1
            else:
                listGrade.append((list1[i],'A0'))
                ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
                A2 += 1
        elif i <= lenB:
            if i <= (lenB-lenA) //2 + lenA:
                listGrade.append((list1[i], 'B+'))
                ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
                listB1.append(list1[i])
                B1 += 1
            else:
                listGrade.append((list1[i],'B0'))
                ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
                B2 += 1
        else:
            if i <= (lenC-lenB) //2 + lenB:
                listGrade.append((list1[i], 'C+'))
                ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
                listC1.append(list1[i])
                C1 += 1
            else:
                listGrade.append((list1[i],'C0'))
                ws.cell(row=list2.index(listGrade[i][0])+1, column=8, value=listGrade[i][1])
                C2 += 1
if A1 > A2:
    for i in range(A1-(A1+A2)//2):
        ws.cell(row=list2.index(listA1[-1])+1, column=8, value='A0')
        listA1.pop()
elif B1 > B2:
    for i in range(B1-(B1+B2)//2):
        ws.cell(row=list2.index(listB1[-1])+1, column=8, value='B0')
        listB1.pop()
elif C1 > C2:
    for i in range(C1-(C1+C2)//2):
        ws.cell(row=list2.index(listC1[-1])+1, column=8, value='C0')
        listC1.pop()
print(lenB)
print(C1)
print(C2)
wb.save("student.xlsx")
