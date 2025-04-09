nome = input('Digite o seu nome: ')
Idade = int(input('Digite o seu idade: '))

# A Baixo Captura do valor do Produto
Valor_prod = float(input('Digite o valor do seu produto: R$ '))

# Calcula o valor com 10% pode ser 20% de acréscimo
Valor_com_Acre = Valor_prod * 1.20

#Type ele saber qual é o int, str, float etc.
# Quando usar a formula |Print(type(nome))
print(nome)
print(Idade)
# Exibir o Valor Final na Tela
print(f'O valor final do produto, com acréscimo é: R$ {Valor_com_Acre:.2f}')