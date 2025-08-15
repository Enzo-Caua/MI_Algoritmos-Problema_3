import random


# Cria matrizes de N x N espaços
def criar_matrizes():
    valido = False
    matriz = {}

    while not valido:
        try:
            linhas = int(input('Informe a quantidade de linhas: '))
            colunas = int(input('Informe a quantidade de colunas: '))
            valido = True
        except ValueError:
            print()

    for l in range(linhas):
        for c in range(colunas):
            matriz[(l, c)] = random.randint(1,9)

    for l in range(linhas):
        for c in range(colunas):
            print('|', end='')
            print(f'{matriz[(l, c)]:^10}', end='')
        print('|')


criar_matrizes()