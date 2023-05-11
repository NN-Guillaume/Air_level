""" Concat """

# Créer un programme qui transforme un tableau une  chaîne de caractères en une seule chaîne de caractères.
# Espacé d'un séparateur donné en dernier argument.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( array_de_strings, séparateur )
#       algo...
#       return (string)

import sys
import unittest

# turn a list into a string with a separator
def uniteFunc(isAList, unify):
    displayStr = unify.join(isAList)
    print(displayStr)


try:
    myInput = sys.argv[1:-1] #  "Hello" "my" "dudes" ":-D"
    mySpliter = sys.argv[-1] # " "
except:
    sys.exit(" ERROR ") # do not trigger any error if no args in input !  :-C


uniteFunc(myInput, mySpliter)




""" TEST """
class TestSplitFunc(unittest.TestCase):

    def test_type(self):
        self.assertRaises(TypeError, uniteFunc, "turlututu" "chapeau" "pointu" " ")