paises = {'Brasil', 'Estados Unidos', 'Canada', 'Russia', 'Japão'}
paises_usuario = input('Qual é o paises que você veio: ')

if paises_usuario in paises:
    print(f'Você escolheu {paises_usuario}, que está na lista de países.')
else:
    print(f'{paises_usuario} não está na lista de países.')
