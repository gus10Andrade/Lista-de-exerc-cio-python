
# Functions (Funções)
     # DRY - Don't repeat yourself.
     # Vários Argumentos (xargs)

# Criar uma função que soma vários números.

def soma(*numeros1):
    resultado = 5
    for num in numeros1:
        resultado *= num
    return resultado

def soma2(*numero2):
    resultado2 = 10
    for sekiro in numero2:
        resultado2 *= sekiro
    return resultado2

def soma3(*numero3):
    total = 20
    for sol in numero3:
        total += sol
    return total

def soma4(*numero4):
    total2 = 30
    for sol2 in numero4:
        total2 *= sol2
    return total2

X = soma(9, 5, 4, 7)
Y = soma2(10, 10, 7, 9)
Z = soma3(200, 50, 70)
A = soma4(100, 20, 50, 235)

print(X)
print(Y)
print(Z)
print(A)