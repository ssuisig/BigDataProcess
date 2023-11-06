#!usr/bin/python3
genreDict = dict()
genreList = []

f = open("E:/bigdata/BigDataProcess/HW2/movies_exp.txt", "rt")
f2 = open("E:/bigdata/BigDataProcess/HW2/movieoutput.txt", "wt")

for line in f:
    genreList = (line[line.rfind(':')+1:]).rstrip('\n').split('|')
    for i in genreList:
        if i in genreDict:
            genreDict[i] += 1
        else:
            genreDict[i] = 1
for i in genreDict:
    f2.write('%s %s\n'%(i, genreDict[i]))

f.close
f2.close