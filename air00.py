""" Split """

# Créer un programme qui découpe une chaîne de caractères en tableau (séparateurs: espaces, tabulations, retour à la ligne).

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( string_à_couper, string_séparateur )
#       algo...
#       return (tableau)

import sys

def splitFunc(sentence, space):
    nowList = list(sentence.split(space))
    print(nowList)
    
    print(*nowList, sep='\n')

myInput = sys.argv[1] # Hello my dudes  :-D
#spaceSeparator = sys.argv[2] ------------------------> seems useless

try:
    splitFunc(myInput, " ")
except IndexError:
    sys.exit(" ERROR ")
