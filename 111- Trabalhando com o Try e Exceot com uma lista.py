
# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
     letras = ['a', 'b', 'c']
     forma = ["A", "B", "C"]
     print(letras[3])
except IndexError:
     print('Index não existe')