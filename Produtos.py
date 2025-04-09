print('Bem-Vindo à Loja de aparelhos Malucos')

def boas_vindas_1(nome, produto, preco, estoque):
    print(f'Olá, seja bem vindo, {nome}, espero que desfrute de nossos aparelhos incríveis e fascinantes')
    print(f'Temos: {produto} | preco: R${preco} | estoque: {estoque}')

# Produtos disponíveis
produtos = {
    'Manopla do infinito': {'preco': 49.99, 'estoque': 1679},
    'Besouro Azul': {'preco': 259.99, 'estoque': 3987},
    'Bombinhas de Buraco Negro': {'preco': 49.99 ,'estoque': 2598},
    'Caneca de Ouro': {'preco': 99.99, 'estoque': 3572},
    'Xbox serie X': {'preco': 2599.00, 'estoque': 9937}
}
