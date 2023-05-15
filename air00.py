""" Split """

# Créer un programme qui découpe une chaîne de caractères en tableau (séparateurs: espaces, tabulations, retour à la ligne).

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( string_à_couper, string_séparateur )
#       algo...
#       return (tableau)

import sys


# Cut the string and display each elements over one another
def split_func(sentence, space):
    if type(sentence) not in [str]:
        raise TypeError("Must use a string as first argument")
    nowList = list(sentence.split(space))
    print(nowList)
    #print(*nowList, sep='\n')      <--- a lot easier than using "return" statement
    return nowList


try:
    myInput = sys.argv[1] # "Hello my dudes  :-D"
except IndexError:
    sys.exit(" ERROR ")


#splitFunc(myInput, " ")
display00 = split_func(myInput, " ")
print(*display00, sep='\n')