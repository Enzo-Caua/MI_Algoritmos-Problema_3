import os
import random

def sequencias_asc_3x3():
    ascendente = []
    for i in range(7):
        possiblidades_asc = []
        possiblidades_asc.append(i+1)
        possiblidades_asc.append(i+2)
        possiblidades_asc.append(i+3)
        ascendente.append(possiblidades_asc)
    return ascendente


def linhas_3x3(jogadas):
    linha1 = []
    linha2 = []
    linha3 = []
    for i in range(3):
        if i==0:
            linha1.append(jogadas[(i,i)])
            linha2.append(jogadas[(1,i)])
            linha3.append(jogadas[(2,i)])
        else:   
            linha1.append(jogadas[(0,i)])
            linha2.append(jogadas[(1,i)])
            linha3.append(jogadas[(2,i)])                    
    linhas = {}
    linhas['linha1'] = linha1
    linhas['linha2'] = linha2
    linhas['linha3'] = linha3
    return linhas


def criar_matriz(nivel, nivel_raiz):
    jogador1 = input('\nDigite o nome de usuário do primeiro jogador: ')
    jogador2 = input('\nDigite o nome de usuário do segundo jogador: ')
    jogador_inicio = random.randint(1,2)
    objetivos = {1:'ascendentes', 2:'descendentes', 3:'ímpares', 4:'pares'}
    if jogador_inicio == 1:
        print(f'\nO jogador {jogador1} iniciará a partida.')
        visualizar = input(f'\n{jogador1} pressione a tecla ENTER para visualizar o seu objetivo.')
        if visualizar == '':
            objetivo1 = random.randint(1,4)
            print(f'\nO seu objetivo é formar uma sequencia de números {objetivos[objetivo1]}.')
            esconder = input(f'\n{jogador1} pressione a tecla ENTER para esconder o seu objetivo e passe para {jogador2}.')
            os.system('cls')
            visualizar = input(f'\n{jogador2} pressione a tecla ENTER para visualizar o seu objetivo.')
            objetivo2 = random.randint(1,4)
            print(f'\nO seu objetivo é formar uma sequencia de números {objetivos[objetivo2]}.')
            iniciar = input(f'\n{jogador2} pressione a tecla ENTER para esconder o seu objetivo e passe para {jogador1} iniciar a partida.'),
            os.system('clear')
    else:
        print(f'\nO jogador {jogador2} iniciará a partida.')
        visualizar = input(f'\n{jogador2} pressione a tecla ENTER para visualizar o seu objetivo.')
        if visualizar == '':
            objetivo1 = random.randint(1,4)
            print(f'\nO seu objetivo é formar uma sequencia de números {objetivos[objetivo1]}.')
            esconder = input(f'\n{jogador2} pressione a tecla ENTER para esconder o seu objetivo e passe para {jogador1}.')
            os.system('cls')
            visualizar = input(f'\n{jogador1} pressione a tecla ENTER para visualizar o seu objetivo.')
            objetivo2 = random.randint(1,4)
            print(f'\nO seu objetivo é formar uma sequencia de números {objetivos[objetivo2]}.')
            iniciar = input(f'\n{jogador1} pressione a tecla ENTER para esconder o seu objetivo e passe para {jogador2} iniciar a partida.')
            os.system('cls')
    jogadas = {}
    for i in range(nivel_raiz):
        for j in range(nivel_raiz):
            jogadas[(i,j)]=''
    for i in range(nivel):
        if i ==0:
            num_jogada = int(input('\nDigite o número que você deseja inserir no tabuleiro: '))
            linha = int(input('\nDigite o número correspondente à linha em que você deseja inserir o número escolhido: '))
            coluna = int(input('\nDigite o número correspondente à coluna em que você deseja inserir o número escolhido: '))
            jogada = jogadas.get((linha-1,coluna-1), False)
        else:
            print(f"\n\033[32m{'TABULEIRO DE NÚMEROS':^5}\033[m")
            for i in range(nivel_raiz):
                for j in range(nivel_raiz):
                    print(f'{jogadas[(i,j)]:^5}|', end = '')
                print()
            num_jogada = int(input('\nDigite o número que você deseja inserir no tabuleiro: '))
            linha = int(input('\nDigite o número correspondente à linha em que você deseja inserir o número escolhido: '))
            coluna = int(input('\nDigite o número correspondente à coluna em que você deseja inserir o número escolhido: '))
            jogada = jogadas.get((linha-1,coluna-1), False)               
        while jogada:
            print(f'\n\033[31mA posição ({linha},{coluna}) já está ocupada, escolha outra.\033[m')
            linha = int(input('\nDigite o número correspondente à linha em que você deseja inserir o número escolhido: '))
            coluna = int(input('\nDigite o número correspondente à coluna em que você deseja inserir o número escolhido: '))
            jogada = jogadas.get((linha-1,coluna-1), False)
        if not jogada:
            jogadas[(linha-1,coluna-1)] = num_jogada
            print(f'\n\033[36mO número {num_jogada} foi inserido na posição ({linha},{coluna}).\nPasse a vez para o outro jogador.\033[m\n')
        ascendente = sequencias_asc_3x3()
        linhas = linhas_3x3(jogadas)
        if linhas['linha1'] in ascendente or linhas['linha2'] in ascendente or linhas['linha3'] in ascendente :
            print('\nVocê ganhou!!!')
            break