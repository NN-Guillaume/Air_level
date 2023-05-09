""" Insertion dans un tableau trié """

# Créer un programme qui ajoute à une liste d'entiers triée un nouvel entier tout en gardant la liste triée dans l'ordre croissant. 

# Le dernier argument est l'élément à ajouter.

# Le programme doit utiliser une fonction prototypée comme suit:

# sorted_insert( array, new_element )
#       algo...
#       return (new_array)

import sys

# FIRST METHOD

# Convert the numbers into list, add the new value and sort the list
"""def sorted_insert(array, new_elem):
    nowList = list(array.split(" "))
    nowList.append(new_elem)
    nowList.sort()
    print(nowList)

myList = sys.argv[1]
newValue = sys.argv[2]

sorted_insert(myList, newValue)"""







# SECOND METHOD

def selectionSort(list):
    for num in range(len(list)):
        minNum = num
        for i in range(num, len(list)):
            #print(list) display the whole process of sorting
            if list[i] < list[minNum]:
                minNum = i
        list[num], list[minNum] = list[minNum], list[num]
    
    return list

def sorted_insert(array, new_elem):
    nowList = list(array.split(" "))
    nowList.append(new_elem)
    selectionSort(nowList)
    print(nowList)

myList = sys.argv[1]
newValue = sys.argv[2]

sorted_insert(myList, newValue)
