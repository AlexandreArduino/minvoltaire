import os
import last_pip_registered
from var import REGISTERY

try:
    import requests
    request_check_import = True
except:
    request_check_import = False

R = REGISTERY()

def installer():
    print("Welcome to the Voltaire Project Hack installer ! (developped by @Meuhsieur Capuche and tested by @absworld")
    input("Press enter to start the installation ...")
    print("If you've got some problems after that, please contact : alexandrepybaalbaky@gmail.com")
    print("/!\ WARNING : You are using the uncompiled version !")
    print("You need to have this packages installed on your computer : " + str(R.packages_necessary) + " ...")
    if os.name == "posix":
        for i in range(0, len(R.linux_commands)):
            os.system(R.linux_commands[i])
        for i in range(0, len(R.packages_necessary)):
            os.system('pip3 install ' + R.packages_necessary[i])
        if ask_reset(): delete_files_github_or_reset()
    elif os.name == "nt":
        '''try:
            if True:
               if request_check_import:
                    print("Downloading last version of pip3 for you because you're so nice with me :) I'm joking ! ^^ ...")
                    file = open("cache.py", "w")
                    file.write(requests.get("https://bootstrap.pypa.io/get-pip.py").text)
                    file.close()
                    print("Installing pip3 ...")
                    os.system('cache.py')
                    print("Removing installer ...")
                    os.remove("cache.py")
                else:
                    print("Using last version registered of pip3 ...")
                    last_pip_registered.main()'''
        if True:
            print("Installing depencies ...")
            for i in range(0, len(R.packages_necessary)):
                os.system('C:/Users/%username%/AppData/Local/Programs/Python/Python39/Scripts/pip3 install ' + R.packages_necessary[i])
            print("To run the program, you just need to run launcher.py in voltaire !")
            #if ask_reset(): delete_files_github_or_reset()
            exit()
        else:
            #if ask_reset(): delete_files_github_or_reset()
            exit()
    else:
        print("This operating system is not supported, please installed packages by yourself :/")
        print("Make sur that you've got : pip3, python3 and install with pip3 : pygame, pynput and Cx_Freeze, keyboard, then download the source code here : https://github.com/AlexandreArduino/voltaire and run the voltaire_project_hack.py script in voltaire/")
        if ask_reset(): delete_files_github_or_reset()
        exit()
def delete_files_github_or_reset():
    to_del = ['conf/help.menu', 'conf/preset.menu', 'files/data.json', 'files/result.json', 'settings/overclock.set', 'settings/time_btw_clicks.set', 'settings/time_click.set']
    print("Reseting file configuration ...")
    for i in range(0, len(to_del)):
        try: os.remove(to_del[i])
        except: pass
def ask_reset():
    '''if input("Do you want to reset file configuration ? (Y/n) >>> ").lower() == 'y':
        return True
    else:
        return False'''
    return False
installer()
