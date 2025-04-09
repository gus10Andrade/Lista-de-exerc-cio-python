
# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...


#         Keys | Values
aluno = {'nome': 'Ana',
         'idade': 16,
         'nota_final': 'A',
         'aprovação': True
}

# aluno['nome'] = 'Jose'
# aluno.update({'nome': 'Jose', 'nota_final' : 'B'})
# aluno.update({'endereço': 'Rua A'})
#print(aluno.get('endereco', 'Não existe'))
del aluno['idade']
print(aluno)