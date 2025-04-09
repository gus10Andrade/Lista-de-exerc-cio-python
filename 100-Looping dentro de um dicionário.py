
# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...



aluno ={'nome': 'Ana',
        'idade': 16,
        'nota_final': 'A',
        'aprovação': True
}

#for x in aluno.keys():
#for x in aluno.values():
for keys, values in aluno.items():
 print(keys, values)