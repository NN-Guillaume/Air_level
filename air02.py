""" Concat """

# Créer un programme qui transforme un tableau une  chaîne de caractères en une seule chaîne de caractères.
# Espacé d'un séparateur donné en dernier argument.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( array_de_strings, séparateur )
#       algo...
#       return (string)

import sys


# turn a list into a string with a separator
def unite_func(isAList, unify):
    displayStr = unify.join(isAList)
    #print(displayStr)
    return displayStr


try:
    myInput = sys.argv[1:-1] #  "Hello" "my" "dudes" ":-D"
    mySpliter = sys.argv[-1] # " "
except:
    sys.exit(" ERROR ") # do not trigger any error if no args in input !  :-C


display03 = unite_func(myInput, mySpliter)
print(display03)
