Nome = 'Gustavo'
Sobrenome = 'Paulo'
Profissao = 'Aprendiz'
Jogo = 'Xcom 2'
Filme = 'Zootopia'
Serie = 'The Walking Dead'

texto = 'O ' + Nome + ' ' + Sobrenome + ' e um excelente ' + '[' + Profissao + ']'

texto2 = (f'''O {Nome} {Sobrenome} e um excelente [{Profissao}] e seu Jogo Prefido é {Jogo}
e seu Filme Prefido é {Filme} e sua Serie Prefido é {Serie}''')

print(texto)
print(texto2)

# Gustavo Paulo e um otimo [Aluno]