
from urllib.parse import urlparse
import re
import datetime
import random
import scrapLibrary as sl

paginas = set()
todos_links_internos = set()
todos_links_externos = set()
random.seed(datetime.datetime.now())

#Listas dos links internos encontrados em uma página
def pega_links_internos(bs, inclue_url):
    inclue_url = f'{urlparse(inclue_url).scheme}://{urlparse(inclue_url).netloc}'
    links_internos = []

    #Encontra links que começam com "/"
    for link in bs.find_all('a', href=re.compile('^(⁽/|.*'+inclue_url+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in links_internos:
                if (link.attrs['href'].startswith('/')):
                    links_internos.append(inclue_url + link.attrs['href'])
                else:
                    links_internos.append(link.attrs['href'])

    return links_internos

#Listas dos links externos encontrados em uma página
def pega_links_externos(bs, exclue_url):
    links_externos = []

    #Encontra todos os links que começam com "http" e que não contenham a URL atual
    for link in bs.find_all('a', href=re.compile('^(http|www)((?! '+ exclue_url + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in links_externos:
                links_externos.append(link.attrs['href'])

    return links_externos

def pega_link_externo_aleatorio(pagina_inicial):
    tags = sl.verifica_erro_pagina(pagina_inicial)
    bs = sl.html_parser(tags)
    links_externos = pega_links_externos(bs, urlparse(pagina_inicial).netloc)

    if len(links_externos) == 0:
        print('Sem links externos. Procurando...')
        dominio = f'{urlparse(pagina_inicial).scheme}://{urlparse(pagina_inicial).netloc}'
        links_internos = pega_links_internos(bs, dominio)
        return pega_link_externo_aleatorio(links_internos[random.randint(0, len(links_internos) - 1)])
    else:
        return links_externos[random.randint(0, len(links_externos) - 1)]

def segue_link_externo_apenas(pagina_inicial):
    link_externo = pega_links_externos(pagina_inicial)
    print(f'Link externo aleatório --> {link_externo}')
    segue_link_externo_apenas(link_externo)

def pega_todos_links_externos(url):
    tags = sl.verifica_erro_pagina(url)
    bs = sl.html_parser(tags)
    dominio = f'{urlparse(url).scheme}://{urlparse(url).netloc}'
    links_internos = pega_links_internos(bs, dominio)
    links_externos = pega_links_externos(bs, dominio)

    for link in links_externos:
        if link not in todos_links_externos:
            todos_links_externos.add(link)
            print(link)

    for link in links_internos:
        if link not in todos_links_internos:
            todos_links_internos.add(link)
            pega_todos_links_externos(link)



