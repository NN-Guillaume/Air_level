""" Meta exercice """

# Créer un programme qui vérifie si:
# 1°) - les exercices de l'épreuve de l'air sont présent dans le répertoire
# 2°) - les exercices fonctionnent (sauf celui-ci).

# Créer une de ces saloperies de test pour chaque exercice.
import sys

import os

from os import walk

# FIRST - check for the presence of all files (from air00 to air12)
"""
myPath = '/Users/guill/Desktop/GALAXY/ENTREPRENEUR/Coding Accelerator/02_Epreuves/02_AIR/Air_level'

verifList = ['air00.py','air01.py','air02.py','air03.py','air04.py','air05.py','air06.py','air07.py','air08.py','air09.py','air10.py','air11.py','air12.py','air13.py','air14.py',]

myFilesNames = []

for (dirpath, dirnames, filenames) in walk(myPath):
    myFilesNames.extend(filenames)
    break
#print(*myFilesNames, sep='\n')

# 
for x in myFilesNames:
    print("File detected: %s" % (x))

if verifList == myFilesNames:
    print("SUCCESS - all files are presents inside the folder !")
else:
    print("Detection have failed - there are missing files in your folder - please check it carefully")

"""
# SECOND - check for the presence of all files (from air00 to air12)

# air00 (1/3) : success
# air00 (2/3) : success
# air00 (3/3) : success
# air01 (1/2) : success
# air01 (2/2) : success
# air02 (1/1) : success
# ...
# air12 (x/x) : success

# Total success: xx/yy
#--------------------------------------------------------------------------------------------------------------------------------------------
""" air00.py """
from air00 import splitFunc
#from unittest import splitFunc

#class TestSplitFunc(unittest.TestCase):

def test_result_is_a_list_with_spaces():
    splitFunc("turlututu chapeau pointu", " ")
    assert splitFunc() == ['turlututu', 'chapeau', 'pointu']

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air01.py """
from air01 import splitFunc

def test_result_is_a_list_without_splitter():
    splitFunc("turlututu chapeau pointu", "chapeau")
    assert splitFunc() == ['turlututu', 'pointu']
#--------------------------------------------------------------------------------------------------------------------------------------------
""" air02.py """
from air02 import uniteFunc

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air03.py """
from air03 import oddHunter

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air04.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air05.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air06.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air07.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air08.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air09.py """

#--------------------------------------------------------------------------------------------------------------------------------------------

""" air10.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air11.py """

#--------------------------------------------------------------------------------------------------------------------------------------------
""" air12.py """

#--------------------------------------------------------------------------------------------------------------------------------------------