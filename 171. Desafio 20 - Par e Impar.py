# lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numero = list(range(1,11))

for i in lista_numero:
    if i % 2 == 0:
        print(f'O número {i} e par!')
    else:
        print(f'O número {i} impar!')