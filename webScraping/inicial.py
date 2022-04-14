import scrapLibrary as sl

def menu_principal():
    print("▓" * 100)
    print('Escolha sua opção:')
    print('1 - Conteúdo das tags aninhadas')
    print('2 - Conteúdo das tags selecionadas')
    print('3 - Lista de imagens')
    print('0 - Sair')
    print("▓" * 100)
    print('\n')

    opcao = int(input('Opção --> '))
    return opcao

def menu_tag():
    print("▒" * 100)
    print('Escolha o tipo de tag:')
    print('1 - Filho')
    print('2 - Irmão')
    print('3 - Descendente')
    print("▒" * 100)
    print('\n')

    opcao_tag = int(input('Opção de tag --> '))
    return opcao_tag

#Página de teste1 --> 'http://www.pythonscraping.com/pages/page3.html'
#Página de teste 2 --> ''

titulo_pega_conteudo_tags = 'PEGANDO CONTEÚDO DAS TAGS ANINHADAS'
titulo_pega_tags = 'PEGANDO O CONTEÚDO DA TAG SELECIONADA'
titulo_mostra_imagens = 'EXIBINDO A LISTA DE IMAGENS DO SITE'
flag = 1

page = input('Digite a página a ser explorada: ')
tags = sl.verifica_erro_pagina(page)

while flag:
    opt = menu_principal()

    if opt == 1:
        tag = input('Digite a tag HTML [div/h1/h2/h3/title]: ')
        sl.imprime_titulo(titulo_pega_conteudo_tags)
        sl.pega_conteudo_tags(tag, tags)
        sl.imprime_fecho
    elif opt == 2:
        opt_tag = menu_tag()
        if opt_tag == 1:
            sl.imprime_titulo(titulo_pega_conteudo_tags)
            sl.pega_tags_filho(tags)
            sl.imprime_fecho
        elif opt_tag == 2:
            sl.imprime_titulo(titulo_pega_conteudo_tags)
            sl.pega_tags_irmao(tags)
            sl.imprime_fecho
        elif opt_tag == 3:
            sl.imprime_titulo(titulo_pega_conteudo_tags)
            sl.pega_tags_descendente(tags)
            sl.imprime_fecho
        else:
            print('Opção de tag inválida!')
            continue
    elif opt == 3:
        sl.imprime_titulo(titulo_mostra_imagens)
        sl.mostra_imagens(tags)
        sl.imprime_fecho
    else:
        print('Opção inválida!')

    flag = int(input('Continuar? [0 - Não / 1 - Sim]: '))
    print('\n\n')







