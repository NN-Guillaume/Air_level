""" Chercher l'intrus """

# Créer un programme qui retourne la valeur d'une liste qui n'a pas de paire

# exemple "1 2 3 4 5 4 3 2 1"
# display ---> 5

import sys


# count each value ---> equal "2" if twins and "1" if single ---> display the single value
def odd_hunter(li):
    for x in li:
        value = li.count(x)

        if value == 1:
            print(x, end='  ')


try:
    myList = sys.argv[1:] # 1 2 3 4 5 4 3 2 1
except:
    sys.exit(" ERROR ") # do not trigger any error if no args in input !  :-C


odd_hunter(myList)
















# Most easy and less effectiv solution...
"""
for i in testList:
    while testList[0] == testList[-1]:

        testList.pop(0)
        testList.pop(-1)
        print(testList)

        if len(testList) == 1:
            print(" This is the only single element")
            print(testList)
            break

        else:
            continue
"""