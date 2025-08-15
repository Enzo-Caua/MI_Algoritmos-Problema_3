import os
import random
import time
import pickle


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
            escolha = input(f'{cor["ci"]}Escolha uma opção: ').upper()
            if escolha not in opcoes:
                raise IndexError

        except ValueError:
            print(f'{cor["vm"]}Atenção: Entrada invalida!')

        except IndexError:
            print(f'{cor["vm"]}Atenção: Opção invalida!')

    return escolha


# Sequencia de casas das linhas, colunas e diagonais
def sequencias_de_referencia(tamanho):
    if tamanho == 3:
        sequencias = {
            'L1' : ['A', 'B', 'C'], # Linha 1
            'L2' : ['D', 'E', 'F'], # Linha 2
            'L3' : ['G', 'H', 'I'], # Linha 3
            'C1' : ['A', 'D', 'G'], # Coluna 1
            'C2' : ['B', 'E', 'H'], # Coluna 2
            'C2' : ['C', 'F', 'I'], # Coluna 3
            'D'  : ['A', 'E', 'I']  # Diagonal
        }
        return sequencias

    elif tamanho == 4:
        sequencias = {
            'L1' : ['A', 'B', 'C', 'D'], # Linha 1
            'L2' : ['E', 'F', 'G', 'H'], # Linha 2
            'L3' : ['I', 'J', 'K', 'L'], # Linha 3
            'L4' : ['M', 'N', 'O', 'P'], # Linha 4
            'C1' : ['A', 'E', 'I', 'M'], # Coluna 1
            'C2' : ['B', 'F', 'J', 'N'], # Coluna 2
            'C3' : ['C', 'G', 'K', 'O'], # Coluna 3
            'C4' : ['D', 'H', 'L', 'P'], # Coluna 4
            'D'  : ['A', 'F', 'K', 'P']  # Diagonal
        }
        return sequencias

    elif tamanho == 5:
        sequencias = {
            'L1' : ['A', 'B', 'C', 'D', 'E'], # Linha 1
            'L2' : ['F', 'G', 'H', 'I', 'J'], # Linha 2
            'L3' : ['K', 'L', 'M', 'N', 'O'], # Linha 3
            'L4' : ['P', 'Q', 'R', 'S', 'T'], # Linha 4
            'L5' : ['U', 'V', 'W', 'X', 'Y'], # Linha 5
            'C1' : ['A', 'F', 'K', 'P', 'U'], # Coluna 1
            'C2' : ['B', 'G', 'L', 'Q', 'V'], # Coluna 2
            'C3' : ['C', 'H', 'M', 'R', 'W'], # Coluna 3
            'C4' : ['D', 'I', 'N', 'S', 'X'], # Coluna 4
            'C5' : ['E', 'J', 'O', 'T', 'Y'], # Coluna 5
            'D'  : ['A', 'G', 'M', 'S', 'Y']  # Diagonal
        }
        return sequencias


# Sequencia de casas das linhas, colunas e diagonais
def tabuleiros_de_referencia(tamanho):
    if tamanho == 3:
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C',
            'D': 'D', 'E': 'E', 'F': 'F',
            'G': 'G', 'H': 'H', 'I': 'I'
        }
        return tabuleiro

    elif tamanho == 4:
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
            'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
            'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L',
            'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P'
        }
        return tabuleiro

    elif tamanho == 5:
        tabuleiro = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
            'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
            'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
            'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
            'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y'
        }
        return tabuleiro


