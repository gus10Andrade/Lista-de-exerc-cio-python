from sys import getsizeof

# Generator Expressions
    # Uma forma mais rápida para Listras, dicionários e etc.
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(100000)]
print(type(numeros))
print(numeros)

print('=====')

numeros = (x * 10 for x in range(100000))
print(type(numeros))
# print(list(numeros))
print(getsizeof(numeros))