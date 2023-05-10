""" Le roi des tris """

# Créer un programme qui trie une liste de nombres.

# Le programme doit implémenter l'algorithme du tri rapide (QuickSort).

# Le programme doit utiliser une fonction prototypée comme suit:

# my_quick_sort( array )
#       algo...
#       return (new_array)

# https://www.youtube.com/watch?v=5iSZ7mh_RAk&ab_channel=codebasics

# METHOD 1 - QUICKSORT USING LIST COMPREHENSION

import sys

# turn the list into a string and display it
def returnToString(li):
    simpleStr = ' '.join(map(str, li))
    #print(simpleStr, end=' ')
    print(simpleStr, end=' ')

# cut the string according to the given separator
def splitFunc(sentence):
    arr = list(sentence.split())
    print(arr)
    #return arr
    quickSort(arr)

def quickSort(arr):
    # if the array is less or equal to 1 we immediately display it
    if len(arr) <= 1:
        return arr
    
    else:
        # At the begining, pivot is defined at the leftmost
        pivot = arr[0]
        # inferior values to pivot are put on the left side
        left = [ x for x in arr[1:] if x < pivot]
        # greater values to pivot are put on the right side
        right = [ x for x in arr[1:] if x >= pivot]
        # asseble the array as such = inferior values + pivot + greater values
        return quickSort(left) + [pivot] + quickSort(right)


try:
    testArr = sys.argv[1] # "1 2 7 4 1 10 9 -2"
except:
    sys.exit(" ERROR ")

splitFunc(testArr)

sorted_arr = quickSort(testArr)
print("sorted array in ascending order")
returnToString(sorted_arr)










# METHOD 2 - COMPLICATED BUT DETAILED EXPLAINATIONS

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

"""
# Function to find the partition position
def partition(array, low, high):
    
    # choose the rightmost element as pivot
    pivot = array[high]
    
    # pointer for greater element
    point_i = low - 1
    
    # go through all elements, compare each elements with pivot
    for parse_j in range(low, high):
        if array[parse_j] <= pivot:
            
            # if elem smaller than pivot is found, swap it with the greater elem pointed by point_i
            point_i =point_i + 1
            
            # swapping elem at point_i with elem at parse_j
            (array[point_i], array[parse_j]) = (array[parse_j], array[point_i])
            
    # swap the pivot elem with the greater elem specified by point_i
    (array[point_i + 1], array[high]) = (array[high], array[point_i + 1])
    
    # return the position from where partition is done
    return point_i + 1


# Function to perform QuickSort
def quickSort(array, low, high):
    if low < high:
        
        # Find pivot elem such that elem smaller than pivot are on the left and greater than pivot on the right
        pivot = partition(array, low, high)
        
        # recursive call on the left of pivot
        quickSort(array, low, pivot - 1)
        
        # recursive call on the right of pivot
        quickSort(array, pivot + 1, high)


data = [1, 2, 7, 4, 1, 10, 9, -2]
print("unsorted array")
print(data)

size = len(data) # use this to do not get an error type "out of bound exception"

quickSort(data, 0, size - 1) # use this to do not get an error type "out of bound exception"

print("sorted array in ascending order")
print(data)"""