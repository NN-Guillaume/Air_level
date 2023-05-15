""" Suppression sur contenu """

# Créer un programme qui supprime d'un tableau tous les éléments qui ne  contiennent pas une autre chaîne de caractères.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_fonction( array_de_strings, string_char )
#       algo...
#       return (new_array_de_strings)

import sys

def names_that_contain_it(arr, stri):
    for names in arr:
        #print(names, sep="\n")

        upStri = stri.upper()
        if upStri not in names:
            
            lowStri = stri.lower()
            if lowStri not in names:

                #print(names)
                return names


try:
    input01 = sys.argv[1:-1]    # "Michel" "Albert" "Thérèse" "Benoit" 
    input02 = sys.argv[-1]      # "t"
except:
    sys.exit(" ERROR ") # do not trigger any error if no args in input !  :-C


display06 = names_that_contain_it(input01, input02)
print(display06)