import random
import numpy as np

def criar_tabuleiro():
    return np.zeros((3, 3), dtype=int)

def sortear_objetivo():
    tipos = ['ascendente', 'descendente', 'ímpares', 'pares']
    return random.choice(tipos)

def checar_vitoria(tabuleiro, objetivo):
    linhas, colunas = tabuleiro.shape

    def sequencia_ascendente(l):
        return all(l[i] < l[i+1] for i in range(len(l) - 1))

    def sequencia_descendente(l):
        return all(l[i] > l[i+1] for i in range(len(l) - 1))

    def sequencia_impares(l):
        return all(x % 2 != 0 for x in l)

    def sequencia_pares(l):
        return all(x % 2 == 0 for x in l)

    verificadores = {
        'ascendente': sequencia_ascendente,
        'descendente': sequencia_descendente,
        'ímpares': sequencia_impares,
        'pares': sequencia_pares
    }

    for i in range(linhas):
        if verificadores[objetivo](tabuleiro[i, :]):
            return True
        if verificadores[objetivo](tabuleiro[:, i]):
            return True

    if verificadores[objetivo]([tabuleiro[i, i] for i in range(linhas)]):
        return True

    if verificadores[objetivo]([tabuleiro[i, linhas - 1 - i] for i in range(linhas)]):
        return True

    return False

def jogada(tabuleiro, linha, coluna, valor):
    if tabuleiro[linha, coluna] == 0:
        tabuleiro[linha, coluna] = valor
        return True
    return False

def mostrar_tabuleiro(tabuleiro):
    print(tabuleiro)

# Exemplo de uso
tabuleiro = criar_tabuleiro()
objetivo_jogador1 = sortear_objetivo()
objetivo_jogador2 = sortear_objetivo()
print(f"Objetivo do Jogador 1: {objetivo_jogador1}")
print(f"Objetivo do Jogador 2: {objetivo_jogador2}")

mostrar_tabuleiro(tabuleiro)

# Jogadas exemplo
jogada(tabuleiro, 0, 0, 1)
jogada(tabuleiro, 0, 1, 3)
jogada(tabuleiro, 0, 2, 5)

mostrar_tabuleiro(tabuleiro)

# Verificação de vitória
if checar_vitoria(tabuleiro, objetivo_jogador1):
    print("Jogador 1 venceu!")
if checar_vitoria(tabuleiro, objetivo_jogador2):
    print("Jogador 2 venceu!")
