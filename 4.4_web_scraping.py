from bs4 import BeautifulSoup
import requests

#recebe o conteudo da requisicao http do site ...
site=requests.get('https://www.climatempo.com.br/').content
#download do site html
soup=BeautifulSoup(site, 'html.parser')
#transforma o html em string:
#print(soup.prettify())

#Procurar: span class="_block _margin-b-5 -gray"
tag_class = soup.find("span", class_="_block _margin-b-5 -gray")

print(tag_class)
#print(tag_class.string)

print(soup.title.string)
#print(soup.a.string)
#print(soup.p.string)
#print(soup.find('admin'))
