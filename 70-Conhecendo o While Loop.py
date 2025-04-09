# == While Loops ===
# Excelente para loops dependentes de uma condição.
# Criar uma promoção para um produto no valor de R$100.

valor = 100
Dia = 0
while valor > 0:
    Dia += 1
    print(f'No dia {Dia} o poduto vai ser vendido por R$ {valor}')
    valor -= 1