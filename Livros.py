def boas_vindas_1(nome, titulo, escrito, quantidade, publicado):
    print(f'Olá, seja bem-vindo, {nome}')
    print(f'Temos: {titulo} | Escrito: {escrito} | Publicação: {publicado} | Quantidade: {quantidade}')

livros = [
    {'Titulo': 'Conjurador O aprendiz (Vol. 1)', 'Escrito': 'Taran Matharu', 'Publicado': 2015, 'Estoque': 145},
    {'Titulo': 'Academia dos Magos - Crônicas do Multiverso', 'Escrito': 'M.F Pettersen', 'Publicado': 2022, 'Estoque': 250},
    {'Titulo': 'Eu Sou a Lenda', 'Escrito': 'Richard Matheson', 'Publicado': 1954, 'Estoque': 235}
]

# Exibindo a lista de livros disponíveis
print("Livros Disponíveis:")
for i, livro in enumerate(livros):
    print(f"{i + 1}. {livro['Titulo']}")

# Capturando a escolha
escolha = int(input("Digite o número do livro que você deseja ver as informações: ")) - 1

# Verificando se a escolha é válida
if 0 <= escolha < len(livros):
    livro_escolhido = livros[escolha]
    boas_vindas_1('Visitante', livro_escolhido['Titulo'], livro_escolhido['Escrito'], livro_escolhido['Estoque'], livro_escolhido['Publicado'])
else:
    print("Escolha inválida. Por favor, tente novamente.")