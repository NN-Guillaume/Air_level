""" Concat """

# Créer un programme qui transforme un tableau une  chaîne de caractères en une seule chaîne de caractères.
# Espacé d'un séparateur donné en dernier argument.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( array_de_strings, séparateur )
#       algo...
#       return (string)

import sys

myInput = sys.argv[1] #  "Hello"  "my"  "dudes"   "":-D"  HOW TO PUT A LIST HERE ?
mySpliter = sys.argv[2] # " "

def strToList(sentence):
    nowList = list(sentence.split(" "))
    print(nowList)

def uniteFunc(isAList, unify):
    strToList(myInput)
    displayStr = unify.join(isAList)
    print(displayStr)

try:
    uniteFunc(myInput, mySpliter)
except:
    sys.exit(" ERROR ")