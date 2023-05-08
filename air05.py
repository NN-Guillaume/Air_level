""" Sur chacun d'entre eux """

# Créer un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d'une liste.
# L'opération à appliquer sera toujours le dernier élément

# exemple ---> 1 2 3 4 5 "+2"               10 11 12 20 "-5"
# ---> 3 4 5 6 7                             5  6  7 15

import sys

def doSubstraction():
    pass

def doAddition(nums, operator):
    manageNums(nums)
    for i in myNums:
        resNum = i + operator
        print(resNum, end=' ')


# identify the operator
def identifyOperator(operator):
    opType = list(operator)
    print(opType)
    
    if opType[0] == '+':
        #addResult = num1 + num2
        operator = opType[1]
        print(" Addition ")
        doAddition(myNums, operator)
    
    elif opType[0] == '-':
        #subResult = num1 - num2
        print(" Soustraction ")

# turn the numbers input into a list
def manageNums(numInput):
    nowList = list(numInput.split(" "))
    print(nowList)

myNums = sys.argv[1]
symbol = sys.argv[2]

manageNums(myNums)
identifyOperator(symbol)
