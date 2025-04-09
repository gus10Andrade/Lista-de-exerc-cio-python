# Python Object-Orientd Programming

# Classes:
         # Utilizadas para criar Objetos (instances)
         # Objetos são partes dentro de uma Class (instancias)
         # Classe são utilizadas para agrupar dados e funções, podendo reutilizar

# Criar uma Classe
class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome

# Criar o Objeto
usuario1 = Funcionarios( "Leonado", "Cabral", "(12/01/2006)")
usuario2 = Funcionarios("Elena", "Manoela", "(15/05/1996)")
usuario3 = Funcionarios( "Pablo", "Dias", "(5/09/2026)")

# Print
# print(usuario1.nome + " " +usuario1.sobrenome + ' ' + usuario1.data_nascimento)
# print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
