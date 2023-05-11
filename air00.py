""" Split """

# Créer un programme qui découpe une chaîne de caractères en tableau (séparateurs: espaces, tabulations, retour à la ligne).

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( string_à_couper, string_séparateur )
#       algo...
#       return (tableau)

import sys
import unittest

# Cut the string and display each elements over one another
def splitFunc(sentence, space):
    if type(sentence) not in [str]:
        raise TypeError("Must use a string as first argument")
    nowList = list(sentence.split(space))
    #print(nowList)
    print(*nowList, sep='\n')


try:
    myInput = sys.argv[1] # "Hello my dudes  :-D"
except IndexError:
    sys.exit(" ERROR ")


splitFunc(myInput, " ")



""" TEST """
class TestSplitFunc(unittest.TestCase):

    def test_type(self):
        self.assertRaises(TypeError, splitFunc, "turlututu chapeau pointu")