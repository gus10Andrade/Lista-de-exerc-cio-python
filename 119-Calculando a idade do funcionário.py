from datetime import datetime

# Python Object-Orientd Programming

# Classes:
         # Utilizadas para criar Objetos (instances)
         # Objetos são partes dentro de uma Class (instancias)
         # Classe são utilizadas para agrupar dados e funções, podendo reutilizar

# Criar uma Classe
class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# Criar o Objeto
usuario1 = Funcionarios( "Leonado", "Cabral", 2006)
usuario2 = Funcionarios("Elena", "Manoela", 1996)
usuario3 = Funcionarios( "Pablo", "Dias", 2026)

# print
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))