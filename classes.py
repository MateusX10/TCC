class Interface:

    def __init__(self):

        pass


class Usuario:



    def __init__(self, id, nome, email, senha, data_nascimento, genero):

        from random import randint


        self.id = id

        self.nome = nome

        self.email = email

        self.senha = senha

        self.data_nascimento = data_nascimento

        self.genero = genero

        self.perfil = Perfil(self.id, randint(0, 10000), ["Os vingadores: guerra infinita", "Friends", "O Poderoso Chefão"], ["O Labirinto do Fauno", "The Crown", "Black Mirror"], ["Rei Leão", "Sherlock", "Madagascar"], ["ação", "comédia", "sci-fi"], ["Os Vingadores: Guerra Infinita"])
 


    
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




class Perfil:


    def __init__(self, id_perfil, id_usuario,  obras_assistidas, obras_assistindo, obras_a_assistir, generos_preferidos, obras_preferidas):

        self.id_perfil = id_perfil

        self.id_usuario = id_usuario

        self.obras_assistidas = obras_assistidas

        self.obras_assistindo = obras_assistindo

        self.obras_a_assistir = obras_a_assistir

        self.generos_preferidos = generos_preferidos

        self.obras_preferidas = obras_preferidas



    def editar_perfil(self):


        pass



    def visualizar_obras_assistida(self):

        pass


    def visualizar_obras_assistindo(self):

        pass



    def visualizar_obras_a_assistir(self):

        pass




class Filmes:


    def __init__(self, id, titulo, genero, diretor, ano_lancamento, sinopse, elenco, classificacao, duracao, average_rate, popularidade, link_trailer, poster):


        self.id = id

        self.titulo = titulo

        self.genero = genero


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


    # método "get_informacoes"
    def __str__(self):

        pass


    def get_comentarios(self):

        pass


    def get_reviews(self):


        pass





class Series:

    def __init__(self, id, titulo, genero, numero_episidios, numero_temporadas, ano_lancamento, diretor, sinopse, elenco, classificacao, duracao, average_rate, popularidade, link_trailer, poster):


        self.id = id


        self.titulo = titulo


        self.genero = genero


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


    def __init__(self, tema_do_sistema, idioma_do_sistema, email_do_usuario, texto_de_politica_de_privacidade, texto_de_politica_de_cookies):


        self.tema_do_sistema = tema_do_sistema

        self.idioma_do_sistema = idioma_do_sistema


        self.email_do_usuario = email_do_usuario

        self.texto_de_politica_de_privacidade =  texto_de_politica_de_privacidade


        self.texto_de_politica_de_cookies = texto_de_politica_de_cookies

