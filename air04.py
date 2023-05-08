""" Un seul à la fois """

# Créer un programme qui affiche une  chaîne de caractères en évitant les caractères identiques adjacents.

# exemple ---> " Hello my lord "
#  ---> " Helo my lord "
import sys

# Create a twin  :-O
def valueToList(word):
    value = list(word.split(' '))
    print(value)

# Turn your input into a list
def strToList(sentence):
    nowList = list(sentence.split(" "))
    print(nowList)
    valueToList(sentence)

myInput = sys.argv[1]

strToList(myInput)