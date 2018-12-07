import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nytimes.com/")
#soup = BeautifulSoup(r.text,"html.parser")

soup = BeautifulSoup(r.text, 'html.parser')

int(soup.prettify())
#for headings in soup.find_all(class_="css-x6ko9e"):
#    print(headings.text)
