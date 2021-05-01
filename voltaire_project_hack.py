import os
from time import sleep, monotonic
import requests
from random import randint

if True:
	import help
	import doc
	import settings
	import pynput
	from pynput.mouse import Button, Controller
	import pygame
	from pygame.locals import *
	from pynput import mouse
	import cx_Freeze
	import screen
	from screen import log
	import lib
	import var
else:
	print("There are packages missing, please run installer.py")
	#exit()

#lib.init_all_process()
mouser = Controller()

class VOLTAIRE_PROJECT_HACK(object):
	def __init__(self):
		cache = lib.start_question()
		self.auto_correction = cache[1]
		self.time_to_do = cache[0]
		if cache: del cache
		self.overclock = int(lib.get_data("settings/overclock.set"))
		self.pos = []
		self.windows_timeout = 10000
		self.linux_timeout = 2000
		self.load_preset()
		self.start_time = int(monotonic()/60)
		self.end_time = self.start_time+self.time_to_do
		log("Arrêt prévu à " + str(self.end_time) + " min")
		self.sound = int(lib.read_file_config(var.REGISTERY().main_file_config_path, "[MUSIC]"))
		if os.name == 'posix':
			self.timeout = self.linux_timeout
		elif os.name == 'nt':
			self.timeout = 100000
		else:
			self.timeout = 50000
		log("Getting infos from settings directory ...")
		self.time_click = lib.get_data("settings/time_click.set")
		self.time_btw_clicks = lib.get_data("settings/time_btw_clicks.set")
		self.corrector_state = int(lib.read_file_config(var.REGISTERY().main_file_config_path, "[CORRECTOR]"))
		self.check_dirs()
		self.gui()
	def load_preset(self):
			try:
				if int(lib.get_data("conf/preset.menu")):
					log("Using preset ...")
					try:
						self.pos.clear()
					except: pass
					try:
						file = open("files/x.preset", "r")
						file.close()
						file2 = open("files/y.preset", "r")
						file2.close()
					except:
						return False
					file = open("files/x.preset", "r")
					posx = file.readlines()
					file.close()
					file = open("files/y.preset", "r")
					posy = file.readlines()
					file.close()
					for i in range(0, len(posx)):
						posx[i] = int(posx[i])
					if i: del i
					for i in range(0, len(posy)):
						posy[i] = int(posy[i])
					if i: del i
					for i in range(0, len(posx)):
						self.pos.append((posx[i], posy[i]))
					if i: del i
				else:
					pass
			except:
				log("Cancelling loading preset ...")
	def gui(self):
		self.checkbox_turn = False
		pygame.init()
		dim = (largeur, hauteur) = (800, 500)
		win = pygame.display.set_mode(dim)
		pygame.display.set_caption("VOLTAIRE PROJECT HACK BY BAALBAKYA")
		font = pygame.font.Font(None, 24)
		icon = pygame.image.load('files/voltaire_hack.ico')
		pygame.display.set_icon(icon)
		if self.sound: pygame.mixer.music.load('files/notif.wav')
		self.act = False
		self.enregistrement_accord = False
		checkbox1 = CHECKBOX(150, 400, win, "Afficher le menu d'aide au démarrage (appuyez sur m)", (0, 255, 0), (255, 0, 0), font, self, K_m, "conf/help.menu")
		checkbox2 = CHECKBOX(155, 450, win, "Utiliser les presets au démarrage (appuyez sur p)   ", (0, 255, 0), (255, 0, 0), font, self, K_p, "conf/preset.menu")
		while int(monotonic()/60) < self.end_time:
			win.fill((0, 0, 0))
			background = pygame.image.load("files/voltaire_hack.png")
			fond = background.convert()
			win.blit(fond,(0,0))
			if not self.enregistrement_accord and not self.act:
				text = font.render("ACCUEIL PROJET VOLTAIRE HACK" , 1, (255, 255, 255))
				win.blit(text, (260, 20))
			elif self.enregistrement_accord and not self.act:
				text = font.render("ENREGISTREMENT DES POSITIONS" , 1, (0, 255, 0))
				win.blit(text, (260, 20))
			elif not self.enregistrement_accord and self.act:
				text = font.render("SIMULATION HUMAINE EN COURS" , 1, (255, 0, 0))
				win.blit(text, (260, 20))
			else: pass
			text = font.render("février 2021 - avril 2021" , 1, (255, 255, 255))
			win.blit(text, (300, 60))
			text = font.render("Ouvrez votre navigateur sur www.projet-voltaire.fr, connectez-vous et lancez l'entrainement." , 1, (255, 255, 255))
			win.blit(text, (30, 140))
			text = font.render("Pour configurez la position des boutons sur lesquels cliquer, restez sur eux jusqu'au bip." , 1, (255, 255, 255))
			win.blit(text, (37, 180))
			text = font.render("La position actuelle de votre curseur : " + str(mouser.position) , 1, (255, 255, 255))
			win.blit(text, (190, 260))
			text = font.render("Entrez e pour enregistrer une nouvelle position", 1, (255, 255, 255))
			win.blit(text, (195, 300))
			text = font.render("Entrez s pour start/stop la simulation de toutes positions", 1, (255, 255, 255))
			win.blit(text, (163, 340))
			if self.checkbox_turn:
				checkbox1.update()
				checkbox2.show()
			else:
				checkbox2.update()
				checkbox1.show()
			pygame.display.update()
			self.simulation()
			self.detect_keys()
			if self.detect_wait() and self.enregistrement_accord:
				self.pos.append(mouser.position)
				if self.sound: pygame.mixer.music.play(loops=0, start=0.0)
			pygame.time.wait(self.overclock)
			self.checkbox_turn = not self.checkbox_turn
	def detect_wait(self):
		count = 0
		pos = mouser.position
		if len(self.pos):
			while mouser.position == pos and mouser.position != self.pos[len(self.pos)-1]:
				count += 1
				if count >= self.timeout:
					return True
				else:
					pass
			return False
		else:
			while mouser.position == pos:
				count += 1
				if count >= self.timeout:
					return True
				else:
					pass
			return False		
	def check_dirs(self):
		'''print("Verifying files ...")
		check = True
		l = ['files/notif.wav', 'files/voltaire_hack.ico', 'files/voltaire_hack.png', 'help.py', 'installer.py', 'launcher.bat', 'launcher.py', 'update.py', 'voltaire_project_hack.py', 'screen.py', 'files/logo.txt', 'conf/.version', 'conf/help.menu', 'conf/preset.menu', 'doc.py', 'settings.py']
		for i in range(0, len(l)):
			print(l[i] + " ... => ", end='')
			try:
				file = open(l[i], "r")
				file.close()
				print("yes")
			except:
				print("no")
				check = False
		if not check: self.alert_dirs()
		if i: del i
		if l: del l
		screen.logo()'''
	def alert_dirs(self):
		pygame.init()
		dim = (largeur, hauteur) = (600, 200)
		win = pygame.display.set_mode(dim)
		pygame.display.set_caption("Erreur (pas grave) dans les fichiers")
		font = pygame.font.Font(None, 24)
		for i in range(100, 0, -1):
			win.fill((0, 0, 0))
			text = font.render("Il manque des fichiers pour l'application, veuillez la réinstaller :)" , 1, (255, 255, 255))
			win.blit(text, (10, 10))
			text = font.render("Vous pouvez avoir supprimer un dossier par erreur ou alors avoir déplacé, " , 1, (255, 255, 255))
			win.blit(text, (10, 50))
			text = font.render("l'application. Il manque du contenu dans .files ." , 1, (255, 255, 255))
			win.blit(text, (10, 90))
			text = font.render("Fermeture de cette fenêtre dans : " + str(int(i/10)) + " seconde(s)" , 1, (255, 255, 255))
			win.blit(text, (10, 130))
			pygame.display.update()
			pygame.time.wait(100)
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					exit()
		pygame.quit()
		exit()
	def detect_keys(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				self.save_preset()
				exit()
			if event.type == KEYDOWN and event.key == K_e:
				self.enregistrement_accord = not self.enregistrement_accord
				self.act = False
			if event.type == KEYDOWN and event.key == K_s:
				self.act = not self.act
				self.enregistrement_accord = False
				if self.act: sleep(5)
	def simulation(self):
		if self.act:
			log("Acting ...")
			for i in range(0, 1):
				for j in range(0, len(self.pos)):
					mouser.position = self.pos[j]
					mouser.press(Button.left)
					sleep(self.time_click/1000)
					mouser.release(Button.left)
					sleep(.1)
			for k in range(0, 100):
				sleep(.1)
				if self.act:
					for event in pygame.event.get():
						if event.type == KEYDOWN and event.key == K_s:
							self.act = not self.act
							self.enregistrement_accord = False
							if not self.act: return False
						if event.type == QUIT:
							pygame.quit()
							self.save_preset()
							exit()
			if self.sound: pygame.mixer.music.play(loops=0, start=0.0)
			if self.corrector_state: log("Result : " + str(lib.auto_correct(state=self.auto_correction)))
			sleep(5)
		else: pass
	def simple_gui(self):
		if True:
			pass
	def save_preset(self):
		if len(self.pos):
			log("Saving new preset ...")
			posx = []
			posy = []
			for i in range(0, len(self.pos)):
				posx.append(self.pos[i][0])
				posy.append(self.pos[i][1])
			log("\t- x ...")
			file = open("files/x.preset", "w")
			for i in range(0, len(posx)):
				file.write(str(posx[i]) + "\n")
			file.close()
			log("\t- y ...")
			file = open("files/y.preset", "w")
			for i in range(0, len(posy)):
				file.write(str(posy[i]) + "\n")
			file.close()
			if i: del i
	def get_actually_state_of_help_menu(self):
		file = open("conf/help.menu", "r")
		log("Unable to do RAM optimisation")
		n = int(file.readline())
		file.close()
		return n
class CHECKBOX(object):
	def __init__(self, x, y, win, text, unclicked_color, clicked_color, font, var_space, key, file):
		self.x = x
		self.y = y
		self.win = win
		self.text = text
		self.unclicked_color = unclicked_color
		self.clicked_color = clicked_color
		self.font = font
		self.clicked = False
		self.var_space = var_space
		self.key = key
		self.file = file
		log("Getting configuration in " + self.file + " ...")
		file = open(self.file, "r")
		self.clicked = int(file.readline())
		file.close()
		log("RAM optimisation ...")
		if x: del x
		if y: del y
		if win: del win
		if text: del text
		if unclicked_color: del unclicked_color
		if clicked_color: del clicked_color
		if font: del font
		if var_space: del var_space
		if key: del key
		if file: del file
	def show(self):
		if self.clicked:
			pygame.draw.rect(self.win, self.unclicked_color, [self.x, self.y, 20, 20], 0)
			cache = self.font.render(self.text , 1, self.unclicked_color)
			self.win.blit(cache, (self.x+30, self.y+2))
			pygame.display.flip()
			if cache: del cache
		else:
			pygame.draw.rect(self.win, self.clicked_color, [self.x, self.y, 20, 20], 0)
			cache = self.font.render(self.text , 1, self.clicked_color)
			self.win.blit(cache, (self.x+30, self.y+2))
			pygame.display.flip()
	def update_state(self):
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == self.key:
				self.clicked = not self.clicked
				self.show()
				log("Saving new state in " + self.file + " ...")
				file = open(self.file, "w")
				if self.clicked:
					file.write("1")
				else:
					file.write("0")
				file.close()
				log(str(self.clicked))
				check = True
				while check:
					for event in pygame.event.get():
						if event.type == KEYDOWN and event.key == self.key: check = True
						else: check = False
			if event.type == QUIT:
				pygame.quit()
				self.var_space.save_preset()
				exit()
			if event.type == KEYDOWN and event.key == K_e:
				log("Using var_space switch")
				self.var_space.enregistrement_accord = not self.var_space.enregistrement_accord
				self.var_space.act = False
			if event.type == KEYDOWN and event.key == K_s:
				log("Using var_space switch")
				self.var_space.act = not self.var_space.act
				self.var_space.enregistrement_accord = False
				if self.var_space.act: sleep(5)
				break
	def update(self):
		self.update_state()
		self.show()
try:
	file = open("conf/help.menu", "r")
	if file.readline() == '1':
		file.close()
		help.help()
		doc.doc()
		settings.settings()
	else:
		file.close()
except: pass

V = VOLTAIRE_PROJECT_HACK()
