import random

cor = {
    'base': '\033[m',
    'pt': '\033[30m',
    'vm': '\033[31m',
    'vd': '\033[32m',
    'am': '\033[33m',
    'az': '\033[34m',
    'ma': '\033[35m',
    'ci': '\033[36m',
    'bc': '\033[37m',
    '__': '\033[4m'
}


# Cria matrizes de N x N espaços
def criar_matrizes():
    valido = False
    matriz = {}
    linhas = colunas = 0

    while not valido:
        try:
            linhas = int(input('Informe a quantidade de linhas: '))
            colunas = int(input('Informe a quantidade de colunas: '))
            valido = True
        except ValueError:
            print()

    for l in range(linhas):
        for c in range(colunas):
            matriz[(l, c)] = random.randint(1, 9)

    for l in range(linhas):
        for c in range(colunas):
            print('|', end='')
            print(f'{matriz[(l, c)]:^10}', end='')
        print('|')


# Valida a entrada do usuario
def validar_escolha_usuario(opcoes):
    escolha = 0
    while escolha not in opcoes:
        try:
            escolha = input(f'{cor["ci"]}Escolha uma opção: ')
            if escolha not in opcoes:
                raise IndexError
        except ValueError:
            print(f'{cor["vm"]}Atenção: Entrada invalida!')
        except IndexError:
            print(f'{cor["vm"]}Atenção: Opção invalida!')
    return escolha


# Exibe as opçoes do menu inicial
def exibir_menu_principal():
    encerrar = False

    while not encerrar:

        print(f'\n{cor["ma"]}{" MENU PRINCIPAL ":=^43}')
        print(f'{cor["ci"]}'
              'Escolha a opção que deseja executar:\n\n'
              '[ 1 ] Iniciar Novo Jogo\n'
              '[ 2 ] Continuar Jogo\n'
              '[ 3 ] Ranking de Vitorias\n'
              '[ 4 ] Regras\n'
              '[ 5 ] Encerrar o Programa')
        lista_opcoes = ['1', '2', '3', '4', '5']
        escolha_usuario = validar_escolha_usuario(lista_opcoes)

        if escolha_usuario == '1':
            criar_matrizes()

        if escolha_usuario == '5':
            encerrar = True


# Função Principal
def main():
    exibir_menu_principal()

    print(f'\n{cor["ma"]}{"=" * 43}')
    print(f'\n{cor["vd"]}{" PROGRAMA ENCERRADO ":*^43}\n')
    print(f'{cor["ma"]}{"=" * 43}')


main()
