#Juste pour mettre à jour patch.txt
from datetime import datetime


def add():
    n = input("Changements effectués >>> ")
    date = "[" + str(datetime.now().day) + ":" + str(datetime.now().month) + ":" + str(datetime.now().year) + "]"
    file = open("patch.txt", "a")
    file.write(date + " => " + n + "\n")
    file.close()