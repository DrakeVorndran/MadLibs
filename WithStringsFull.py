from termcolor import colored, cprint
from random import random
storyD = {
"The Pizza Place":['''Pizza was invented by a %s %s chef named  %s. To make a pizza, you need to take a lump of %s, and make a thin, round %s %s. Then you cover it with %s sauce, %s cheese, and fresh chopped %s. Next you have to bake it in a very hot %s. When it is done, cut it into %s %s. Some kids like %s pizza the best, but my favorite is the %s pizza. If I could, I would eat pizza %s times a day!.''' ,["adjective","nationality","person","noun","adjective","noun","adjective","adjective","plural noun","noun","number","shapes","food","food","number"]],

"The Fugitive":['''A %s in %s was arrested this morning after he %s a %s in from of %s . %s , had a history of %s , but no one, not even his %s ever imagined he'd %s with a %s stuck in his %s . "I always thought he was %s , but I never thought he'd do something like this. Even his %s was surprised." After a brief %s , cops followed him to a %s , where he reportedly %s in the fry machine. In %s, a woman was charged with a similar crime. But rather than %s with a %s , she %s with a %s . Either way, we imagine that after witnessing him %s with a %s there are probably a whole lot of %s''', ['noun', 'Wacky_State', 'verb', 'noun', 'noun', 'proper_name', 'verb', 'noun', 'verb','noun', 'part_of_the_body', 'adjective', 'Relative', 'activity', 'chain_restaurant', 'Past_tense_adjective', 'month', 'verb', 'noun', 'Past_tense_verb', 'Adjective', 'verb', 'noun', 'plural_noun']],

"Frank The Outlaw":['''"Put your hands up" said the %s. "You\'re under arrest for %s" the %s at the %s"."%s!" thought Frank. His hands were %s like %s on a %s. This wasn\'t the first time he had %s a %s and he knew he was in %s trouble. Just moments before Frank %s into a %s and %s a %s and a %s. He was spotted and a big %s chased after him and %s him in the %s. Now frank was surrounded and had no choice but to surrender. So it was off to %s for Frank. Frank was the %s sheep of his %s, always %s into trouble. It started when Frank %s a %s from a neighbor and %s rode the %s home''', ['noun', 'verb ending in ing', 'noun', 'noun', 'exclamation', 'verb ending in ing', 'plural noun', 'noun', 'past tense verb', 'noun', 'adjective', 'past tense verb', 'noun', 'past tense verb', 'noun', 'noun', 'noun', 'past tense verb', 'body part', 'place', 'color', 'noun', 'verb ending in ing', 'past tense verb', 'noun', 'adverb', 'noun']]

}

def getIn(prompt = "",type="person",cpuIn="empty"):
    if type=="person":
        return input(prompt)
    else:
        if cpuIn=="empty":
            return"asdf"
        else:
            return(cpuIn)
def printStories():
    stories = []
    for x in storyD:
        stories.append(x)
    for x in range(len(stories)):
        print (str(x+1)+". "+colored(stories[x],"red"))
    return(stories)

def chooseStory():
    print("Choose your story:")
    stories = printStories()
    userNotSmart = True
    while(userNotSmart):
        print("Please type either the number or name of the story you'd like to play: ")
        userIn = (getIn().lower()).title()
        print(userIn)
        if(userIn == "Stop"):
            userNotSmart = False
        elif(userIn in stories):
            return(storyD[userIn])

        else:
            try:
                userIn = int(userIn)
                return(storyD[stories[userIn-1]])
            except ValueError:
                print ("Im sorry but {} is not an input I recognise".format(userIn))
            except IndexError:
                print ("I dont have that many stories")
                print("heres my list:")
                printStories()


def test():
    chosenStory = storyD["Frank The Outlaw"]
    for x in range(len(chosenStory[1])):
        chosenStory[1][x] = (colored(getIn(chosenStory[1][x]+':',"cpu",chosenStory[1][x]),"yellow",attrs=['bold']))
    print (chosenStory[0] % tuple(chosenStory[1]))

def getWords(cS):
    wordsL = cS[1]
    wordsR = []
    for x in range(len(wordsL)):
        wordsR.append(x)

    for x in range(50+int(random()*100)):
        rand1 = int(random()*len(wordsL))
        rand2 = int(random()*len(wordsL))
        wordsL[rand1],wordsL[rand2] = wordsL[rand2],wordsL[rand1]
        wordsR[rand1],wordsR[rand2] = wordsR[rand2],wordsR[rand1]


    for x in range(len(wordsL)):
        wordsL[x] = (colored(getIn(wordsL[x]+':'),"yellow",attrs=['bold']))
    for x in range(len(wordsL)):
        pos1 = wordsR.index(x)
        pos2 = wordsR[pos1]
        wordsR[pos1],wordsR[pos2],wordsL[pos1],wordsL[pos2] = wordsR[pos2],wordsR[pos1],wordsL[pos2],wordsL[pos1]
    return(cS)

def run():
    chosenStory = chooseStory()
    chosenStory = getWords(chosenStory)
    print (chosenStory[0] % tuple(chosenStory[1]))

run()
