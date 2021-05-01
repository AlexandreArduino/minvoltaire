import os

os.system('git pull')
print("Liste des changements : ")
file = open("patch.txt", "r")
print("".join(file.readlines()))
file.close()