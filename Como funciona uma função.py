# Functions (Funções)
# DRY - Don't repeat yourself
# Parametro --> Argumento
# Default = aquele que você define o valor no parametro
# Non-Default = aquele que você não define o valor no parametro

def boas_vindas(nome, quantidade, jogos):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')
    print(f'Temos {jogos} jogos no momento')

boas_vindas('Gustavo Lindo', 5, 8 )
boas_vindas('Ryan', 4, 6 )
boas_vindas('Fabio', 3, 4)
boas_vindas('Larissa', 2, 3 )
boas_vindas('Jian', 1, 2)
boas_vindas('Chales', 0, 0 )

'''''
def boas_vindas_Gustavo():
    print('Olá, Gustavo!')
    print('Termos 5 Laptopd em estoque')


def boas_vindas_Larissa():
    print('Olá, Larissa!')
    print('Termos 4 Laptopd em estoque')

def boas_vindas_Ryan():
    print('Olá, Ryan!')
    print('Termos 3 Laptopd em estoque')

def boas_vindas_Fabio():
    print('Olá, Fabio!')
    print('Termos 2 Laptopd em estoque')

def boas_vindas_Jian():
    print('Olá, Jian!')
    print('Termos 1 Laptopd em estoque')

def boas_vindas_Chales():
    print('Olá, Chales!')
    print('Não Termos Laptopd em estoque')

boas_vindas_Gustavo()
boas_vindas_Ryan()
boas_vindas_Larissa()
boas_vindas_Jian()
boas_vindas_Fabio()
boas_vindas_Chales()
'''''