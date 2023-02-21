import sys 
from bs4 import BeautifulSoup
import requests

if len(sys.argv) != 2:
    print("El programa necesita 2 argumentos para funcionar")

else:
    canal=sys.argv[1]
    result = requests.get(canal,cookies={'CONSENT':'YES+1'})
    soup = BeautifulSoup(result.text, 'html.parser')
    with open("codigo.txt", "w", encoding="utf-8") as texto:
        texto.write(result.text)
    print(soup.title.text)
    open('codigo.txt', 'r').read()
    print('hola')
    print("que tal")
