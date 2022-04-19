import scrapLibrary as sl
from bs4 import BeautifulSoup
import requests

class Conteudo:
    def __init__(self, url, titulo, corpo):
        self.url = url
        self.titulo = titulo
        self.corpo = corpo

    def pega_pagina(self, url):
        sl.verifica_erro_pagina(url)
        req = requests.get(url)
        return BeautifulSoup(req.text, 'html.parser')

    def scrape_NYTimes(self, url):
        bs = self.pega_pagina(url)
        titulo = bs.find('h1').text
        linhas = bs.find_all('p', {'class':'story-content'})
        corpo = '\n'.join([linha.text for linha in linhas])
        return Conteudo(url, titulo, corpo)

    def scrape_Brookings(self, url):
        bs = self.pega_pagina(url)
        titulo = bs.find('h1').text
        linhas = bs.find_all('div', {'class':'post-body'})
        corpo = '\n'.join([linha.text for linha in linhas])
        return Conteudo(url, titulo, corpo)

    def pega_conteudo_brookings(self, url):
        #url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
        conteudo = self.scrape_Brookings(url)
        print(f'Título: {conteudo.title}')
        print(f'URL: {conteudo.url}')
        print(conteudo.body)

    def pega_conteudo_nytimes(self, url):
        #url_nyt = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality/'
        conteudo = self.scrape_NYTimes(url)
        print(f'Título: {conteudo.title}')
        print(f'URL: {conteudo.url}')
        print(conteudo.body)


