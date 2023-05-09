""" Afficher le contenu """

# Créer un programme qui affiche le contenu d'un fichier donné en argument

import sys

def readFile(argFile):

    # Opening the given file in read-only mode
    with open(argFile, 'r') as fileData:
        
        # Go through each line of the file
        for line in fileData:
            
            # Print the line
            print(line)

    # Always close the file after reading it
    fileData.close()

try:
    # Give the file in argument
    inputFile = sys.argv[1]
except:
    print(" ERROR ")

readFile(inputFile)