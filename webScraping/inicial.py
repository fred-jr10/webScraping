import scrapLibrary as sl

#Página de teste1 --> 'http://www.pythonscraping.com/pages/page3.html'
#Página de teste 2 --> ''

page = input('Digite a página a ser explorada: ')
#tag = input('Digite a tag HTML [div/h1/h2/h3/title]: ')
tags = sl.verifica_erro_pagina(page)

titulo_pega_conteudo_tags = 'PEGANDO CONTEÚDO DAS TAGS ANINHADAS'
titulo_pega_tags = 'PEGANDO O CONTEÚDO DA TAG SELECIONADA'
titulo_mostra_imagens = 'EXIBINDO A LISTA DE IMAGENS DO SITE'

#sl.imprime_titulo(titulo_pega_conteudo_tags)
#sl.pega_tags_filho(tags)
#sl.pega_tags_irmao(tags)
#sl.pega_tags_descendente(tags)
#sl.imprime_fecho

#sl.imprime_titulo(titulo_pega_conteudo_tags)
#sl.pega_conteudo_tags(tag, tags)
#sl.imprime_fecho

sl.imprime_titulo(titulo_mostra_imagens)
sl.mostra_imagens(tags)
sl.imprime_fecho
