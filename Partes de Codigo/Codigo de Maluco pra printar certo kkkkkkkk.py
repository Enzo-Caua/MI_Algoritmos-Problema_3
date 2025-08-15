# Dicionário de cores
cores = {'nome_j1': '\033[33m', 'nome_j2': '\033[34m'}

# Selecionar a cor para o jogador
cor_jg = cores['nome_j1']

# Definir o número a ser exibido
num = '1'

# Compor a jogada com cor
jogada = cor_jg + num + '\033[32m'

# Calcular o espaçamento ignorando os caracteres de escape ANSI
largura_total = 10
largura_visivel = len(num)


# Calcular os espaços à esquerda e à direita
espacos_esquerda = (largura_total - largura_visivel) // 2
espacos_direita = largura_total - largura_visivel - espacos_esquerda

# Construir a string final com os espaços corretamente posicionados
jogada_formatada = ' ' * espacos_esquerda + jogada + ' ' * espacos_direita

# Imprimir a jogada formatada
print(jogada_formatada)
