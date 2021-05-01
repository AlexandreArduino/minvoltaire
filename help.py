import pygame
from pygame.locals import *
from random import randint
from screen import log
import os

def help():
    if os.name == "nt": os.system('notepad readme.txt')
    else:
        os.system('cat readme.txt')
        input("Appuyez pour continuer ...") 
    log("Starting help menu ...")
    pygame.init()
    dim = (largeur, hauteur) = (800, 600)
    win = pygame.display.set_mode(dim)
    pygame.display.set_caption("VOLTAIRE PROJECT HACK BY BAALBAKYA | README")
    font = pygame.font.Font(None, 24)
    while True:
        win.fill((0, 0, 0))
        background = pygame.image.load("files/voltaire_hack.png")
        fond = background.convert()
        win.blit(fond,(0,0))
        text = font.render("Manuel d'utilisation : " , 1, (255, 255, 255))
        win.blit(text, (330, 20))
        text = font.render("Développé par @Meuhsieur Capuche et testé par @Abcsworld" , 1, (randint(0, 255), randint(0, 255), randint(0, 255)))
        win.blit(text, (180, 60))
        text = font.render("Fermez cette fenêtre pour démarrer le logiciel", 1, (255, 255, 255))
        win.blit(text, (232, 100))
        text = font.render("Pour des problèmes d'installation, merci de contacter : <mail@gmail.com>", 1, (255, 255, 255))
        win.blit(text, (20, 150))
        text = font.render("En appuyant sur e, vous activez/désactivez l'enregistrement des positions", 1, (255, 255, 255))
        win.blit(text, (20, 190))
        text = font.render("Cela se produit dès que vous restez plus d'une seconde sans bouger la souris", 1, (255, 255, 255))
        win.blit(text, (20, 230))
        text = font.render("/!\ Faites donc attention de ne pas laisser la souris à une mauvaise position pour rien", 1, (255, 255, 255))
        win.blit(text, (20, 270))
        text = font.render("Quand vous entendez : \"Hé mon gâté comment tu vas bien ?\", alors la position a été sauvegardée", 1, (255, 255, 255))
        win.blit(text, (20, 310))
        text = font.render("Enfin, quand toutes les positions sont enregistrées, appuyez sur e pour stopper le processus", 1, (255, 255, 255))
        win.blit(text, (20, 350))
        text = font.render("Pour commencer la simulation appuyez sur s, vous avez 5 secondes où la fenêtre est bloquée", 1, (255, 255, 255))
        win.blit(text, (20, 390))
        text = font.render("Pendant ce temps, mettez la page web du projet voltaire en premier plan (cliquez dessus)", 1, (255, 255, 255))
        win.blit(text, (20, 430))
        text = font.render("Vos positions vont êtres répétées avec une pause de 20 secondes toutes les 10 fois", 1, (255, 255, 255))
        win.blit(text, (20, 470))
        text = font.render("Vous pouvez stopper ce processus en fermant la fenêtre seulement pendant ces 20 secondes !", 1, (255, 255, 255))
        win.blit(text, (20, 510))
        text = font.render("Pour toutes autres questions, veuillez contacter l'addresse mail plus haut :)", 1, (255, 255, 255))
        win.blit(text ,(20, 550))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return True
        pygame.display.update()
        pygame.time.wait(100)