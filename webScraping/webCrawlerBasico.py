
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

def verifica_erro_pagina(page):
    try:
        html = urlopen(page)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('Servidor não encontrado')
    else:
        print('\nProcessando...')

    return html

def html_parser(tags):
    bs = BeautifulSoup(tags.read(), 'html.parser')
    return bs

def mostra_imagens(page, tags):
    bs = html_parser(tags)
    images = bs.find_all('img', {'src':re.compile('\.\./img\/gifts/img.*\.jpg')})

    print('\n')
    print('*' * 100)
    print('Imprimindo relação de imagens')
    print('-' * 100)

    for image in images:
        print(image['src'])
        print('-' * 100)

    print('*' * 100)
    print('\n')

page = 'http://www.pythonscraping.com/pages/page3.html'
tags = verifica_erro_pagina(page)

mostra_imagens(page, tags)