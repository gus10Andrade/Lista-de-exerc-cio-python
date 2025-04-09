# == for loop nested ===
# Outer loop
# Inner loop

'''''
Criar um retoangulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''''

linhas = 7
colunas = 200
simbolo = '01001'

for l in range(linhas):
    for c in range(colunas):
          print(simbolo, end="")
    print()