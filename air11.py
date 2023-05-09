""" Afficher une pyramide """

# Afficher un escalier constitué  d'un caractère et d'un nombre d'étages donné en paramètre.

import sys


# row1 =  1
# row2 =  3    row1 + 2

#         A
#       A A A
#     A A A A A
#   A A A A A A A
# A A A A A A A A A
# 0 1 2 3 4 5 6 7 8

def printSymb(char, row):

    symList = list(char.split(" "))
    #print(symList)

    basicAdd = 3
    rowConter = 0

    """symList.append(char*basicAdd)
    print(symList)"""

    while rowConter != row:
        
        #basicAdd = 3

        #symList.append(char*basicAdd)
        #print(symList)

        basicAdd += 2
        symList.append(char*basicAdd)
        rowConter += 1

        if rowConter == row:
            print(*symList, sep='\n')
            print("END")
            break
        else:
            continue

def printSymb(char, row):

    symList = list(char.split(" "))
    #print(symList)

    basicAdd = 3
    rowConter = 0

    """symList.append(char*basicAdd)
    print(symList)"""

    while rowConter != row:
        
        #basicAdd = 3

        #symList.append(char*basicAdd)
        #print(symList)

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

printSymb(symbol, line)
#printSymbol(symbol, line)