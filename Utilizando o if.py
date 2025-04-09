
idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Menor de Idade')
elif 18 <= idade < 60:
    print('Maior de Idade')
else:
    print('Idoso')

# Logical Operadores (Operadores Logicos)
Renda_Acima_5mil = False
Nome_Limpo = False

if Renda_Acima_5mil or Nome_Limpo:
    print('Finaciamento Aprovado')
else:
  print('Finaciamento Negado')