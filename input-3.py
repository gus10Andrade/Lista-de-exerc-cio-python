# Multiplas entradas na mesma linha de input()

Dados = input('Digite o seu nome, idade e Altura: ').split() # Gustavo 21 165
nome = Dados[0]
Idade = Dados[1]
Altura = Dados[2]

print(f'Meu nome é {nome.upper()}, tenho {Idade} anos de Idade e minha altura é de {Altura} centimetro.')