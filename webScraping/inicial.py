# Primeiros passos com Web Scraping

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def get_content_tag(page, tag):
    try:
       html = urlopen(page)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('Servidor não encontrado')
    else:
        print('\nProcessando...')

# Usando html.parser
    bs = BeautifulSoup(html.read(), 'html.parser')

    print('\n')
    print('*' * 100)
    print('Usando html.parser')
    print('-' * 100)

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

    print('-' * 100)
    print('*' * 100)
    print('\n')

# Página de teste --> http://www.pythonscraping.com/pages/page1.html
page = input('Digite o endereço da página web: ')
tag = input('Digite a tag HTML [div/h1/h2/h3/title]: ')

get_content_tag(page, tag)