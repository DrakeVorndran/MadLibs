from random import random
storyList = ["hello",["name",1],"you","are","a","very",["adjective",6],"human"]

def parseL(Story):
    returnL = []
    for x in Story:
        if(type(x) is list):
            returnL.append(x[1])
    return returnL

def Rwords(editible):
    sClone = storyList[:]
    currEdit = 0
    for x in range(len(editible)):
        currEdit = editible.pop(int(random()*len(editible)))
        prevWord = ""
        if(sClone[currEdit][0][0] in ["a","e","i","o","u"]):
            prevWord = "an"
        else:
            prevWord = "a"
        sClone[currEdit] = input("please give me {} {} ".format(prevWord,sClone[currEdit][0]))
    return sClone

def printStory(printL):
    printerS = ""
    for x in printL:
        printerS+=" "+x
    return printerS[1:]

def test(editible):
    for x in editible:
        storyList[x] = storyList[x][0]

# test(parseL(storyList))
print (printStory(Rwords(parseL(storyList))))
