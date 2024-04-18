class Interface:

    def __init__(self):


        # elementos a serem inseridos na interface.Os elementos a serem inseridos na interface podem ser: configuracao (apenas uma), administradores, clientes, perfis, filmes ou séries (comentários e reviews já estão contidos em filmes e séries e, logo, são excluidos)
        self.elementos = {"configuração": [], "administradores": [], "clientes": [],  "filmes": [], "series": []}


    def adicionar_elemento(self, tipo_de_elemento, elemento)-> None:
        '''-> Adiciona um elemento à interface

            Parâmetros:

                tipo_de_elemento(str): o tipo de elemento a ser adicionado (filme, série, administrador, cliente, filmes, series)
                return: sem retorno


            Tipos de elemento:

                - configuração, administradores, clientes, perfis, filmes, series
        '''

        
        self.elementos[tipo_de_elemento].append(elemento)




class Perfil:


    def __init__(self, id_perfil, id_usuario,  generos_preferidos):

        self.id_perfil = id_perfil

        self.id_usuario = id_usuario

        self.filmes_assistidos = []

        self.filmes_assistindo = []


        self.filmes_a_assistir = []

        self.series_assistidas = []

        self.series_assistindo = []

        self.series_a_assistir = []

        self.filmes_preferidos = []


        self.series_preferidas = []

        self.generos_preferidos = generos_preferidos




    def adicionar_filme_assistido(self, filme_assistido):

        self.filmes_assistidos.append(filme_assistido)


    def adicionar_filme_assistindo(self, filme_assistindo):

        self.filmes_assistindo.append(filme_assistindo)


    def adicionar_filme_a_assistir(self, filme_a_assistir):

        self.filmes_a_assistir.append(filme_a_assistir)


    def adicionar_serie_assistida(self, serie_assistida):


        self.series_assistidas.append(serie_assistida)


    def adicionar_serie_assistindo(self, serie_assistindo):

        self.series_assistindo.append(serie_assistindo)


    def adicionar_serie_a_assistir(self, serie_a_assistir):


        self.series_a_assistir.append(serie_a_assistir)




class Usuario:



    def __init__(self, id, nome, email, senha, data_nascimento, genero):

        from random import randint


        self.id = id

        self.nome = nome

        self.email = email

        self.senha = senha

        self.data_nascimento = data_nascimento

        self.genero = genero

        self.perfil = Perfil(self.id, randint(0, 10000), ["ação", "aventura", "comédia"])
 


  
    def cadastrar(self):

        pass


    def logar(self):

        pass

    
    def editar_perfil(self):

        pass


    def excluir_perfil(self):

        pass


    def get_filmes_recomendados(self):

        pass


    def avaliar_obra(self):

        pass


    def comentar_obra(self):

        pass


    def get_historico(self):

        pass




class Cliente(Usuario):


    def __init__(self, id, nome, email, senha, data_nascimento, genero):

        super().__init__(id, nome, email, senha, data_nascimento, genero)





class Administrador(Usuario):


    def __init__(self, id, nome, email, senha, data_nascimento, genero):


        super().__init__(id, nome, email, senha, data_nascimento, genero)


    def gerenciar_usuarios(self):

        pass

    def gerenciar_obras(self):

        pass

    def gerenciar_recomendacoes(self):

        pass


    def gerar_relatorio(self):

        pass








    def editar_perfil(self):


        pass



    def visualizar_obras_assistida(self):

        pass


    def visualizar_obras_assistindo(self):

        pass



    def visualizar_obras_a_assistir(self):

        pass




class Filme:


    def __init__(self, id, titulo, generos: list, diretor: list, ano_lancamento, sinopse, elenco: list, classificacao, duracao, average_rate, popularidade, link_trailer, poster):


        self.id = id

        self.titulo = titulo

        self.generos = generos


        self.diretor = diretor


        self.ano_lancamento = ano_lancamento

        self.sinopse = sinopse


        self.elenco = elenco

        self.classificacao = classificacao

        self.duracao = duracao

        self.average_rate = average_rate

        self.popularidade = popularidade


        self.link_trailer = link_trailer

        self.poster = poster

        self.comentarios = []

        self.reviews = []


    # método "get_informacoes"
    def __str__(self):

        pass


    def adicionar_comentario(self, id_comentario, id_usuario, id_obra,  comentario, data_comentario):

        id_obra = self.id

        comentario = Comentarios(id_comentario, id_usuario, id_obra, comentario, data_comentario)

        self.adicionar_comentario(comentario)


    def get_comentarios(self):

        pass


    def get_reviews(self):


        pass





class Series:

    def __init__(self, id, titulo, generos: list, numero_episidios, numero_temporadas, ano_lancamento, diretor: list, sinopse, elenco: list, classificacao, duracao, average_rate, popularidade, link_trailer, poster):


        self.id = id


        self.titulo = titulo


        self.generos = generos
    

        self.numero_episodio = numero_episidios

        self.numero_temporadas = numero_temporadas

        self.ano_lancamento = ano_lancamento

        self.diretor = diretor


        self.sinopse = sinopse


        self.elenco = elenco


        self.classificacao = classificacao

        self.duracao = duracao


        self.average_rate = average_rate


        self.popularidade = popularidade


        self.link_trailer = link_trailer

        self.poster = poster

        self.comentarios = []

        self.reviews = []


    # método "get_informacoes"
    def __str__(self):

        pass


    def get_comentarios(self):

        pass


    def get_reviews(self):


        pass



class Comentarios:

    def __init__(self, id_comentario, id_usuario, id_obra, comentario, data_do_comentario):


        self.id_comentario = id_comentario

        self.id_usuario = id_usuario

        self.id_obra = id_obra

        self.comentario = comentario


        self.data_do_comentario = data_do_comentario



    def criar_comentario(self):

        pass



    def editar_comentario(self):

        pass


    def excluir_comentario(self):


        pass


class Review:

    def __init__(self, id_review, id_usuario, id_obra, review, recomendado, data_review, review_rate):

        self.id_review = id_review

        self.id_usuario = id_usuario

        self.id_obra = id_obra


        self.review = review

        self.recomendado = recomendado

        self.data_review = data_review

        self.review_rate = review_rate



    def criar_review(self):


        pass

    def editar_review(self):


        pass



    def excluirReview(self):


        pass


    def dar_nota_a_review(self):

        pass








class Configuracoes:


    def __init__(self, tema_do_sistema, idioma_do_sistema, email_do_usuario, texto_de_politica_de_privacidade):


        self.tema_do_sistema = tema_do_sistema

        self.idioma_do_sistema = idioma_do_sistema


        self.email_do_usuario = email_do_usuario

        self.texto_de_politica_de_privacidade =  texto_de_politica_de_privacidade



