
# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Nâo utiliza index


list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union ele unificar
print(num1 - num2) # Differend
print(num1 ^ num2) # Symmeti Differend
print(num1 & num2) # And
print(len(num1))
print(num1[1])