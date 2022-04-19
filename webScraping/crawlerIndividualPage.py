
import scrapLibrary as sl
from bs4 import BeautifulSoup
import requests

def pega_pagina(url):
    sl.verifica_erro_pagina(url)
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

'''
Página de teste do NY Times não existe mais
def scrape_NYTimes(url):
    bs = pega_pagina(url)
    titulo = bs.find('h1').text
    linhas = bs.find_all('p', {'class': 'story-content'})
    corpo = '\n'.join([linha.text for linha in linhas])
    return [url, titulo, corpo]
'''

def scrape_Brookings(url):
    bs = pega_pagina(url)
    titulo = bs.find('h1').text
    linhas = bs.find_all('div', {'class': 'post-body'})
    corpo = '\n'.join([linha.text for linha in linhas])
    return [url, titulo, corpo]


def pega_conteudo_brookings(url):
    # url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
    conteudo = scrape_Brookings(url)
    print(f'Título: {conteudo[1]}')
    print(f'URL: {conteudo[0]}')
    print(conteudo[2])

'''
Página de teste do NY Times não existe mais
def pega_conteudo_nytimes(url):
    # url_nyt = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality/'
    conteudo = scrape_NYTimes(url)
    print(f'Título: {conteudo[1]}')
    print(f'URL: {conteudo[0]}')
    print(conteudo[2])
'''

