
def menu_principal():
    print("▓" * 100)
    print('Escolha sua opção:')
    print('1 - Conteúdo das tags aninhadas')
    print('2 - Conteúdo das tags selecionadas')
    print('3 - Lista de imagens')
    print('4 - Crawler individual - Brookings e NYTimes')
    print('0 - Sair')
    print("▓" * 100)
    print('\n')

    opcao = int(input('Opção --> '))
    return opcao

def menu_tag():
    print('\n')
    print("▒" * 100)
    print('Escolha o tipo de tag:')
    print('1 - Filho')
    print('2 - Irmão')
    print('3 - Descendente')
    print("▒" * 100)
    print('\n')

    opcao_tag = int(input('Opção de tag --> '))
    return opcao_tag

def menu_pagina():
    print('\n')
    print("▒" * 100)
    print('Escolha a página:')
    print('1 - Brookings')
    print('2 - NY Times --> INVÁLIDO')
    print("▒" * 100)
    print('\n')

    opcao_pagina = int(input('Opção de página --> '))
    return opcao_pagina