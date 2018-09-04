Now only done with strings

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
    dict = {dict of all the stories}

    function to have user choose story
    starterString = "some string with {} in it"
    list with all the diffrent word types
    code to prompt the user for all of them
    put all answers in a list
    print answer
