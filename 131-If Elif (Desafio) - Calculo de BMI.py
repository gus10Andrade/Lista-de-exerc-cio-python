# Calculo de IMC - Índice de Massa Corporal


altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em Kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
   print('Magreza')
elif IMC <= 18.5 and IMC < 24.9:
   print('NORMAL')
elif IMC <= 25.0 and IMC < 29.9:
    print('SOBREPESO')
elif IMC <= 30.0 and IMC < 34.9:
    print('OBESIDADE I')
elif IMC <=  35.0 and IMC < 39.9:
    print('OBESIDADE II')
else:
    print('OBESIDADE III')


# MENOR QUE 18,5 MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 OBESIDADE
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0    OBESIDADE GRAVE

'''''
peso = float(input('Qual é o seu peso em Kg: '))

if peso < 18.5:
    print('MAGREZA')
elif 18.5 <= peso < 24.9:
    print('NORMAL')
elif 25 <= peso < 29.9:
    print('SOBREPESO')
elif 30 <= peso < 34.9:
    print('OBESIDADE I')
elif 35 <= peso < 39.9:
    print('OBESIDADE II')
else:
    print('OBESIDADE III')
'''''