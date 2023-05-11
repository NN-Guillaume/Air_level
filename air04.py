""" Un seul à la fois """

# Créer un programme qui affiche une  chaîne de caractères en évitant les caractères identiques adjacents.

import sys
import unittest

# turn the list into a string and display it
def returnToString(li):
    simpleStr = ' '.join(map(str, li))
    #print(simpleStr, end=' ')
    print(simpleStr, end=' ')


# revert to a simple list
def revertBack(li):
    li[0::] = [''.join(li[0::])]
    #print(li)
    returnToString(li)


# take care of any twin letters
def twinHunter(li):
    li = list(dict.fromkeys(li))
    #return(li)
    #print(li)
    revertBack(li)


# Convert each word into a list
def wordConvert(li):
    for word in li:
        isList = list(word)
        #print(isList, sep='\n')
        twinHunter(isList)


# Turn your input into a list
def strToList(sentence):
    nowList = list(sentence.split(" "))
    #print(nowList)
    wordConvert(nowList)

try:
    myInput = sys.argv[1] # "Hello my lord"
except:
    sys.exit(" ERROR ")


strToList(myInput)



""" TEST """
class TestSplitFunc(unittest.TestCase):

    def test_oddHunter(self):
        self.assertEqual(strToList("hello my dude"), ['hello','my','dude'])

    """def test_type(self):
        self.assertRaises(TypeError, splitFunc, "turlututu chapeau pointu")"""