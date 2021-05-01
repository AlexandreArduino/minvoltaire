'''from spellchecker import SpellChecker
from var import REGISTERY

R = REGISTERY()

spell = SpellChecker(language='fr')

def correct(sentence):
    sentence = sentence.split(" ")
    for i in range(0, len(sentence)):
        for j in range(0, len(R.ponctuation)):
            sentence[i] = sentence[i].replace(R.ponctuation[j], "")
    misspelled = spell.unknown(sentence)
    for word in misspelled:
        print(spell.candidates(word))
correct(input(">>> "))'''

import pynput
from pynput.mouse import Controller
from time import sleep

mouse = Controller()

while True:
    print(mouse.position)
    sleep(.1)