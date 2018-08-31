game:
    Requirements:
        list of story broken up into single words with words that need
        to be replaced as a list consisting of the word type and position in the text

        user gets a prompt of word type and is expected to put in that word

        output prints out the completed story

    Psudocode:


        starterlist = [random,story,that,[name,3],can,put,in]

        def parseList(starter list):
            goes through starterlist and finds all positions that need replacing and puts them in a list it returns

        def replaceWords(parseList output):
            goes through the list parseList creates at random and prompts the user to give them the type of word
            then outputs a seperate list that is a clone of the orignal list except for with the replacements made

        def print_story(replaceWords output):
            goes through replacewords output list and appends them to a single string, then prints said string to the console

generator:
    Requirements:
        prompts user for story with parts of it broken in a certin way so parser knows that it is requesting that type of
        word, not part of the story

        parser to turn the story into a list compatible with game

    Psudocode:

        string = userinput(sting to parse)

        parser(string):
            returns compatible list


withstrings:
    starterString = "some string with {} in it"
    list with all the diffrent word types
    code to prompt the user for all of them
    put all answers in a list
    print answer
