""" Suppression sur contenu """

# Créer un programme qui supprime d'un tableau tous les éléments qui ne  contiennent pas une autre chaîne de caractères.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( array_de_strings, string_char )
#       algo...
#       return (new_array_de_strings)

import sys

###########################################################################################################################################

# ma_fonction( array_de_strings, string_char )
#       algo...
#       return (new_array_de_strings)

def control(nameArray, removerChar):
    pass

# remove the words containing the letter
def removeWords(arg1):
    for names in arg1:
        arg1.pop(names)

# turn the string into a list
def splitArgv(string):
    return list(string)

# verify the elements in common, works even if not attached to each others
def sameElem(arg1, arg2):
    for x in arg1:
        for y in arg2:
            if x == y:
                verdict = True
                print("TRUE")
                return verdict


def atStartOrAtEnd(arg1, arg2):
    if arg1[-1:] == arg2[-1:]: # good ! check the end
        print("True")
        # add removal func
        removeWords(arg1)
        
    elif arg1[:+1] == arg2[:+1]: # good ! check the begining
        print("True")
        # add removal func
        removeWords(arg1)
        
    elif sameElem(arg1, arg2):
        print("Contain identical letters but in disorder")
        # add removal func
        removeWords(arg1)
        
    elif not sameElem(arg1, arg2):
        print("False")
        # trigger ERROR...
    else:
        print("unexpected event")


try:
    input01 = str(sys.argv[1]) # Bonjour
    input02 = str(sys.argv[2]) # jour
except:
    sys.exit(" ERROR ")


# print(splitArgv(input01))
splitArgv(input01)
# print(splitArgv(input02))
splitArgv(input02)

atStartOrAtEnd(input01, input02)

###########################################################################################################################################


#input01 = str(sys.argv[1]) # Bonjour
#input02 = str(sys.argv[2]) # jour

#testList = ["Michel", "Albert", "Thérèse", "Benoit"]
#removerElem = "t" # seul Michel doit ressortir
