import json


def save_json():
    # Exemplo de dicionário
    dicionario = {
        "chave1": "valor1",
        "chave2": "valor2",
        "chave3": "valor3"
    }

    # Exemplo de matriz de listas
    matriz_de_listas = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Salvando o dicionário e a matriz de listas em um arquivo JSON
    dados = {
        "dicionario": dicionario,
        "matriz_de_listas": matriz_de_listas
    }

    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def ler_json():
    import json

    # Carregando os dados do arquivo JSON
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)

    # Obtendo o dicionário e a matriz de listas
    dicionario_carregado = dados["dicionario"]
    matriz_de_listas_carregada = dados["matriz_de_listas"]

    # Exibindo o dicionário e a matriz de listas
    print("Dicionário:")
    for chave, valor in dicionario_carregado.items():
        print(f"{chave}: {valor}")

    print("\nMatriz de Listas:")
    for linha in matriz_de_listas_carregada:
        print(linha)
