""" Sur chacun d'entre eux """

# Créer un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d'une liste.
# L'opération à appliquer sera toujours le dernier élément

# exemple ---> 1 2 3 4 5 "+2"               10 11 12 20 "-5"
# ---> 3 4 5 6 7                             5  6  7 15

import sys

def doMath(ls, op):
    ls = ls.split(" ")
    #print(ls)

    ls = [eval(i) for i in ls]
    #print(ls)

    op = int(op)

    for i in ls:
        res = i + op
        print(res, end=" ")

nuls = sys.argv[1]
oper = sys.argv[2]

doMath(nuls, oper)