# Exibe as regras
def exibir_regras():
    print(f'\n{cor["ma"]}{" REGRAS ":=^50}')
    print(f'{cor["ci"]}')
    print(''
          '1 - Os tabuleiros tem N x N casas de acordo com a\n'
          '    dificuldade;\n'
          '2 - O numeros disponiveis para jogar vão de 1 ate \n'
          '    N² de acordo com a dificuldade;\n'
          '3 - Os jogadores jogam de forma alternada, sendo\n'
          '    o primeiro definido aleatoriamente;\n'
          '4 - Ganha o jogador que completar uma sequencia\n'
          '    dentre as disponiveis primeiro;\n'
          '5 - As sequencias são sorteadas ao inicio de cada\n'
          '    partida;\n'
          '6 - As sequencias disponiveis são:\n'
          '    * Ascendente: Numeros crescentes de 1 em 1\n'
          '    * Descentes: Numeros decrescentes de 1 em 1\n'
          '    * Pares: Numeros pares crescentes ou decres-\n'
          '      cente de 1 em 1\n'
          '    * Impares: Numeros impares crescentes ou de-\n'
          '      crescente de 1 em 1\n'
          '7 - O jogo termina em empate se todas as casas\n'
          '    forem preenchidas sem que nenhum objetivo\n'
          '    seja alcançado;\n'
          '8 - Cada jogador possui uma cor diferente no \n'
          '    tabuleiro;\n'
          '9 - Uma jogada especial pode ser ativada ao\n'
          '    inicio de cada partida, a jogada limpa \n'
          '    os numeros de uma linha, coluna ou dia-\n'
          '    gonal escolhida;\n'
          '10 - A jogada especial pode ser usada a \n'
          '     qualquer momento digitando "45" ao \n'
          '     informar a casa que deseja jogar;\n'
          '     * Curiosidade: 45 é o valor da letra "E"\n'
          '       em codigo Hexadecimal\n'
          '11 - O jogo pode atual pode ser salvo a \n'
          '     qualquer momento digitando "53" ao \n'
          '     informar a casa que deseja jogar\n'
          '     * Curiosidade: 53 é o valor da letra "S"\n'
          '       em codigo Hexadecimal\n'
          '     * Infelizmente esta funcionalidade ainda\n'
          '       não foi implementada.\n'
          '')


# Sorteia a sequencia objetivo do jogador
def sortear_objetivo():
    continuar = 'N'
    valido = False

    objetivos = {
        'Ascendente': 
        '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25', 

        'Descendente': 
        '25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1', 

        'Impar': 
        '1,3,5,7,9,11,13,15,17,19,21,23,25,25,23,21,19,17,15,13,11,9,7,5,3,1', 

        'Par' : 
        '2,4,6,8,10,12,14,16,18,20,22,24,24,22,20,18,16,14,12,10,8,6,4,2'
        }

    print(f"{cor['ma']}{' Jogador 1 ':=^50}{cor['ci']}")
    nome_j1 = input('Nome: ')

    print('SORTEANDO O OBJETIVO! Lembre-se apenas voce \ndeve ver o objetivo!')
    sequencia, objetivo_j1 = random.choice(list(objetivos.items()))

    for _ in range(3):
        print('...')
        time.sleep(0.5)
    print(f'\nSeu objetivo é: Sequencia {sequencia}')

    while continuar not in 'Ss':
        continuar = input('\nLembre-se deste objetivo! Continuar[S/N]?')
    limpar_terminal()


    print(f"{cor['ma']}{' Jogador 2 ':=^50}{cor['ci']}")
    while not valido:
        nome_j2 = input('Nome: ')
        if nome_j2 == nome_j1:
            print(f'{cor["vm"]}Nome igual ao do jogador anterior!{cor["ci"]}')
            print(f'Escolha outro nome!')
        else:
            valido = True

    print('SORTEANDO O OBJETIVO! Lembre-se apenas voce \ndeve ver o objetivo!')
    sequencia, objetivo_j2 = random.choice(list(objetivos.items()))

    for _ in range(3):
        print('...')
        time.sleep(0.5)
    print(f'\nSeu objetivo é: Sequencia {sequencia}')

    while continuar not in 'Ss':
        continuar = input('\nLembre-se deste objetivo! Continuar[S/N]?')

    dados_jogadores = {nome_j1 : objetivo_j1, nome_j2 : objetivo_j2}
    cores_jogadores = {nome_j1 : '\033[33m', nome_j2 : '\033[34m'}
    return dados_jogadores, cores_jogadores


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
    lista_opcoes = ['1', '2', '3', '4']
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
    elif escolha_usuario == '3':
        exibir_menu_principal()


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

    print(f'\n{cor["ma"]}{" TABULEIRO DE NUMEROS ":=^50}')

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


# Salva o estado do jogo
def salvar_jogo():
    print(f'\n{cor["pt"]}Infelizmente esta funcionalidade ainda não foi' 
          'implementada :( \nAguarde a proxima atualização!')


