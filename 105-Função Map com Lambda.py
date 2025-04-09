
# Map Function
     # Muito utilizado com listas
     # Aplicar uma função a um It erable, por item. (list, tuple, dic etc.)

lista1 = [666, 555, 999, 1579, 64357]
lista2 = [100000 - 679 - 534 - 3333 - 7554]

# def multi(x):
#    return x * 2


# lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))
print(list(map(lambda x: x * 2, lista2)))

