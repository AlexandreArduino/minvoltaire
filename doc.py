import pygame
from pygame import *
from screen import log

def doc():
    log("Starting documentation menu ...")
    pygame.init()
    dim = (largeur, hauteur) = (900, 900)
    win = pygame.display.set_mode(dim)
    pygame.display.set_caption("VOLTAIRE PROJECT HACK BY BAALBAKYA | DOCUMENTATION")
    font = pygame.font.Font(None, 24)
    while True:
        for i in range(1, 5):
            win.fill((0, 0, 0))
            background = pygame.image.load("doc/doc" + str(i) + ".png")
            fond = background.convert()
            win.blit(fond,(0,0))
            pygame.display.update()
            for j in range(0, 500):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        return True
                    else: pass
                pygame.time.wait(10)