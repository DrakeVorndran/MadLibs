from random import random
storyList = ['A', ['noun', 1], 'in', ['Wacky_State', 3], 'was', 'arrested', 'this', 'morning', 'after', 'he', ['verb', 10], 'a', ['noun', 12], 'in', 'from', 'of', ['noun', 16], '.', ['proper_name', 18], ',', 'had', 'a', 'history', 'of', ['verb', 24], ',', 'but', 'no', 'one,', 'not', 'even', 'his', ['noun', 32], 'ever', 'imagined', 'he\’d', ['verb', 36], 'with', 'a', ['noun', 39], 'stuck', 'in', 'his', ['part_of_the_body', 43], '.', '“I', 'always', 'thought', 'he', 'was', ['adjective', 50], ',', 'but', 'I', 'never', 'thought', 'he\’d', 'do', 'something', 'like', 'this.', 'Even', 'his', ['Relative', 63], 'was', 'surprised.”', 'After', 'a', 'brief', ['activity', 69], ',', 'cops', 'followed', 'him', 'to', 'a', ['chain_restaurant', 76], ',', 'where', 'he', 'reportedly', ['Past_tense_adjective', 81], 'in', 'the', 'fry', 'machine.', 'In', '[month],', 'a', 'woman', 'was', 'charged', 'with', 'a', 'similar', 'crime.', 'But', 'rather', 'than', ['verb', 99], 'with', 'a', ['noun', 102], ',', 'she', ['Past_tense_verb', 105], 'with', 'a', ['Adjective', 108], '.', 'Either', 'way,', 'we', 'imagine', 'that', 'after', 'witnessing', 'him', ['verb', 118], 'with', 'a', ['noun', 121], 'there', 'are', 'probably', 'a', 'whole', 'lot', 'of', ['plural_noun', 129], 'that', 'are', 'going', 'to', 'need', 'some', 'therapy.']

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