# Atualiza o ranking e salva no arquivo
def atualizar_ranking(ganhador):

    # Retorna somento o valor do dicionario
    def pegar_valor(itens):
        return itens[1]

    try:
        with open('ranking.pkl', 'rb') as arquivo_ranking:
            ranking = pickle.load(arquivo_ranking)
    except FileNotFoundError:
        with open('ranking.pkl', 'wb') as arquivo_ranking:
            pass  # Cria o arquivo se ele não existir

    if ganhador in ranking:
        ranking[ganhador] += 1
    else:
        ranking[ganhador] = 1

    # Organizar o dicionário por ordem de valores, do maior para o menor
    ranking_ordenado = dict(
                        sorted(ranking.items(), key=pegar_valor, reverse=True))

    with open('ranking.pkl', 'wb') as arquivo_ranking:
        pickle.dump(ranking_ordenado, arquivo_ranking) 


# Exibe o Ranking
def visualizar_ranking():
    i = 1

    try:
        with open('ranking.pkl', 'rb') as arquivo_ranking:
            ranking = pickle.load(arquivo_ranking)
        print(f'\n{cor["ma"]}{" RANKING ":=^50}')
        print(f'{cor["ci"]}')

        while i < 11:
            for nome in ranking.keys():
                if i == 10:
                    print(f'{i} - {nome}')
                else:
                    print(f'{i}  - {nome}')
                i += 1
    except FileNotFoundError:
        print(f'{cor["vm"]}Ranking Inexistente')


# Valida os objetivos
def validar_objetivo(tabuleiro_validacao, objetivos, tamanho):
    sequencias_validacao = sequencias_de_referencia(tamanho)
    sequencia_tabuleiro = []

    for sequencia in sequencias_validacao.values():
        valores_tabuleiro = []
        for casa in sequencia:
            valores_tabuleiro.append(tabuleiro_validacao[casa])
        sequencia_tabuleiro.append(','.join(valores_tabuleiro))

    for sequencia in sequencia_tabuleiro:
        if sequencia in objetivos[0]:
            return objetivos[0]
        elif sequencia in objetivos[1]:
            return objetivos[1]
    return False


# Gera as opçoes da jogada especial
def gerar_opcoes(tamanho):
    opcoes = []
    # Adicionar opções de linhas
    for i in range(1, tamanho + 1):
        opcoes.append(f'L{i}')
    # Adicionar opções de colunas
    for i in range(1, tamanho + 1):
        opcoes.append(f'C{i}')
    # Adicionar opção diagonal
    opcoes.append('D')

    return opcoes


# Exibe o Menu de jogada especial
def menu_jogada_especial(tamanho, tabuleiro_validacao, tabuleiro_visual):

    print(f'\n{cor["ma"]}{" JOGADA ESPECIAL ":=^50}')
    print(f'{cor["ci"]}'
            'Informe um dos codigos para executar a jogada:\n\n'
           f'[ L1 -> L{tamanho} ] Linhas de 1 a {tamanho}\n'
           f'[ C1 -> C{tamanho} ] Colunas de 1 a {tamanho}\n'
            '[ D ] Diagonal\n')
    lista_opcoes = gerar_opcoes(tamanho)
    escolha_usuario = validar_escolha_usuario(lista_opcoes)
    realizar_jogada_especial(escolha_usuario, tamanho, 
                             tabuleiro_validacao, tabuleiro_visual)


# Realiza a jogada especial
def realizar_jogada_especial(jogada_especial, tamanho, 
                             tabuleiro_validacao, tabuleiro_visual):

    sequencias = sequencias_de_referencia(tamanho)
    sequencia_jogada_especial = sequencias[jogada_especial]
    tabuleiro_referencia = tabuleiros_de_referencia(tamanho)

    for casa in sequencia_jogada_especial:
        tabuleiro_validacao[casa] = tabuleiro_referencia[casa]
        tabuleiro_visual[casa] = tabuleiro_referencia[casa]


