from classes import *
from variaveis_filmes import *
from variaveis_series import *
from objetos_filmes import *
from objetos_series import *
from objetos_usuarios import *
from variaveis_comentarios import *
from objetos_comentarios import *
from objetos_reviews import *


# filmes assistidos pelo cliente1
cliente1.perfil.adicionar_filme_assistido(filme1)


cliente1.perfil.adicionar_filme_assistido(filme2)

cliente1.perfil.adicionar_filme_assistido(filme6)


# filmes que o cliente1 está assistindo

cliente1.perfil.adicionar_filme_assistindo(filme9)

cliente1.perfil.adicionar_filme_assistindo(filme5)


cliente1.perfil.adicionar_filme_assistindo(filme8)


# filmes que o cliente1 planeja assistir futuramente

cliente1.perfil.adicionar_filme_a_assistir(filme3)


cliente1.perfil.adicionar_filme_a_assistir(filme4)


cliente1.perfil.adicionar_filme_a_assistir(filme7)



# series assistidas pelo cliente

cliente1.perfil.adicionar_serie_assistida(serie1)

cliente1.perfil.adicionar_serie_assistida(serie9)


cliente1.perfil.adicionar_serie_assistida(serie6)

lista_series_assistidas_cliente1 = cliente1.perfil.series_assistidas


# serie que cliente está assistindo

cliente1.perfil.adicionar_serie_assistindo(serie4)


cliente1.perfil.adicionar_serie_assistindo(serie7)

cliente1.perfil.adicionar_serie_assistindo(serie8)


lista_series_assistindo_cliente1 = cliente1.perfil.series_assistindo


# serie que cliente planeja assistir
cliente1.perfil.adicionar_serie_a_assistir(serie2)

cliente1.perfil.adicionar_serie_a_assistir(serie3)

cliente1.perfil.adicionar_serie_a_assistir(serie5)


lista_series_planeja_assistir = cliente1.perfil.series_a_assistir




# filmes assistidos pelo administrador1

administrador1.perfil.adicionar_filme_a_assistir(filme1)

administrador1.perfil.adicionar_filme_a_assistir(filme10)

administrador1.perfil.adicionar_filme_a_assistir(filme11)



# filmes que o administrador1 está assistindo


administrador1.perfil.adicionar_filme_assistindo(filme12)

administrador1.perfil.adicionar_filme_assistindo(filme13)

administrador1.perfil.adicionar_filme_assistindo(filme14)


# filmes que o administrador1 planeja assistir

administrador1.perfil.adicionar_filme_assistido(filme2)


administrador1.perfil.adicionar_filme_assistido(filme5)


administrador1.perfil.adicionar_filme_assistido(filme7)




# filmes assistidos  cliente
lista_filmes_assistidos_cliente1 = cliente1.perfil.filmes_assistidos

# filmes assistindo cliente
lista_filmes_assistindo_cliente1 = cliente1.perfil.filmes_assistindo

# filmes que planeja assistir cliente
lista_filmes_a_assistir_cliente1 = cliente1.perfil.filmes_a_assistir


# filmes assistidos administrador
lista_filmes_assistidos_administrador1 = administrador1.perfil.filmes_assistidos

# filmes assistindo administrador

lista_filmes_assistindo_administrador1= administrador1.perfil.filmes_assistindo

# filmes que o administrador planeja assistir
lista_filmes_a_assistir_administrador1 = administrador1.perfil.filmes_a_assistir


# <<< cliente >>>
print(f"\033[1;32m<<< Cliente {cliente1.nome} >>>\033[m")


# mostra filmes assistidos pelo cliente

print("\n\033[1;33m- Filmes assistidos:\033[m")

for posicao, filme in enumerate(lista_filmes_assistidos_cliente1):

    print(f"{posicao + 1} - {filme.titulo}")



# mostra filmes que o cliente está assistindo


print("\n\033[1;33m- Filmes assistindo\033[m")

for posicao, filme in enumerate(lista_filmes_assistindo_cliente1):

    print(f"{posicao + 1} - {filme.titulo}")



# mostra filmes que o cliente planeja assistir


print("\n\033[1;33m- Filmes que planeja assitir\033[m")

for posicao, filme in enumerate(lista_filmes_a_assistir_cliente1):

    print(f"{posicao + 1} - {filme.titulo}")



# séries que cliente assistiu

print("\n\033[1;33m- Séries assistidas \033[m")

for posicao, serie in enumerate(lista_series_assistidas_cliente1):


    print(f"{posicao + 1} - {serie.titulo}")


# séries que o cliente está assistindo

print("\n\033[1;33m- Séries assistindo\033[m")


for posicao, serie in enumerate(lista_series_assistindo_cliente1):

    print(f"{posicao + 1} - {serie.titulo}")


# Séries que o cliente planeja assistir


print("\n\033[1;33m- Séries que o cliente planeja assistir")

for posicao, serie in enumerate(lista_series_planeja_assistir):

    print(f"{posicao + 1} - {serie.titulo}")





# <<< Administrador >>>

print(f"\n\n\033[1;34m<<< Administrador {administrador1.nome} >>>\033[m")


# mostra filmes que o administrador1 assistiu
print("\n\033[1;33m- Filmes assistidos:\033[m")


for posicao, filme in enumerate(lista_filmes_assistidos_administrador1):

    print(f"{posicao + 1} - {filme.titulo}")



# mostra filmes que o administrador1 está assistindo


print("\n\033[1;33m- Filmes assistindo\033[m")

for posicao, filme in enumerate(lista_filmes_assistindo_administrador1):


    print(f"{posicao + 1} - {filme.titulo}")



# mostra filmes que o administrador1 planeja assistir

print("\n\033[1;33m- Filmes que planeja assitir\033[m")

for posicao, filme in enumerate(lista_filmes_a_assistir_administrador1):


    print(f"{posicao + 1} - {filme.titulo}")





# comentários

lista_comentario = [comentario1, comentario2, comentario3]


print("\n\033[1;32m<<< comentários >>>\033[m")

for posicao, comentario in enumerate(lista_comentario):

    print(f"Comentario {posicao + 1} -> {comentario.comentario}")



# reviews

lista_reviews = [review1, review2, review3]


for posica, review in enumerate(lista_reviews):

    print(f"{posicao + 1} - {review.review}")