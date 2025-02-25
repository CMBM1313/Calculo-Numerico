import numpy as np

# Definindo a matriz A

A = np.array([[2, 3, -4, 9], [-4, -27, 11, -6], [36, 11, -20, 10], [-2, -7, 22, -6]], dtype=float)

# Tomando L como a identidade e U como uma cópia de A

n = A.shape[0]
L = np.eye(n)
U = A.copy()

# Realizando a decomposição LU
for i in range(n):
    for j in range(i+1, n):

        # Calculando o fator multiplicador

        fator = U[j, i] / U[i, i]

        # Atualizador da linha j da matriz U

        U[j, i:] -= fator * U[i, i:]

        # Colocando o fator multiplicador na matriz L

        L[j, i] = fator

# Print das matrizes L e U

print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)
