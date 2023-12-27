#!usr/bin/python3

import sys
import numpy as np
import operator
import os

def createDataSet(folder):
        group_list = []
        labels = [] 
        files = os.listdir(folder)
        for i in files:
                labels.append(i[0])
                data = ""
                list = []
                with open(os.path.join(folder, i), 'r') as f:
                        data = f.read().replace('\n', '')
                        for ch in data:
                                list.append(int(ch))
                group_list.append(list)
        group = np.array(group_list) 
        return group, labels

def classify0(test_group, train_group, train_labels, k):
        dataSetSize = train_group.shape[0]
        diffMat = np.tile(test_group, (dataSetSize, 1)) - train_group
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis = 1)
        sortedDistIndicies = sqDistances.argsort()
        classCount = {}
        for i in range(k):
                voteIlabel = train_labels[sortedDistIndicies[i]]
                classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
        return sortedClassCount[0][0]

def compare_predictions(predicted_result, labels):
        cnt = 0 
        file_cnt = len(predicted_result)
        for i in range(file_cnt):
                if (predicted_result[i] != labels[i]):
                        cnt += 1
        result = round(cnt / file_cnt * 100)
        return result

training_folder = sys.argv[1]
test_folder = sys.argv[2]

train_group, train_labels = createDataSet(training_folder)
test_group, test_labels = createDataSet(test_folder)


for i in range(1, 21):
        error = 0
        for j in range(len(test_labels)):
                if test_labels[j] != classify0(test_group[j], train_group, train_labels, i):
                        error += 1
        print(int(error / len(test_labels) * 100))
