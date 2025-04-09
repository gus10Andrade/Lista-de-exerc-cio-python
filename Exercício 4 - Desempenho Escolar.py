Nota_Aluno = int(input('Digite a nota do Aluno: '))

if  Nota_Aluno >= 9:
    print('Excelente, você tirou um A')
elif Nota_Aluno >= 7:
    print('Bom Trabalho, Você tirou um B')
elif Nota_Aluno >= 5:
    print('Você Passou, mas precisa melhorar, Sua nota é C')
else:
    print('Reprovado')