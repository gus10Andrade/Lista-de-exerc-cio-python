

# Unpacking Lists
     # Armazenar mais de uma informação em variáveis
     # Manter a senquencia dos dados em uma variável


produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]
#items          0         1         2         3

item1, item2, item3, *item4 = produtos

#item1 = produtos[0]
#item2 = produtos[1]
#item3 = produtos[2]
#item4 = produtos[3]

print(produtos)
#print(item1)
#print(item2)
#print(item3)
#print(item4)