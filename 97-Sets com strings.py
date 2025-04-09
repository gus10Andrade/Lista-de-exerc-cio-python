
# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Nâo utiliza index




set1 = {'A', 'B', 'C'}
set2 = {'A', 'D', 'E'}
set3 = {'C', 'D', 'F'}

set4 = set1.symmetric_difference(set3)
# set4 = set1.intersection(set2)
# set4 = set1.difference(set3)
# set4 = set1.union(set2)

print(set4)
