import os
from screen import log
import pygame
from pygame.locals import *
from var import REGISTERY

def settings():
    log("Starting settings menu ...")
    pygame.init()
    dim = (largeur, hauteur) = (800, 600)
    win = pygame.display.set_mode(dim)
    pygame.display.set_caption("VOLTAIRE PROJECT HACK BY BAALBAKYA | SETTINGS")
    font = pygame.font.Font(None, 30)
    log("Setting up direcories ...")
    try:
        os.mkdir("settings")
    except: pass
    try:
        file = open("settings/time_click.set", "r")
        file.close()
    except:
        file = open("settings/time_click.set", "w")
        file.write("0")
        file.close()
    try:
        file = open("settings/time_btw_clicks.set", "r")
        file.close()
    except:
        file = open("settings/time_btw_clicks.set", "w")
        file.write("0")
        file.close()
    try:
        file = open("settings/overclock.set", "r")
        file.close()
    except:
        file = open("settings/overclock.set", "w")
        file.write("100")
        file.close()
    log("Launching gui ...")
    time_click = get_result("settings/time_click.set")
    time_btw_clicks = get_result("settings/time_btw_clicks.set")
    overcloking = get_result("settings/overclock.set")
    count = 0
    path =  REGISTERY().main_file_config_path
    while True:
        win.fill((0, 0, 0))
        background = pygame.image.load("files/voltaire_hack.png")
        fond = background.convert()
        win.blit(fond,(0,0))
        text = font.render("Paramètres du logiciel" , 1, (255, 255, 255))
        win.blit(text, (300, 20))
        text = font.render("Délai (ms) pendant le click : " + time_click + " ms => settings/time_click.set", 1, (255, 255, 255))
        win.blit(text, (50, 125))
        text = font.render("Délai (ms) entre les clicks : " + time_btw_clicks + " ms => settings/time_btw_clicks.set", 1, (255, 255, 255))
        win.blit(text, (50, 165))
        text = font.render("Vitesse d'éxécution : " + overcloking + " ms => settings/overclock.set", 1, (255, 255, 255))
        win.blit(text, (50, 205))
        text = font.render("Modifier les paramètres globaux : " + path, 1, (255, 255, 255))
        win.blit(text, (50, 245))
        if count == 100:
            log("Refreshing value ...")
            count = 0
            time_click = get_result("settings/time_click.set")
            time_btw_clicks = get_result("settings/time_btw_clicks.set")
            overcloking = get_result("settings/overclock.set")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return True
        pygame.time.wait(100)
        pygame.display.update()
        count += 1
    pygame.quit()
def get_result(path):
    log("Getting data in " + path + " ...")
    try:
        file = open(path, "r")
        file.close()
    except:
        return "undefined"
    file = open(path, "r")
    l = file.readline()
    file.close()
    try:
        return str(int(l))
    except:
        return "Invalid litteral, not int value"