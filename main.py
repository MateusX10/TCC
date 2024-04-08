from classes import *
from variaveis_filmes import *
from objetos import *



cliente1.perfil.adicionar_filme_assistido(filme1)


cliente1.perfil.adicionar_filme_assistido(filme2)


administrador1.perfil.adicionar_filme_assistido(filme2)

administrador1.perfil.adicionar_filme_a_assistir(filme1)


lista_filmes_assistidos_cliente1 = cliente1.perfil.filmes_assistidos


print(f"Cliente {cliente1.nome} assistiu aos seguintes filmes:")


for posicao, filme in enumerate(lista_filmes_assistidos_cliente1):

    print(f"{posicao + 1} - {filme.titulo}")


#print(cliente1.perfil.filmes_assistidos[0].titulo)


lista_filmes_assistidos_administrador1 = administrador1.perfil.filmes_assistidos


print(f"Administrador {administrador1.nome} assistiu aos seguintes filmes:")


for posicao, filme in enumerate(lista_filmes_assistidos_administrador1):

    print(f"{posicao + 1} - {filme.titulo}")


