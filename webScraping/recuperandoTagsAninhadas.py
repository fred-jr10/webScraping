# Recuperação de contúdo de tags filhas e descendentes

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def get_content_tag(page):
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

# Página de teste --> http://www.pythonscraping.com/pages/page3.html
page = 'http://www.pythonscraping.com/pages/page3.html'

get_content_tag(page)