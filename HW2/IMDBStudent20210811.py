#!usr/bin/python3
genreDict = dict()
genreList = []
resultList = []

inputFile = sys.argv[1]
outputFile = sys.argv[2]

# f = open("E:/bigdata/BigDataProcess/HW2/movies_exp.txt", "rt")
# f2 = open("E:/bigdata/BigDataProcess/HW2/movieoutput.txt", "wt")

with open(inputFile, "rt") as f:
    for line in f:
        genreList = (line[line.rfind(':')+1:]).rstrip('\n').split('|')
        for i in genreList:
            if i in genreDict:
                genreDict[i] += 1
            else:
                genreDict[i] = 1
    for i in genreDict:
        resultStr = str(i)+' '+str(genreDict[i])
        resultList.append(resultStr)
print(resultStr)

with open(outputFile, "wt") as fp:
    for i in resultStr:
        print(i)