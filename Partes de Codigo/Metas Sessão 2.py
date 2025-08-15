import os
import random
import time

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

# Limpa o terminal de acordo com o SO do usuario
def limpar_terminal():
        # Verifica o sistema operacional
        if os.name == 'nt':
            # Se for Windows
            os.system('cls')
        else:
            # Se for Unix/Linux/MacOS
            os.system('clear')


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


# Sorteia a sequencia objetivo do jogador
def sortear_objetivo(jogador):
    objetivos = {
        'Ascendente': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
                        20,21,22,23,24,25], 
        'Descendente': [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,
                        5,4,3,2,1], 
        'Impares': [25,23,21,19,17,15,13,11,9,7,5,3,1,1,3,5,7,9,11,13,15,17,19,
                    21,23,25], 
        'Pares' : [24,22,20,18,16,14,12,10,8,6,4,2,2,4,6,8,10,12,14,16,18,20,22,
                   24]
        }

    print(f"{cor['ma']}{jogador:=^40}{cor['ci']}")
    nome = input('Nome: ')

    print('SORTEANDO O OBJETIVO! Lembre-se apenas voce deve ver o objetivo!')
    sequencia, objetivo_sorteado = random.choice(list(objetivos.items()))

    for _i in range(3):
        print('...')
        time.sleep(0.5)
    print(f'Seu objetivo é: \nSequencia {sequencia}: {objetivo_sorteado}')

    return nome, objetivo_sorteado


# Cria o tabuleiro de acordo com a dificuldade
def criar_matrizes():
    contador = 65
    matriz = {}

    print(f'\n{cor["ma"]}{" DIFICULDADE ":=^43}')
    print(f'{cor["ci"]}'
            'Escolha a opção que deseja executar:\n\n'
            '[ 1 ] Facil (3 x 3)\n'
            '[ 2 ] Medio (4 x 4)\n'
            '[ 3 ] Dificil (5 x 5)\n'
            '[ 4 ] Retornar ao Menu Principal')
    lista_opcoes = ['1', '2', '3', '4']
    escolha_usuario = validar_escolha_usuario(lista_opcoes)

    if escolha_usuario == '1':
        for l in range(3):
            for c in range(3):
                matriz[(l, c)] = chr(contador)
                contador += 1
        return matriz, 3

    elif escolha_usuario == '2':
        for l in range(4):
            for c in range(4):
                matriz[(l, c)] = chr(contador)
                contador += 1
        return matriz, 4

    if escolha_usuario == '3':
        for l in range(5):
            for c in range(5):
                matriz[(l, c)] = chr(contador)
                contador += 1
        return matriz, 5

    elif escolha_usuario == '4':
        return {}, 0


# Executa o jogo
def executar_jogo(tabuleiro, tamanho):
    while True:
        chave_encontrada = None

        print(f"\n{cor['ma']}{' TABULEIRO DE NUMEROS ':=^56}{cor['ci']}\n")

        for l in range(tamanho):
            for c in range(tamanho):
                print('|', end='')
                print(f'{tabuleiro[(l, c)]:^10}', end='')
            print('|')

        letra = input('\nInforme a casa que deseja jogar: ').upper()
        numero = int(input('Informe o numero:  '))

        # Procura a chave correspondente à letra
        for chave, valor in tabuleiro.items():
            if valor == letra:
                chave_encontrada = chave
                break

        tabuleiro[chave_encontrada] = numero


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
            prox = 'N'
            iniciar = 'N'

            tabuleiro, tamanho = criar_matrizes()

            limpar_terminal()

            nome_j1, objetivo_j1 = sortear_objetivo(' Jogador 1 ')
            while prox not in 'Ss':
                prox = input(
                'Lembre deste objetivo! Passar para o proximo jogador[S/N]?')

            limpar_terminal()

            nome_j2, objetivo_j2 = sortear_objetivo(' Jogador 2 ')
            while iniciar not in 'Ss':
                iniciar = input('Lembre deste objetivo! Iniciar Jogo[S/N]?')

            limpar_terminal()

            executar_jogo(tabuleiro, tamanho)


        elif escolha_usuario == '5':
            encerrar = True


# Função Principal
def main():
    exibir_menu_principal()

    print(f'\n{cor["ma"]}{"=" * 43}')
    print(f'\n{cor["vd"]}{" PROGRAMA ENCERRADO ":*^43}\n')
    print(f'{cor["ma"]}{"=" * 43}')


main()