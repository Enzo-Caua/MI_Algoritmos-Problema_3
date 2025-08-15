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


# Sorteia a sequencia objetivo do jogador
def sortear_objetivo(jogador):
    continuar = 'N'
    
    objetivos = {
        'Ascendente': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
                       23,24,25], 
        'Descendente': [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,
                        5,4,3,2,1], 
        'Impar': [25,23,21,19,17,15,13,11,9,7,5,3,1,1,3,5,7,9,11,13,15,17,19,
                    21,23,25], 
        'Par' : [24,22,20,18,16,14,12,10,8,6,4,2,2,4,6,8,10,12,14,16,18,20,22,
                   24]
        }

    print(f"{cor['ma']}{jogador:=^50}{cor['ci']}")
    nome = input('Nome: ')

    print('SORTEANDO O OBJETIVO! Lembre-se apenas voce \ndeve ver o objetivo!')
    sequencia, objetivo_sorteado = random.choice(list(objetivos.items()))

    # for _ in range(3):
    #     print('...')
    #     time.sleep(0.5)
    print(f'\nSeu objetivo é: Sequencia {sequencia}')
    
    while continuar not in 'Ss':
        continuar = input('\nLembre-se deste objetivo! Continuar[S/N]?')

    return nome, objetivo_sorteado


# Exibe o Menu de Dificuldade
def selecionar_dificuldade():
    tabuleiro = {}

    print(f'\n{cor["ma"]}{" DIFICULDADE ":=^50}')
    print(f'{cor["ci"]}'
            'Escolha a DIFICULDADE que deseja jogar:\n\n'
            '[ 1 ] Facil [3 x 3]\n'
            '[ 2 ] Normal [4 x 4]\n'
            '[ 3 ] Dificil [5 x 5]\n'
            '[ 4 ] Retornar ao Menu')
    lista_opcoes = ['1', '2', '3', '4', '5']
    escolha_usuario = validar_escolha_usuario(lista_opcoes)
    
    if escolha_usuario == '1':
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C',
            'D': 'D', 'E': 'E', 'F': 'F',
            'G': 'G', 'H': 'H', 'I': 'I'
        }
        return tabuleiro, 3

    elif escolha_usuario == '2':
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
            'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
            'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
            'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P'
        }
        return tabuleiro, 4

    elif escolha_usuario == '3':
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
            'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
            'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
            'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
            'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y'
        }
        return tabuleiro, 5


# Exibe o tabuleiro
def imprimir_tabuleiro(tabuleiro, tamanho):
    # Função para criar linhas horizontais da tabela
    def linha_horizontal(char):
        return f"|{char*7}" * tamanho + '|'

    # Função para criar uma linha com conteúdo
    def linha_conteudo(indices):
        lc = '|'+'|'.join(f"{tabuleiro[indice]:^7}" for indice in indices) + '|'
        return lc
    
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    print(f'{cor["vd"]}')

    # Imprimir linha superior da tabela
    print(linha_horizontal('‾'))

    # Imprimir linhas da tabela
    for i in range(tamanho):
        # Gerar os índices para a linha atual
        indices = [letras[i * tamanho + j] for j in range(tamanho)]
        print(linha_conteudo(indices))
        if i < tamanho - 1:
            print(linha_horizontal('_'))
            print(linha_horizontal(' '))

    # Imprimir linha inferior da tabela
    print(linha_horizontal('_'))


# Exibe o Menu Principal
def exibir_menu_principal():
    encerrar = False

    while not encerrar:
        print(f'\n{cor["ma"]}{" MENU PRINCIPAL ":=^50}')
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
            executar_jogo()

        elif escolha_usuario == '5':
            encerrar = True


# Função Principal
def main():

    exibir_menu_principal()

    print(f'\n{cor["ma"]}{"=" * 43}')
    print(f'\n{cor["vd"]}{" PROGRAMA ENCERRADO ":*^43}\n')
    print(f'{cor["ma"]}{"=" * 43}')


# Executa o jogo
def executar_jogo():

    tabuleiro, tamanho = selecionar_dificuldade()

    tabuleiro_visual = dict(tabuleiro)
    tabuleiro_validacao = dict(tabuleiro)

    limpar_terminal()
    nome_j1, objetivo_j1 = sortear_objetivo(' Jogador 1 ')

    limpar_terminal()
    nome_j2, objetivo_j2 = sortear_objetivo(' Jogador 2 ')

    # Aleatoriza a ordem de inicio
    jogadores = [nome_j1, nome_j2]
    random.shuffle(jogadores)

    executar_rodadas(tabuleiro_visual, tabuleiro_validacao, tamanho)


# Executa as Rodadas
def executar_rodadas(tabuleiro_visual, tabuleiro_validacao, tamanho):

    # Realiza as jogadas
    def realizar_jogadas(casas, numeros):
        valido = False
        while not valido:
            try:
                casa = input(f'\n{cor["ci"]}Selecione uma casa: ').upper()
                if casa not in casas:
                    raise IndexError
                
                num = int(input(f'{cor["ci"]}Selecione um numero: '))
                if num not in numeros:
                    raise IndexError
                
                casas.remove(casa)
                numeros.remove(num)

                valido = True
            except:
                print(f'{cor["vm"]}Atenção: Entrada invalida!')
        tabuleiro_visual[casa] = num
        tabuleiro_validacao[casa] = num
        casas_disponiveis = len(casas)
        return casas_disponiveis

    ganhador = None
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    
    n = tamanho ** 2
    numeros = list(range(1,n+1))
    casas = letras[0:n]
    casas_disponiveis = len(casas)

    while casas_disponiveis > 0 and ganhador == None:
        imprimir_tabuleiro(tabuleiro_visual, tamanho)
        casas_disponiveis = realizar_jogadas(casas, numeros)
        ganhador = validar_objetivo()
    
def validar_objetivo(tabuleiro_validacao, objetivo):
    pass






tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C',
            'D': 'D', 'E': 'E', 'F': 'F',
            'G': 'G', 'H': 'H', 'I': 'I'
        }


tabuleiro_visual = dict(tabuleiro)
tabuleiro_validacao = dict(tabuleiro)
tamanho = 3

executar_rodadas(tabuleiro_visual, tabuleiro_validacao, tamanho)
