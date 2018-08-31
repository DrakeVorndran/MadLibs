inString = input("write a story you would like to be converted into madlibs")
# inString = "write a story [name] would like to be converted into madlibs"

def parse(type,inString):
    type = type.upper()
    if((type)=='L'):

        index1 = inString.index(" ")

        outList = []

        while(index1<len(inString)-1):
            if(inString[index1-1]=="]"):
                outList.append([inString[1:index1-1],len(outList)])
            else:
                outList.append(inString[:index1])
            inString = inString[index1+1:]
            if(" " in inString):
                index1 = inString.index(" ")
            else:
                index1 = len(inString)
        outList.append(inString[:index1])
        print (outList)
    elif((type)=="S"):
        index1 = 0
        index2 = 0
        outList = ["",[]]
        while("]" in inString):
            print("im heree")
            index1 = inString.index("[")
            index2 = inString.index("]")
            outList[1].append(inString[index1+1:index2])
            outList[0]+=inString[:index1]+"%s"
            inString = inString[index2+1:]
        print (outList)

parse("S",inString)
