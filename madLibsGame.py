from random import random
storyList = ["hello",["name",1],"you","are","a","very",["adjective",6],"human"]

def parseL(Story):
    returnL = []
    for x in Story:
        if(type(x) is list):
            returnL.append(x[1])
    return returnL

def Rwords(editible):
    currEdit = 0
    for x in range(len(editible)):
        currEdit = editible.pop(int(random()*len(editible)))
        storyList[currEdit] = input("please give me a {} word type: ".format(storyList[currEdit][0]))

Rwords(parseL(storyList))
print(storyList)
