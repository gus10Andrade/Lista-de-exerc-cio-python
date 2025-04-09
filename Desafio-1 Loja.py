import Produtos

# Carrinho de compras
carrinho = {}

# Função para exibir produtos
def exibir_produtos():
    for produto, in Produtos.produtos:
        print(f'{produto} - preco: R${["preco"]} | estoque: {["estoque"]}')

# Função para adicionar ao carrinho
def adicionar_ao_carrinho(produto, quantida):
    if produto in Produtos.produtos and Produtos.produtos[produto]['estoque'] >= quantida:
        if produto in carrinho:
            carrinho[produto] += quantida
        else:
            carrinho[produto] = quantida
        Produtos.produtos[produto]['estoque'] -= quantida
        print(f'{quantida} x {produto} adicionado ao carrinho.')
    else:
        print('Produto não disponível ou quantidade insuficiente em estoque.')

# Função para exibir total da compra
def exibir_total():
    total = sum(Produtos.produtos[produto]['preco'] * quantida for produto, quantida in carrinho.items())
    print(f'Total da compra: R${total:.2f}')
    return total

# Programa principal
nome_cliente = 'Cliente Maluco'
Produtos.boas_vindas_1(nome_cliente, list(Produtos.produtos.keys()),
[info['preco']for info in Produtos.produtos.values()],
[info['estoque'] for info in Produtos.produtos.values()])

while True:
    print('\nProdutos disponíveis:')
    exibir_produtos()
    escolha = input('Digite o nome do produto para adicionar ao carrinho (ou "sair" para encerrar): ')
    if escolha.lower() == 'sair':
        break
    quantidade = int(input('Digitite a quantidade: '))
    adicionar_ao_carrinho(escolha, quantidade)

total_gasto = exibir_total()
print('Obrigado por comprar conosco!')