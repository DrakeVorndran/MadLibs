inString = input("write a story you would like to be converted into madlibs")
# inString = "write a story [name] would like to be converted into madlibs"
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
