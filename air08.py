""" Mélanger deux tableaux triés """

# Créer un programme qui fusionne deux listes d'entiers triées en les gardants triées.

# Les deux listes seront séparées par un "fusion". (???)

# Le programme doit utiliser une fonction prototypée comme suit:

# sorted_fusion( array1, array2 )
#       algo...
#       return (new_array)

# exemple ---> "10 20 30" fusion "15 25 35" ----------------> 10 15 20 25 30 35

import sys

# FIRST METHOD - PYTHON METHODS

# Convert the numbers into 2 lists, merges the 2 lists into 1 and sort the list
"""def sorted_fusion(arr1, arr2):
    nowList1 = list(arr1.split(" "))
    nowList2 = list(arr2.split(" "))
    nowList1.extend(nowList2)
    nowList1.sort()
    print(nowList1)

board1 = sys.argv[1]
fusion = sys.argv[2]
board2 = sys.argv[3]

sorted_fusion(board1, board2)"""








# SECOND METHOD - SORT BY SELECTION

# turn the list into a string and display it
def returnToString(li):
    simpleStr = ' '.join(map(str, li))
    #print(simpleStr, end=' ')
    print(simpleStr, end=' ')

# sorting by selection
def selectionSort(list):
    for num in range(len(list)):
        minNum = num
        for i in range(num, len(list)):
            #print(list) display the whole process of sorting
            if list[i] < list[minNum]:
                minNum = i
        list[num], list[minNum] = list[minNum], list[num]
    returnToString(list)

# Convert the numbers into 2 lists, merges the 2 lists into 1 and sort the list
def sorted_fusion(arr1, arr2):
    nowList1 = list(arr1.split(" "))
    nowList2 = list(arr2.split(" "))
    nowList1.extend(nowList2)
    selectionSort(nowList1)
    #print(nowList1)

try:
    board1 = sys.argv[1]
    fusion = sys.argv[2]
    board2 = sys.argv[3]
except:
    sys.exit(" ERROR ")

sorted_fusion(board1, board2)