
# Functions (Funções)
     # DRY - Don't repeat yourself.
     # Vários Argumentos (xargs) identificando o Parametro.

# Criar uma função que armazena numeros e strings (dados)


def agencia(**carro):
    return  carro


print(agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))
print(agencia(marca='Camaro', cor='Amarelho', motor=5.0, placa=2890))
print(agencia(marca='Onix', cor='Preto', motor=8.0, placa=5489))
print(agencia(marca='Zodiaco', cor='Vermelho', motor=11.0, placa=5899))
print(agencia(marca='Fusca', cor='Rosa', motor=1.0, placa=2315))
