idade = int(input('Qual é sua idade: '))

if idade < 13:
    print('você é uma criança')
elif idade < 13 and idade < 20:
    print('você é um adolescente')
else:
    print('Você é um adulto')