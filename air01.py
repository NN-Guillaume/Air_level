""" Split en fonction """

# Créer un programme qui découpe une  chaîne de caractères en tableau, le tout en fonction du séparateur donné en deuxième agument.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( string_à_couper, string_séparateur )
#       algo...
#       return (tableau)

import sys


# cut the string according to the given separator
def split_func(sentence, spliter):
    nowList = list(sentence.split(spliter))
    #print(nowList)
    #print(*nowList, sep='\n')
    return nowList


try:
    myInput = sys.argv[1] # "Hello my dudes  :-D" 
    mySpliter = sys.argv[2] # "my"
except IndexError:
    sys.exit(" ERROR ")


display01 = split_func(myInput, mySpliter)
print(*display01, sep='\n')