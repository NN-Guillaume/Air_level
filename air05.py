""" Sur chacun d'entre eux """

# Créer un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d'une liste.
# L'opération à appliquer sera toujours le dernier élément

import sys

# do addition or substraction upon the symbol given in last arg
def do_math(ls, op):
    ls = ls.split(" ")
    #print(ls)

    ls = [eval(i) for i in ls]
    #print(ls)

    op = int(op)

    for i in ls:
        res = i + op
        print(res, end=" ")


try:
    nuls = sys.argv[1]  # "1 2 3 4 5" "+2"       or        "10 11 12 20"
    oper = sys.argv[2]  # "+2"                   or        "-5"
except:
    sys.exit(" ERROR ")

do_math(nuls, oper)
