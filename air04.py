""" Un seul à la fois """

# Créer un programme qui affiche une  chaîne de caractères en évitant les caractères identiques adjacents.

# exemple ---> " Hello my lord "
#  ---> " Helo my lord "
import sys

# Look for twin char
"""def huntTwin(li):
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc = list(abc)
    
    for x in li:
        for y in abc:
            if y == x*2:
                print("TWIN")
            else:
                print(" ??? ")"""

def comp(li, arg):
    rejectList = [ x for x in li if arg in x]
    print(rejectList)

# Convert each word into a list
def wordConvert(li):
    for word in li:
        #print(i, sep='\n')
        isList = list(word)
        #print(*isList, sep='\n')
        print(isList, sep='\n')
        
        

# Turn your input into a list
def strToList(sentence):
    nowList = list(sentence.split(" "))
    print(nowList)
    wordConvert(nowList)

myInput = sys.argv[1]

strToList(myInput)