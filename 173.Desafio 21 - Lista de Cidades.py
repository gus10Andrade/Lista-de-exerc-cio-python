cidades = ("São Paulo", "Rio de Janeiro" , "Belo Horizonte")
cidades_usuario = input('Adivinhe o nome cidade: ')

if cidades_usuario in cidades:
 print("A cidade existe ")
else:
    print('Essa cidade não existe')