
# Functions (Funções)
     # DRY - Don't repeat yourself.
     # Realizam uma tarefa
     # Calcula e retorna em Valor


def cliente1():
    numer1 = 1045
    numer2 = 1030
    resul = numer1 % numer2
    print(resul)



def cliente2():
    numero1 = 46
    numero2 = 79
    resultado = numero1 * numero2
    return f'Resltado:{resultado}'

Y = cliente1()
X = cliente2()

print(Y)
print(X)