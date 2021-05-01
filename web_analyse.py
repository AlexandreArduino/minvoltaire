from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.google.com/search?channel=fs&client=ubuntu&q=bongeour+les+zamis")
soup = BeautifulSoup(r.text)
print(soup.prettify())
print(soup.find(id="fprsl"))
print(soup.i)