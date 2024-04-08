from classes import *
from variaveis_filmes import *
from objetos import *


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
