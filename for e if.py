# enviar um email com os detalhes da compra online (Maximo 3 tentativas) para compras confirmadas

compra_corfimada = True
dados_compra = 'Compra no valor de R$12,50 e entrega confimada'

for enviar in range(3):
    if compra_corfimada:
       print(dados_compra)
       print('Detalhes enviados para o seu email')
       break
else:
  print('Falha na compra')