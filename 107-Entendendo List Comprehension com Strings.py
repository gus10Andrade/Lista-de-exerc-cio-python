
# List Comprehesion
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for itens in frutas1:
#    if 'n' in itens:
#       frutas2.append(itens)


frutas2 = [iten for  iten in frutas1 if 'a' in iten]



print(frutas2)