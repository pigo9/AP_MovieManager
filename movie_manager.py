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
    pass
