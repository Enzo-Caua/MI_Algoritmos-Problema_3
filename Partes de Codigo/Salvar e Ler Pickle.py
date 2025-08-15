import pickle

matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

# Armazenar a matriz em um arquivo Pickle
with open('matriz.pkl', 'wb') as f:
    pickle.dump(matriz, f)

# Ler a matriz do arquivo Pickle
with open('matriz.pkl', 'rb') as f:
    matriz_lida = pickle.load(f)

# Verificar se a matriz lida é igual à original
print(matriz_lida == matriz)  # Deve imprimir True
