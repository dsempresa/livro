from livro.livro_buscar import buscarPorCodigo
from livro.livro_editar import editarLivro
from livro.livro_listar import listarLivros
from livro.livro_deletar import deletarLivro
from livro.livro_registrar import registrarLivro

def menu() -> None:
    while True:
        print(""""---- BEM VINDO AO MENU----
              1 - Adicionar livro
              2 - Editar livro
              3 - Deletar livro
              4 - Buscar por código
              5 - Listar todos
              6 - sair
        """)
        opcao = input('Selecione uma opção:')
        if opcao == '1':
            titulo = input('Digite o livro:')
            autor = input('Digite o autor:')
            registrarLivro(titulo, autor)
        elif opcao == '2':
            codigo = int(input('Digite o codigo:'))
            titulo = input('Digite o titulo:')
            autor = input('Digite o autor:')
            editarLivro(codigo,titulo,autor)
        elif opcao == '3':
            codigo = int(input('Digite o código:'))
            deletarLivro(codigo)
        elif opcao == '4':
            codigo = int(input('Digite o codigo:'))
            print(buscarPorCodigo(codigo))
        elif opcao == '5':
            listarLivros()
        elif opcao == '6':
            break
        else:
            print('Opção inválida"')


if __name__ == "__main__":
    menu()
