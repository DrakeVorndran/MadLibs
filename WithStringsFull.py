from termcolor import colored, cprint
from random import random
storyD = {
"The Pizza Place":['''Pizza was invented by a %s %s chef named  %s. To make a pizza, you need to take a lump of %s, and make a thin, round %s %s. Then you cover it with %s sauce, %s cheese, and fresh chopped %s. Next you have to bake it in a very hot %s. When it is done, cut it into %s %s. Some kids like %s pizza the best, but my favorite is the %s pizza. If I could, I would eat pizza %s times a day!.''' ,["adjective","nationality","person","noun","adjective","noun","adjective","adjective","plural noun","noun","number","shapes","food","food","number"]],

"The Fugitive":['''A %s in %s was arrested this morning after he %s a %s in from of %s . %s , had a history of %s , but no one, not even his %s ever imagined he'd %s with a %s stuck in his %s . “I always thought he was %s , but I never thought he'd do something like this. Even his %s was surprised.” After a brief %s , cops followed him to a %s , where he reportedly %s in the fry machine. In %s, a woman was charged with a similar crime. But rather than %s with a %s , she %s with a %s . Either way, we imagine that after witnessing him %s with a %s there are probably a whole lot of %s''', ['noun', 'Wacky_State', 'verb', 'noun', 'noun', 'proper_name', 'verb', 'noun', 'verb','noun', 'part_of_the_body', 'adjective', 'Relative', 'activity', 'chain_restaurant', 'Past_tense_adjective', 'month', 'verb', 'noun', 'Past_tense_verb', 'Adjective', 'verb', 'noun', 'plural_noun']]


}

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
        userIn = (input().lower()).title()
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



s = chooseStory()

for x in range(len(s[1])):  s[1][x] = (colored(input(s[1][x]+':'),"yellow",attrs=['bold']))
print (s[0] % tuple(s[1]))
