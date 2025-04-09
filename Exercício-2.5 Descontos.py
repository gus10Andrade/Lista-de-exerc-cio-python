valor_COMPRAS = float(input('Digite o valor: R$ '))

if valor_COMPRAS > 200:
    descontos = 0.2
elif valor_COMPRAS > 100:
    descontos = 0.1
else:
    descontos = 0.05

valor_final = valor_COMPRAS - (valor_COMPRAS * descontos)
print(f'valor_final com desconto é de R$ {valor_final:.2f}')