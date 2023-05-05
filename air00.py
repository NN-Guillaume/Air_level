""" Split """

# Créer un programme qui découpe une chaîne de caractères en tableau (séparateurs: espaces, tabulations, retour à la ligne).

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( string_à_couper, string_séparateur )
#       algo...
#       return (tableau)

import sys

myInput = sys.argv[1] # Hello my dudes  :-D

def splitFunc(sentence, space):
    #algo
    # tun sentence into list
    #separate upon spaces
    nowList = list(sentence.split(space))
    print(nowList)
    #return(nowList)

try:
    splitFunc(myInput, " ")
except:
    sys.exit(" ERROR ")