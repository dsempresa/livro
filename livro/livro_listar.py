from repositorio.livro_repositorio import livro_repositorio

def listarLivros() -> None:
    print('Todos os livros')
    for livro in livro_repositorio:
        print(f"codigo: {livro['codigo']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Emprestado? {livro['codigo']}")
        print("-"*30)

if __name__ == "__main__":
    listarLivros()