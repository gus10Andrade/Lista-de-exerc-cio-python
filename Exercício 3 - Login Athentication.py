Usuario_1 = 'Gustavo'
Usuario_1_senha = '281022'

Usuario_2 = 'Fabio'
Usuario_2_senha = 'eu sou lindo 2012'

usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite a sua Senha: ')

if usuario == Usuario_1 and senha == Usuario_1_senha:
    print('Login OK')
elif usuario == Usuario_2 and senha == Usuario_2_senha:
    print('Login, acerto miseravel')
else:
    print('Usuário ou senha incorretos.')

Velocidade = 40
if Velocidade > 110:
  print(f'Acima da Velocidade Permitida')
elif Velocidade > 60:
  print(f'Favor Reduzir a Velocidade')
else:
 print(f'Velocide Esta Ok')