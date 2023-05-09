""" Afficher une pyramide """

# Afficher un escalier constitué  d'un caractère et d'un nombre d'étages donné en paramètre.

import sys

def pyramid(char, rows):

    space = 2 * rows - 2 # used for number of spaces

    for i in range(0, rows):
        for j in range(0, space):
            print(end=" ")
        
        space = space - 2 # decrement space value for each iteration
        
        for j in range(0, i +1):
            display = "%s  " % (char) 
            print(display, end=" ") # print the stars
        print("")


symbol = sys.argv[1]
line = int(sys.argv[2])


pyramid(symbol, line)
































# MY OWN BUILD, almost complete...
"""
def printSymb(char, row):

    #symList = list(char.split(" "))
    #print(symList)
    
    #################################################################
    
    # blank spaces...
    
    #################################################################
    baseList = []
    baseList.append(char)
    
    listOfList = []
    listOfList.append(baseList)
    #print(listOfList)
    
    basicAdd = 3
    rowConter = 1

    while rowConter != row:

        newList = []
        basicAdd += 2
        newList.append(char*basicAdd)
        listOfList.append(newList)
        rowConter += 1

        if rowConter == row:
            print(*listOfList, sep='\n')
            print("END")
            break
        else:
            continue


# print the symbol but NOT as pyramid AND arg problems for row numbers
def printSymbols(char, row):

    symList = list(char.split(" "))
    #print(symList)

    basicAdd = 3
    rowConter = 1

    while rowConter != row:

        basicAdd += 2
        symList.append(char*basicAdd)
        rowConter += 1

        if rowConter == row:
            print(*symList, sep='\n')
            print("END")
            break
        else:
            continue


symbol = sys.argv[1]
line = int(sys.argv[2])

#printSymbols(symbol, line)
printSymb(symbol, line)"""
