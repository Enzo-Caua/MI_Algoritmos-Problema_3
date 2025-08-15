objetivo = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25'

sequencias_validacao = [
    ['A', 'B', 'C'],  # Linha 1
    ['D', 'E', 'F'],  # Linha 2
    ['G', 'H', 'I'],  # Linha 3
    ['A', 'D', 'G'],  # Coluna 1
    ['B', 'E', 'H'],  # Coluna 2
    ['C', 'F', 'I'],  # Coluna 3
    ['A', 'E', 'I']   # Diagonal
]

tabuleiro = {
    'A': '1', 'B': '2', 'C': '3',
    'D': '4', 'E': '5', 'F': '6',
    'G': '7', 'H': '8', 'I': '9'
}

sequencia_tabuleiro = []

for sequencia in sequencias_validacao:
    valores_tabuleiro = []
    for casa in sequencia:
        valores_tabuleiro.append(tabuleiro[casa])
    sequencia_tabuleiro.append(','.join(valores_tabuleiro))

for sequencia in sequencia_tabuleiro:
    if sequencia in objetivo:
        print("Ganhou", sequencia)
        break
    else:
        print('Perdeu', sequencia)
