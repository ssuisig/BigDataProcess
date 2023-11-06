#!usr/bin/python3
genreDict = dict()
genreList = []

f = open("movies_exp.dat", "rt")
f2 = open("movieoutput.txt", "wt")

for line in f:
    genreList = line[line.rfind(':')+1:-1].split('|')
    for i in genreList:
        if i in genreDict:
            genreDict[i] += 1
        else:
            genreDict[i] = 1
for i in genreDict:
    f2.write('%s %s\n'%(i, genreDict[i]))

f.close
f2.close