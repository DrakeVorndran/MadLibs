storyList = ["hello",["name",1],"you","are","a","very",["adjective",6],"human"]

def parseL(Story):
    returnL = []
    for x in Story:
        if(type(x) is list):
            print(type(x))

parseL(storyList)
