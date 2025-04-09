

# Unpacking Lists
     # Armazenar mais de uma informação em variáveis
     # Manter a senquencia dos dados em uma variável

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('EM ESTOQUE')
else:
    print('NÂO TEMOS EM ESTOQUE')