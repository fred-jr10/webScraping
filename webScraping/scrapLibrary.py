# Recuperação de contúdo de tags filhas e descendentes

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

def imprime_titulo(titulo):
    print('\n')
    print('▓' * 100)
    print(titulo)
    print('▒' * 100)

def imprime_fecho():
    print('▒' * 100)
    print('▓' * 100)
    print('\n')

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

def pega_conteudo_tags(tag, tags):
    bs = html_parser(tags)
    titulo_tags = 'Conteúdo da tag selecionada'

    imprime_titulo(titulo_tags)

    if tag.lower() == 'div':
        print(bs.div)
    elif tag.lower() == 'h1':
        print(bs.h1)
    elif tag.lower() == 'h2':
        print(bs.h2)
    elif tag.lower() == 'h3':
        print(bs.h3)
    elif tag.lower() == 'title':
        print(bs.title)
    else:
        print('Tag inválida!')

    imprime_fecho()

def pega_tags_filho(tags):
    bs = html_parser(tags)
    titulo_filhos = 'Retornando objetos filho'

    imprime_titulo(titulo_filhos)

    for child in bs.find('table', {'id':'giftList'}).children:
        print(child)

    imprime_fecho()

def pega_tags_descendente(tags):
    bs = html_parser(tags)
    titulo_descendentes = 'Retornando objetos descendentes'

    imprime_titulo(titulo_descendentes)

    for descendant in bs.find('table', {'id': 'giftList'}).descendants:
        print(descendant)

    imprime_fecho()

def pega_tags_irmao(tags):
    bs = html_parser(tags)
    titulo_irmaos = 'Retornando objetos irmãos --> Linhas dos produtos de uma tabela'

    imprime_titulo(titulo_irmaos)

    for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

    imprime_titulo()

def mostra_imagens(tags):
    bs = html_parser(tags)
    imagens = bs.find_all('img', {'src':re.compile('\.\./img\/gifts/img.*\.jpg')})
    titulo_imagem = 'Imprimindo relação de imagens'

    imprime_titulo(titulo_imagem)

    for imagem in imagens:
        print(imagem['src'])
        print('-' * 100)

    imprime_fecho()
