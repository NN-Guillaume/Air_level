""" Split en fonction """

# Créer un programme qui découpe une  chaîne de caractères en tableau, le tout en fonction du séparateur donné en deuxième agument.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( string_à_couper, string_séparateur )
#       algo...
#       return (tableau)

import sys

myInput = sys.argv[1] # Hello my dudes  :-D
mySpliter = sys.argv[2] # my

def splitFunc(sentence, spliter):
    #algo
    # tun sentence into list
    #separate upon spaces
    nowList = list(sentence.split(spliter))
    print(nowList)
    #return(nowList)

try:
    splitFunc(myInput, mySpliter)
except:
    sys.exit(" ERROR ")