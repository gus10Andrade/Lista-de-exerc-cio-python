# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para
pinta uma parede. Ousuário deverá fornecer as senguintes
inforções:Rendimento, altura e largura.
Deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''


rendimento = int(input("Qual é o rendimento da lata?: "))
altura = int(input("Qual é a altura da parede?: "))
largura = int(input("Qual é a largura da parede?: "))

def calculo_tinta():
    area = altura * largura
    total =  area / rendimento
    print(f'Você necessita de {total} latas de tinta')

calculo_tinta()
