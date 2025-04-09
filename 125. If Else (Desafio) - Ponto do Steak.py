# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do streak ele retorna o ponto de cozimento em portugues.
O usuario deverá fornecer temperatura.

Temperaturas - Cozimento 
120 F ou 48 C - Rare (Selada)
130 F ou 54 C - Medium rare (Ao ponto para o Mal)
140 F ou 60 C - Medium (Ao ponto)
150 F ou 65 C - Medium Well (Ao ponto para o Bem)
160 F ou 71 C - Well done (Bem passada)
'''

# temperaturas = int(input("Qual é a Temperatura da Carne: "))

# if 48 <= temperaturas <= 54:
#    print("Rare (Selada)")
# elif 54 <= temperaturas <= 60:
#    print("Medium rare (Ao ponto para o Mal)")
# elif 60 <= temperaturas <= 65:
#    print("Medium (Ao ponto)")
# elif 65 <= temperaturas <= 70:
#    print("Medium Well (Ao ponto para o Bem)")
# elif 70 <= temperaturas <= 79:
#    print("Well done (Bem passada)")
# else:
#    print("estragou")

tem_cel = int(input("Qual é a Temperatura da Carne: "))

if tem_cel < 48:
    print('Cozinhar por mais alguns minutos')
elif tem_cel in range(48, 53):
    print('Selada')
elif tem_cel in range(54, 59):
    print('Ao ponto para o Mal')
elif tem_cel in range(60, 64):
    print('Ao ponto')
elif tem_cel in range(65, 70):
    print('Ao ponto para o Bem')
else:
    print('Bem passada')