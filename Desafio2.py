# Carrinhos de Livros
biblioteca = []

# Lista para armazenar os livros
livros = [
    {'Título': 'Conjurador O aprendiz (Vol. 1)', 'Autor': 'Taran Matharu', 'Ano': 2015, 'Estoque': 145},
    {'Título': 'Academia dos Magos - Crônicas do Multiverso', 'Autor': 'M.F Pettersen', 'Ano': 2022, 'Estoque': 250},
    {'Título': 'Eu Sou a Lenda', 'Autor': 'Richard Matheson', 'Ano': 1954, 'Estoque': 235}
]

# Dicionário para armazenar as operações realizadas
operacoes = {
    "adicionar": [],
    "remover": [],
    "listar": [],
    "empresta": []
}

def menu():
    while True:
        print('Bem-Vindo à Biblioteca de São Paulo')
        print("\nMenu:")
        print("1.Adicionar livro")
        print("2.Remover Livro")
        print("3.Listar livros")
        print("4.empresta livros")
        print("5.Exibir informações livro")
        print("6.Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            remover_livro()
        elif opcao == '3':
            listar_livros()
        elif opcao == '4':
            emprestar_livro()
        elif opcao == '5':
            exibir_informacoes_livro()
        elif opcao == '6':
            print("Saindo do programa")
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_informacoes_livro():
    print("Livros Disponíveis:")
    for i, livro in enumerate(livros):
        print(f"{i + 1}. {livro['Título']}")
    try:
        escolha = int(input("Digite o número do livro que você deseja ver as informações: ")) - 1
        if 0 <= escolha < len(livros):
            livro_escolhido = livros[escolha]
            boas_vindas_1('Visitante', livro_escolhido['Título'], livro_escolhido['Escrito'], livro_escolhido['Estoque'], livro_escolhido['Publicado'])
        else:
            print("Escolha inválida. Por favor, tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número, tente novamente.")

def boas_vindas_1(nome, titulo, escrito, quantidade, publicado):
    print(f'Olá, seja bem-vindo, {nome}')
    print(f'Temos: {titulo} | Escrito: {escrito} | Publicação: {publicado} | Quantidade: {quantidade}')

def adicionar_livro():
    titulo = input("Digite o Título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação: ")
    quantidade = int(input("Digite a quantidade disponível: "))
    livro = {'Título': titulo, 'Autor': autor, 'Ano': ano, 'Estoque': quantidade}
    livros.append(livro)
    operacoes['adicionar'].append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def remover_livro():
    titulo = input("Digite o Título do livro a ser removido: ")
    for livro in livros:
        if livro['Título'] == titulo:
            livros.remove(livro)
            operacoes['remover'].append(livro)
            print(f'Livro "{titulo}" removido com sucesso!')
            return

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("Lista de livros:")
        for livro in livros:
            print(f'Título: {livro["Título"]}, Autor: {livro["Autor"]}, Ano: {livro["Ano"]}, Estoque: {livro["Estoque"]}')
        operacoes['listar'].append([livro["Título"] for livro in livros])

def exibir_livro():
    print("Livros disponiveis: ")
    for livro in livros:
        print(f"{livro['Título']}, Escrito: {livro['Escrito']} | Estoque: {livro['Estoque']}")

def emprestar_livro():
    titulo = input("Digite o título do livro que deseja emprestar: ")
    quantidade_emprestada = int(input("Digite a quantidade a ser emprestar: "))
    adicionar_ao_emprestimo(titulo, quantidade_emprestada)

def adicionar_ao_emprestimo(titulo, quantidade_emprestada):
    for livro in livros:
        if livro["Título"].lower() == titulo.lower():
            if livro["Estoque"] >= quantidade_emprestada:
                biblioteca.append({
                    "Título": titulo,
                    "Quantidade_emprestada": quantidade_emprestada
                })
                livro["Estoque"] -= quantidade_emprestada
                print(f"{quantidade_emprestada}x {titulo} adicionado ao carrinho.")
                return
            else:
                print("Quantidade insuficiente em estoque.")
                return
    print('Produto está indisponível.')

def devolver_livros(titulo, quantidade_devolvida):
    for item in biblioteca:
        if item["Título"].lower() == titulo.lower():
            if item.get("Quantidade_emprestada", 0) >= quantidade_devolvida:
                item["Quantidade_emprestada"] -= quantidade_devolvida
                for livro in livros:
                    if livro["Título"] == titulo:
                        livro["Estoque"] += quantidade_devolvida
                        break
                if item["Quantidade_emprestada"] == 0:
                    biblioteca.remove(item)
                print(f'{quantidade_devolvida} x {titulo} devolvido à biblioteca.')
                return
            else:
                print("Quantidade devolvida maior do que a emprestada.")
                return
    print("Livro não encontrado no registro de empréstimos.")

# Execute o menu
menu()