# Recuperação de contúdo de tags filhas e descendentes

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

def get_content_tag(page, tags):

# Usando html.parser
    bs = BeautifulSoup(tags.read(), 'html.parser')

    print('\n')
    print('*' * 100)
    print('Retornando objetos filho')
    print('-' * 100)

    for child in bs.find('table', {'id':'giftList'}).children:
        print(child)

    print('-' * 100)
    print('*' * 100)
    print('\n')

    print('\n')
    print('*' * 100)
    print('Retornando objetos descendentes')
    print('-' * 100)

    for descendant in bs.find('table', {'id':'giftList'}).descendants:
        print(descendant)

    print('-' * 100)
    print('*' * 100)
    print('\n')

    print('\n')
    print('*' * 100)
    print('Retornando objetos irmãos --> Linhas dos produtos de uma tabela')
    print('-' * 100)

    for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

    print('-' * 100)
    print('*' * 100)
    print('\n')

def mostra_imagens(page, tags):
    bs = BeautifulSoup(tags.read(), 'html.parser')
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

# Página de teste --> http://www.pythonscraping.com/pages/page3.html
page = 'http://www.pythonscraping.com/pages/page3.html'

tags = verifica_erro_pagina(page)
# get_content_tag(page, tags)
mostra_imagens(page, tags)