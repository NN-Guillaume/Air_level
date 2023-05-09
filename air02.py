""" Concat """

# Créer un programme qui transforme un tableau une  chaîne de caractères en une seule chaîne de caractères.
# Espacé d'un séparateur donné en dernier argument.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( array_de_strings, séparateur )
#       algo...
#       return (string)

import sys

def uniteFunc(isAList, unify):
    displayStr = unify.join(isAList)
    print(displayStr)

myInput = sys.argv[1:] #  "Hello"  "my"  "dudes"   "":-D"  HOW TO PUT A LIST HERE ?
mySpliter = sys.argv[-1] # " "


try:
    uniteFunc(myInput, mySpliter)
except:
    sys.exit(" ERROR ")
