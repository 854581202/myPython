# -*- coding:utf-8 -*-

def findMinAndMax(*myList):
    minVar = myList[1]
    maxVar = myList[1]
    for i in myList:
        if minVar >= i:
            minVar = i
        else:
            maxVar = i
    return minVar,maxVar

print(findMinAndMax(1,3,2,4,5))