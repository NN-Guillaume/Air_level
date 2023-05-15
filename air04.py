""" Un seul à la fois """

# Créer un programme qui affiche une  chaîne de caractères en évitant les caractères identiques adjacents.

import sys

# turn the list into a string and display it
def return_to_string(li):
    simpleStr = ' '.join(map(str, li))
    #print(simpleStr, end=' ')
    print(simpleStr, end=' ')


# revert to a simple list
def revert_back(li):
    li[0::] = [''.join(li[0::])]
    #print(li)
    return_to_string(li)


# take care of any twin letters
def twin_hunter(li):
    li = list(dict.fromkeys(li))
    #return(li)
    #print(li)
    revert_back(li)


# Convert each word into a list
def word_convert(li):
    for word in li:
        isList = list(word)
        #print(isList, sep='\n')
        twin_hunter(isList)


# Turn your input into a list
def str_to_list(sentence):
    nowList = list(sentence.split(" "))
    #print(nowList)
    word_convert(nowList)

try:
    myInput = sys.argv[1] # "Hello my lord, god bless you."
except:
    sys.exit(" ERROR ")


str_to_list(myInput)
