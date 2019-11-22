def registar_realizador(mm, nome_realizador):
    realizador = {
        'nome': nome_realizador
    }
    mm['realizadores'].append(realizador)


movie_manager = {
    'realizadores': [],
    'atores': [],
    'filmes': []
}
print(movie_manager)
registar_realizador(movie_manager, 'Spielberg')
registar_realizador(movie_manager, 'Scott')
print(movie_manager)