from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(input("Input website to scrap header from: "))

soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all(['h1' ,'h2', 'h3','h4','h5','h6'])

print("Header tags: ", *titles,sep='\n\n')

#print("Header tags:")
#for i in titles:
#    print(i.text)
