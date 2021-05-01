import os
from screen import log
import maintenance
from time import sleep
from var import REGISTERY
from orthocorrector import ORTHOCORRECTOR
import ss
import requests
import pynput
from pynput.mouse import Button, Controller

mouser = Controller()

def get_data(path):
    log("Getting data from " + path + " ...")
    try:
        file = open(path, "r")
        file.close()
    except:
        return 0
    file = open(path, "r")
    n = file.readline()
    file.close()
    try:
        return int(n)
    except:
        return 0
def save_preset():
    log("Saving preset as archive ...")
    try:
        os.mkdir("presets")
    except:
        pass
    log(copyfile("files/x.preset", "presets/x.preset"))
    log(copyfile("files/y.preset", "presets/y.preset"))
def copyfile(path1, path2):
    log("Copying file ...")
    try:
        file = open(path1, "r")
        file.close()
    except:
        return "Error " + str(path1) + ", unable to access"
    try:
        file = open(path1, "r")
        file2 = open(path2, "w")
        file2.write("".join(file.readlines()))
        file.close()
        file2.close()
        return "Success from " + str(path1) + " to " + str(path2)
    except:
        return "Error during process"

def init_all_process():
    main_file_config_init(REGISTERY().main_file_config_path)
    if maintenance.check():
        log("Le site est en maintenance, en attente de la fin de celle-ci ...")
        while maintenance.check(): sleep(10)
    else:
        pass
def main_file_config_init(path):
    log("Veryfing and creating main config file ...")
    try:
        file = open(path, "r")
        file.close()
    except:
        pass
    if True:
        file = open(path, "w")
        file.write("""[MUSIC]:1
[AUTOMAINTENANCE]:1
[WIDTH_LETTER_IN_PIX]:10
[CORRECTOR]:0
        """)
        file.close()
def read_file_config(path, arg):
    if not verify_path(path):
        return "Error path"
    else:
        file = open(path, "r")
        l = file.readlines()
        file.close()
        for i in range(0, len(l)):
            l[i] = l[i].replace("\n", "")
            l[i] = l[i].split(":")
        for i in range(0, len(l)):
            if l[i][0] == arg:
                return l[i][1]
        return "no arg corresponding"
def verify_path(path):
    try:

        file = open(path, "r")
        file.close()
        return True
    except:
        return False
def auto_correct(x0=REGISTERY().x0_select_text, y0=REGISTERY().y0_select_text, state=True):
    if state:
        file = open("files/data.json", "w")
        s = str(ss.select_text())
        file.write("{\"text\":\"" + s + "\"}")
        file.close()
        if os.name == "posix":
            os.system('nodejs dev.js')
        file = open("files/result.json", "r")
        l = file.readline()
        file.close()
        x1 = x0+len(s)
        log("Asked : " + s)
        log("Answer : " + l)
        file = open("dic/database.db", "a")
        file.write(s + ":" + l + "\n")
        file.close()
        s = s.split(" ")
        l = l.split(" ")
        mouser.position = (x0+3+int(read_file_config(REGISTERY().main_file_config_path, "[WIDTH_LETTER_IN_PIX]"))*get_pos(s, l), y0)
        mouser.press(Button.left)
        mouser.release(Button.left)
        return True
    else: return True
def answer_correct(sentence):
    file = open("files/data.json", "w")
    s = sentence
    file.write("{\"text\":\"" + s + "\"}")
    file.close()
    if os.name == "posix":
        os.system('nodejs dev.js')
    file = open("files/result.json", "r")
    l = file.readline()
    file.close()
    file = open("dic/database.db", "a")
    file.write(s + ":" + l + "\n")
    file.close()
    l = l.split(" ")
    sentence = sentence.split(" ")
    for i in range(0, len(sentence)):
        if sentence[i] != l[i]:
            return sentence[i]
        else:
            pass
    return "Pas d'erreurs"
def get_pos(sentence, answer):
    print(sentence)
    print(len(sentence))
    print(answer)
    print(len(answer))
    count = 0
    for i in range(0, len(sentence)):
        if sentence[i] != answer[i]:
            return count
        else:
            count += len(sentence[i])+1 #for spaces value
            print(sentence[i] + " => " + str(len(sentence[i])))
    return count
def remove_app():
    if input("First check, are-you certain you want to remove this app ? Y/n >>> ").lower() == 'y' and input("Second check, Are-you certain ? Y/n >>> ").lower() == 'y':
        print("Removing this app ...")
        if os.name == "posix":
            os.system('rm -Rf ../voltaire')
        elif os.name == "nt":
            os.system('rmdir /Q /S ../voltaire')
        else:
            print("Operating System not supported !")
        input("Press enter to exit ...")
        exit()
def start_question(): return (int(input("Temps en minutes d'utilisation >>> ")), False)