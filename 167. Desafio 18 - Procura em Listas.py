estoque = ['BMW X6', 'BMW I5', 'BMW I8']
pesquisa_carro = input('Digite o carro desejado: ')

if pesquisa_carro in estoque:
    print('O carro está disponível em estoque')
else:
    print('O carro não está disponível em estoque')