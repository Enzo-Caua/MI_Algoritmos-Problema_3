import random
import time
import os

def limpar_terminal():
        # Verifica o sistema operacional
        if os.name == 'nt':
            # Se for Windows
            os.system('cls')
        else:
            # Se for Unix/Linux/MacOS
            os.system('clear')

def sortear_objetivos(jogador):
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

    print(f'{jogador:=^40}')
    nome = input(f'Nome: ')

    print('SORTEANDO O OBJETIVO! Lembre-se apenas voce deve ver o objetivo!')
    sequencia, objetivo_sorteado = random.choice(list(objetivos.items()))

    for i in range(3):
        print('...')
        time.sleep(0.5)
    print(f'Seu objetivo é: \nSequencia {sequencia}: {objetivo_sorteado}')

    return nome, objetivo_sorteado


def inicar():
    prox = 'N'
    iniciar = 'N'
    sortear_objetivos('Jogador 1')
    while not prox in 'Ss':
        prox = input('Lembre deste objetivo! Passar para o proximo jogador[S/N]?')
    limpar_terminal()

    sortear_objetivos('Jogador 2')
    while not iniciar in 'Ss':
        iniciar = input('Lembre deste objetivo! Iniciar Jogo[S/N]?')
    limpar_terminal()

sortear_objetivos('Jogador 1')