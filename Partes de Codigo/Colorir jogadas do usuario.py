# Definindo códigos de cor ANSI
ANSI_RESET = "\033[0m"
ANSI_COLORS = {
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
}

# Função para colorir texto
def colorir_texto(texto, cor):
    return f"{ANSI_COLORS.get(cor, ANSI_RESET)}{texto}{ANSI_RESET}"

# Associando variáveis a cores
variaveis_cores = {
    "var1": "vermelho",
    "var2": "verde",
    "var3": "azul"
}

# Função para imprimir variáveis coloridas
def imprimir_colorido(variavel, valor):
    cor = variaveis_cores.get(variavel, "branco")
    print(colorir_texto(valor, cor))

# Testando
var1 = "Olá, sou a variável 1"
var2 = "Olá, sou a variável 2"
var3 = "Olá, sou a variável 3"

imprimir_colorido("var1", var1)
imprimir_colorido("var2", var2)
imprimir_colorido("var3", var3)
