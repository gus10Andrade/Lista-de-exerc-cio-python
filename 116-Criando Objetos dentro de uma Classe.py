
# Python Object-Orientd Programming

# Classes:
         # Utilizadas para criar Objetos (instances)
         # Objetos são partes dentro de uma Class (instancias)
         # Classe são utilizadas para agrupar dados e funções, podendo reutilizar

# Criar uma Classe
class Funcionarios:
    pass

# Criar o Objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# Criar os Paramentros
usuario1.nome = "Leonado"
usuario1.sobrenome = "Cabral"
usuario1.data_nascimento = "(12/01/2006)"

usuario2.nome = "Elena"
usuario2.sobrenome = "Manoela"
usuario2.data_nascimento = "(15/05/1996)"

# print
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
print('==')
print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.data_nascimento)
