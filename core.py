from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def click(id):
	try:
		search = browser.find_element_by_id(id)
		search.click()
	except:	print("error : " + id)
browser = webdriver.Firefox()
browser.get("https://www.projet-voltaire.fr/")
def click_class(classeur):
		try:
			search = browser.find_element_by_class_name(classeur)
			search.click()
		except: print("error : " + classeur)
try:
	search = browser.find_element_by_id("service-message-close-btn")
	search.click()
	sleep(2)
except: print("Fail maintenance log")
click("authenticateOption")
username = input("Please enter your username >>> ")
psw = input("Please enter your password >>> ")
browser.find_element_by_id("login-username").send_keys(username)
browser.find_element_by_id("login-pwd").send_keys(psw)
input("Appuyez quand vous avez réalisé le captcha ...")
try:
	click("topAuthenticationSubmit")
except: pass
print("Waiting for connection ...")
sleep(15)
print(browser.current_url)
click("applicationOrthographe")
click("btn_home_module_lancer_" + input("Niveau à lancer >>> "))
print("Waiting ...")
sleep(60)
n = browser.current_url
while True:
	click('btn_question_suivante')
	n = browser.current_url
	sleep(.5)
	click_class('nextButton')
	n = browser.current_url
	sleep(.5)
	click_class('understoodButton')
	n = browser.current_url
	sleep(.5)
	click_class('buttonKo')
	n = browser.current_url
	sleep(.5)
	click_class('buttonOk')
	n = browser.current_url
	sleep(.5)
	click_class('buttonKo')
	n = browser.current_url
	sleep(.5)
	click_class('exitButton secondaryButton')
	n = browser.current_url
	sleep(.5)
	click_class('popupButton')
	n =browser.current_url
	sleep(.5)