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

def registar_filme(mm, titulo, genero, nome_realizador):
    # Pesquisar realizador com base no nome
    realizador = None
    for r in mm['realizadores']:
        if r['nome'] == nome_realizador:
            realizador = r
            break
    if realizador is None:
        # Se o realizador não existir, falha
        return None
    else:
        # Se o realizador existir, adiciona filme
        filme = {
            'titulo': titulo,
            'genero': genero,
            'rating': 0.0,
            'sinopse': "",
            'realizador': realizador,
            'atores': []
        }
        mm['filmes'].append(filme)
        return filme
