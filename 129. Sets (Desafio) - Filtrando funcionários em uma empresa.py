# Desafio com 'Sets'

'''''
Criar um programa que gera 3 lista de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham o dia
Lista3 = Funcionários que não tem carro

'''''

funcioarios = ["Ana","Marcos","Alice","Pedro","Sophia","Bruno","Melissa"]
turno_dia = ["Ana","Marcos","Alice","Melissa"]
turno_noi = ["Pedro","Sophia","Bruno"]
tem_carro = ["Marcos","Alice","Bruno","Melissa"]

Lista1 = [funcioarios for funcioarios in turno_noi if funcioarios in tem_carro]
print(f'Funcionários que tem carro e trabalham a noite São {Lista1}')
Lista2 = [funcioarios for funcioarios in turno_dia if funcioarios in turno_dia]
print(f'Funcionários que tem carro e trabalham o dia {Lista2}')
Lista3 = [funcioarios for funcioarios in funcioarios if funcioarios not in tem_carro]
print(f'Funcionários que não tem carro {tem_carro}')

# Esse exemplo abaixou e do professor
# Lista1
# Lista1 = set(tem_carro).intersection(turno_noi)
# print(Lista1)
# #Lista2
# Lista2 = set(tem_carro).intersection(turno_dia)
# print(Lista2)
# Lista3
# Lista3 = set(tem_carro).intersection(funcioarios)
# print(Lista3)
