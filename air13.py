""" Meta exercice """

# Créer un programme qui vérifie si:
# 1°) - les exercices de l'épreuve de l'air sont présent dans le répertoire
# 2°) - les exercices fonctionnent (sauf celui-ci).

from os import walk

import subprocess

# FIRST - check for the presence of all files (from air00 to air12)

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


# SECOND - check for the presence of all files (from air00 to air12)

# colors to display the result
class bcolors:
    ok_green = '\033[92m'
    fail_red = '\033[91m'
class CorrectionExercise:

    @staticmethod
    def check_exercise(exercise_number, command):
        result = 0
        a = 0
        output = subprocess.getoutput(command)
        expected_outputs = {
            'Air00': ['Hello\n', 'my\n', 'dudes\n', ' ', ':-D'],
            'Air01': ['Hello\n', 'dudes  :-D\n'],
            'Air02': ['Hello my dudes :-D\n'],
            'Air03': ['5\n', 'monsieur\n'],
            'Air04': ['Helo my lord, god bles you.\n'],
            'Air05': ['3 4 5 6 7\n', '5 6 7 15\n'],
            'Air06': ['Michel\n', 'Michel, Thérèse, Benoit\n'],
            'Air07': ['1 2 3 4\n', '10 20 30 33 40 50 60 70 90\n'],
            'Air08': ['10 15 20 25 30 35\n'],
            'Air09': ['Albert, Thérèse, Benoit, Michel\n'],
            'Air10': ['Je danse le mia\n', 'Je danse le mia\n'],
            'Air11': ['O\n', 'OOO\n', 'OOOOO\n', 'OOOOOOO\n', 'OOOOOOOOO\n'],
            'Air12': ['1 2 3 4 5 6\n']
        } 
        for expected_output in expected_outputs[exercise_number]:
            if expected_output in output:
                print(f"{bcolors.ok_green} SUCCESS")
                #print("SUCCESS")
                result += 1
            else:
                print(f"{bcolors.fail_red} FAILURE")
                #print("FAILURE")
            a += 1
        return result

    @staticmethod
    def run_exercises():
        total_success = 0
        exercises = [
            ['Air00', 'python Air00.py "Hello my dudes  :-D"'],
            ['Air01', 'python Air01.py "Hello my dudes  :-D" "my"'],
            ['Air02', 'python Air02.py "Hello" "my" "dudes" ":-D" " "'],
            ['Air03', 'python Air03.py 1 2 3 4 5 4 3 2 1 && python Air03.py bonjour monsieur bonjour'],
            ['Air04', 'python Air04.py "Hello my lord, god bless you."'],
            ['Air05', 'python Air05.py 1 2 3 4 5 "+2" && python Air05.py 10 11 12 20 "-5"'],
            ['Air06', 'python Air06.py "Michel" "Albert" "Thérèse" "Benoit" "t" && python Air06.py "Michel" "Albert" "Thérèse" "Benoit" "a"'],
            ['Air07', 'python Air07.py 1 3 4 2 && python Air07.py 10 20 30 40 50 60 70 90 33'],
            ['Air08', 'python Air08.py 10 20 30 fusion 15 25 35'],
            ['Air09', 'python Air09.py "Michel" "Albert" "Thérèse" "Benoit"'],
            ['Air10', 'cat a.txt && python Air10.py "a.txt"'],
            ['Air11', 'python Air11.py O 5'],
            ['Air12', 'python Air12.py 6 5 4 3 2 1']
        ]


        for exercise in exercises:
            exercise_result = CorrectionExercise.check_exercise(exercise[0], exercise[1])
            total_success += exercise_result

        print(f"Total success: ({total_success}/25)")


CorrectionExercise.run_exercises()