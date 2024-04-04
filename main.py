from classes import *
from variaveis import *




filme1 =   Filme(id_filme1, nome_filme1, generos_filme1, ano_lancamento_filme1, diretores_filme1, sinopse_filme1, elenco_filme1, classificacao_filme1, duracao_filme1, average_rate_filme1, popularidade_filme1, link_trailer_filme1, poster_filme1)

cliente1 = Cliente(1, "Pedro", "pedro@email.com", "jdjdhd89812", '09/12/2000', 'M')


administrador1 = Administrador(1, "Roberto", "roberto@email.com", "dXjq93-1~]S/?", '12/03/1991', "M")


cliente1.perfil.adicionar_filme_assistido(filme1)


print(cliente1.nome)


lista_filmes = cliente1.perfil.filmes_assistidos


for filme in lista_filmes:

    print(filme.titulo)

#print(cliente1.perfil.filmes_assistidos[0].titulo)


print(administrador1.nome)


