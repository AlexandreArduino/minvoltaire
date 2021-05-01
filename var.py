from screen import log

class REGISTERY(object):
    def __init__(self):
        log("Starting a new registery session ...")
        self.main_file_config_path = "conf/main.conf"
        self.x0_select_text = 530
        self.y0_select_text = 299
        self.packages_necessary = ['pygame', 'pynput', 'Cx_freeze', 'clipboard', 'requests', 'beautifulsoup4', 'colorama', 'selenium']
        self.linux_commands = ['sudo apt-get update -y', 'sudo apt-get install python3 -y', 'sudo apt-get install python3-pip -y', 'sudo apt-get install xclip -y', 'sudo apt-get install git -y', 'sudo apt-get install firefox-geckodriver']
        self.ponctuation = [',', '.', '?', ':', '/', '!', ';']
        self.url = "https://www.google.com/search?channel=fs&client=android&q="
        self.voltaire_url = "https://www.projet-voltaire.fr/"
R = REGISTERY()