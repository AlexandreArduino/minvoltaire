import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput import keyboard
from var import REGISTERY
from screen import log
from time import sleep
import clipboard

text_pointeur = Controller()
keyboard = pynput.keyboard.Controller()
R = REGISTERY()

def select_text(x0 = R.x0_select_text, y0 = R.y0_select_text, x1 = R.x0_select_text+1000, y1 = R.y0_select_text):
    if x0 == R.x0_select_text and y0 == R.y0_select_text and x1 == R.x0_select_text+1000 and y1 == R.y0_select_text:
        log("Using default configuration you might have errors !")
    else: pass
    text_pointeur.position = (x0, y0)
    text_pointeur.press(Button.left)
    text_pointeur.position = (x1, y1)
    text_pointeur.release(Button.left)
    sleep(.01)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')
        keyboard.release('c')
    return clipboard.paste()