# Realiza as jogadas
def realizar_jogadas(casas, numeros, tamanho, tabuleiro_visual, 
                     tabuleiro_validacao, cor_jg, jogador, jogada_especial):
    valido = False
    while not valido:
        try:
            casa = input(f'\n{cor["ci"]}Selecione uma casa: ').upper()
            if casa == '45':
                if jogada_especial == 'S':
                    menu_jogada_especial(tamanho, 
                                        tabuleiro_validacao, tabuleiro_visual)
                    imprimir_tabuleiro(tabuleiro_visual, tamanho)
                    print(f'Jogador Atual: {cor_jg}{jogador}\033[m')
                    continue
                elif jogada_especial == 'N':
                    print('Jogada Especial Não Disponivel!')
                    continue
            elif casa == '53':
                salvar_jogo()
            elif casa not in casas:
                raise IndexError

            num = input(f'{cor["ci"]}Selecione um numero: ')
            if num not in numeros:
                raise IndexError

            casas.remove(casa)
            numeros.remove(num)

            valido = True
        except IndexError:
            print(f'{cor["vm"]}Atenção: Entrada invalida!')

    # Compor a jogada com cor
    jogada = cor_jg + num + '\033[32m'

    # Calcular o espaçamento ignorando os caracteres de escape ANSI
    largura_total = 7
    largura_visivel = len(num)

    # Calcular os espaços à esquerda e à direita
    espacos_esquerda = (largura_total - largura_visivel) // 2
    espacos_direita = largura_total - largura_visivel - espacos_esquerda

    # Construir a string final com os espaços corretamente posicionados
    jogada_formatada = ' ' * espacos_esquerda + jogada + ' ' * espacos_direita

    tabuleiro_visual[casa] = jogada_formatada
    tabuleiro_validacao[casa] = num
    casas_disponiveis = len(casas)
    return casas_disponiveis


# Executa o jogo
def executar_jogo():

    valido = False
    jogo_valido = False
    ganhou = False

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

    tabuleiro, tamanho = selecionar_dificuldade()
    n = tamanho ** 2
    numeros = [str(num) for num in range(1, n + 1)]

    casas = letras[0:n]
    casas_disponiveis = len(casas)

    tabuleiro_visual = dict(tabuleiro)
    tabuleiro_validacao = dict(tabuleiro)

    # Aleatoriza a ordem de inicio
    jogadores, cores = sortear_objetivo()
    ordem = list(jogadores.keys())
    random.shuffle(ordem)

    while not valido:
        jogada_especial = input('Ativar jogada especial [S/N]?').upper()
        if jogada_especial not in 'SN':
            continue
        valido = True

    while not jogo_valido:
        objetivos = [jogadores[ordem[0]],jogadores[ordem[1]]]
        imprimir_tabuleiro(tabuleiro_visual, tamanho)
        for jogador in ordem:
            cor_jg = cores[jogador]
            print(f'Jogador Atual: {cor_jg}{jogador}\033[m')

            casas_disponiveis = realizar_jogadas(casas, numeros, tamanho,
                                tabuleiro_visual, tabuleiro_validacao, cor_jg, 
                                jogador, jogada_especial)

            imprimir_tabuleiro(tabuleiro_visual, tamanho)

            validar = validar_objetivo(tabuleiro_validacao, objetivos, tamanho)
            if validar is not False:
                for nome, objetivo in jogadores.items():
                    if objetivo == validar:
                        ganhou = True
                        print(f'O jogador {cores[nome]}{nome}\033[32m '
                              'ganhou!')
                        break
            if casas_disponiveis == 0:
                jogo_valido = True
                print(f'Nenhum jogador atingiu o objetivo!')
                print('EMPATE')
                break
            elif ganhou == True:
                jogo_valido = True
                break

    atualizar_ranking(nome)


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

        elif escolha_usuario == '2':
            print(f'{cor["pt"]}')
            print('Infelizmente essa função não foi implementada ainda :(')
            print('Aguarde as proximas atualizações')

        elif escolha_usuario == '3':
            visualizar_ranking()

        elif escolha_usuario == '4':
            exibir_regras()

        elif escolha_usuario == '5':
            encerrar = True


# Função Principal
def main():
    exibir_menu_principal()

    print(f'\n{cor["ma"]}{"=" * 43}')
    print(f'\n{cor["vd"]}{" PROGRAMA ENCERRADO ":*^43}\n')
    print(f'{cor["ma"]}{"=" * 43}')


main()