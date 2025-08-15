objetivos = {
    'Ascendente': 
    '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25', 
    'Descendente': 
    '25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1', 
    'Impar': 
    '25,23,21,19,17,15,13,11,9,7,5,3,1,1,3,5,7,9,11,13,15,17,19,21,23,25', 
    'Par' : 
    '24,22,20,18,16,14,12,10,8,6,4,2,2,4,6,8,10,12,14,16,18,20,22,24'
    }

def tabuleiro_referencia(tamanho):
    tabuleiro = {}
    
    if tamanho == 3:
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C',
            'D': 'D', 'E': 'E', 'F': 'F',
            'G': 'G', 'H': 'H', 'I': 'I'
        }

    elif tamanho == 4:
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
            'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
            'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
            'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P'
        }

    elif tamanho == 5:
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
            'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
            'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
            'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
            'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y'
        }

    return tabuleiro


def sequencias_referencia(tamanho):
    sequencias = []

    if tamanho == 3:
        sequencias = [
            ['A', 'B', 'C'], # Linha 1
            ['D', 'E', 'F'], # Linha 2
            ['G', 'H', 'I'], # Linha 3
            ['A', 'D', 'G'], # Coluna 1
            ['B', 'E', 'H'], # Coluna 2
            ['C', 'F', 'I'], # Coluna 3
            ['A', 'E', 'I']  # Diagonal
        ]
        return sequencias

    elif tamanho == 4:
        sequencias = [
            ['A', 'B', 'C', 'D'], # Linha 1
            ['E', 'F', 'G', 'H'], # Linha 2
            ['I', 'J', 'K', 'L'], # Linha 3
            ['M', 'N', 'O', 'P'], # Linha 4
            ['A', 'E', 'I', 'M'], # Coluna 1
            ['B', 'F', 'J', 'N'], # Coluna 2
            ['C', 'G', 'K', 'O'], # Coluna 3
            ['D', 'H', 'L', 'P'], # Coluna 4
            ['A', 'F', 'K', 'P']  # Diagonal
        ]
        return sequencias

    elif tamanho == 5:
        sequencias = [
            ['A', 'B', 'C', 'D', 'E'], # Linha 1
            ['F', 'G', 'H', 'I', 'J'], # Linha 2
            ['K', 'L', 'M', 'N', 'O'], # Linha 3
            ['P', 'Q', 'R', 'S', 'T'], # Linha 4
            ['U', 'V', 'W', 'X', 'Y'], # Linha 5
            ['A', 'F', 'K', 'P', 'U'], # Coluna 1
            ['B', 'G', 'L', 'Q', 'V'], # Coluna 2
            ['C', 'H', 'M', 'R', 'W'], # Coluna 3
            ['D', 'I', 'N', 'S', 'X'], # Coluna 4
            ['E', 'J', 'O', 'T', 'Y'], # Coluna 5
            ['A', 'G', 'M', 'S', 'Y']  # Diagonal
        ]
        return sequencias