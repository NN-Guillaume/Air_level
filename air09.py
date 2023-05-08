""" Rotation vers la gauche """

# Créer un programme qui décale tous les éléments d'un tableau vers la gauche.

# Le premier élément devient le dernier à chaque rotation.

# Le programme doit utiliser une fonction prototypée comme suit:

# ma_rotation(array)
#       algo...
#       return (new_array)

import sys

def rotate_L(myArr):
    myArr.append(myArr[0]) # the first element is duplicated and put to the last place
    myArr.remove(myArr[0]) # remove the first element
    print(myArr)
    #return myArr

def convertAndRotate(myInput):
    listArr = list(myInput.split(' '))
    print(listArr)
    rotate_L(listArr)

testArr = [ "Bugatti", "BMW", "Lamborghini", "Opel"]

myInput = sys.argv[1]

convertAndRotate(myInput)