# Funções
def registar_realizador(mm, nome_realizador):
    realizador = {
        'nome': nome_realizador
    }
    mm['realizadores'].append(realizador)

def registar_ator(mm, nome_ator):
    ator = {
        'nome': nome_ator
    }
    mm['atores'].append(ator)

# Utilização
movie_manager = {
    'realizadores': [],
    'atores': [],
    'filmes': []
}
print(movie_manager)
registar_realizador(movie_manager, 'Spielberg')
print(movie_manager)
registar_ator(movie_manager, 'João')
print(movie_manager)