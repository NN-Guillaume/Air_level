""" Rotation vers la gauche """

# Créer un programme qui décale tous les éléments d'un tableau vers la gauche.

# Le premier élément devient le dernier à chaque rotation.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_rotation(array)
#       algo...
#       return (new_array)

import sys

# turn the list into a string and display it
def returnToString(li):
    simpleStr = ' '.join(map(str, li))
    #print(simpleStr, end=' ')
    print(simpleStr, end=' ')


# Put the value of index 0 to the end and then delete value at index 0
def rotate_L(myArr):
    myArr.append(myArr[0]) # the first element is duplicated and put to the last place
    myArr.remove(myArr[0]) # remove the first element
    returnToString(myArr)


# convert input arg to list and then modify it by calling the function above
def convertAndRotate(myInput):
    listArr = list(myInput.split(' '))
    #print(listArr)
    rotate_L(listArr)


try:
    myInput = sys.argv[1] # "Bugatti BMW Lamborghini Opel"
except:
    sys.exit(" ERROR ")


convertAndRotate(myInput)