import scrapLibrary as sl
import menu as mn
import crawlerIndividualPage as cip

#Página de teste1 --> http://www.pythonscraping.com/pages/page3.html
#Página de teste Brookings --> https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/
#Página de teste Ny Times --> https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality/ --> NÃO EXISTE MAIS!

titulo_pega_conteudo_tags = 'PEGANDO CONTEÚDO DAS TAGS ANINHADAS'
titulo_pega_tags = 'PEGANDO O CONTEÚDO DA TAG SELECIONADA'
titulo_mostra_imagens = 'EXIBINDO A LISTA DE IMAGENS DO SITE'
titulo_crawler_individual = 'EXIBINDO TÍTULO, URL E CONTEÚDO DOS SITES'
flag = 1

page = input('Digite a página a ser explorada: ')
tags = sl.verifica_erro_pagina(page)

while flag:
    opt = mn.menu_principal()

    if opt == 1:
        tag = input('Digite a tag HTML [div/h1/h2/h3/title]: ')
        sl.imprime_titulo(titulo_pega_conteudo_tags)
        sl.pega_conteudo_tags(tag, tags)
        sl.imprime_fecho
    elif opt == 2:
        opt_tag = mn.menu_tag()
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
    elif opt == 4:
        opt_pagina = mn.menu_pagina()
        sl.imprime_titulo(titulo_crawler_individual)
        if opt_pagina == 1:
            cip.pega_conteudo_brookings(page)
            sl.imprime_fecho
        #elif opt_pagina == 2:
            #cip.pega_conteudo_nytimes(page)
            #sl.imprime_fecho
        else:
            print('Opção de página inválida!')
            continue
    else:
        print('Opção inválida!')

    flag = int(input('Continuar? [0 - Não / 1 - Sim]: '))
    print('\n\n')







