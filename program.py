import movie_manager

def main():
    mm = {
        'realizadores': [],
        'atores': [],
        'filmes': []
    }
    print(mm)
    movie_manager.registar_realizador(mm, 'Spielberg')
    print(mm)
    movie_manager.registar_ator(mm, 'João')
    print(mm)

if __name__ == "__main__":
    main()