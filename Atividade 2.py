def Aplica(f): # Subprograma que vai aplicar um dos valores do intervalo no "Meu polinômio" e asim retornar seu valor para ser analisado.
    return f**3 - 10*f**2 + 7*f + 7 # "Meu polinômio".

def Bisseccao(x, y, Delta = 1e-5, Max = 500, Contador = 0): # "Delta" é o valor máximo para f(a) e f(b) continuar rodando e "Max" é o número de iterações até o programa dar Break.
    M = (x + y) / 2 # Média entre os intervalos.
    X = Aplica(x) # Valor da f(a).
    Y = Aplica(y) # Valor da f(b).
    FM = Aplica(M) # Valor da f(média de a e b).
    N = (y - x)
    print(f"Valor de f(a) e f(b) = {X}, {Y}")

    # Critério de parada.
    if abs(N) <= Delta or Contador >= Max: # O contador faz como diz seu nome e conta, ao chegar em quinhentos ou mais, ele quebra o loop.
        return M

    # Atualizador de intervalo.
    elif X * FM < 0:
        return Bisseccao(x, M, Delta, Max, Contador + 1)
    else:
        return Bisseccao(M, y, Delta, Max, Contador + 1)

# O intervalos ou seja (a,b).
x1, y1 = -5, 0    # Intervalo para a primeira raiz.
x2, y2 = 0, 5     # Intervalo para a segunda raiz.
x3, y3 = 5, 10    # Intervalo para a terceira raiz.

# Invocar a função da bissecção para cada intervalo.
Raiz1 = Bisseccao(x1, y1)
print("Fim da operação para encontrar a raiz 1 e começo da operação para a raiz 2")

Raiz2 = Bisseccao(x2, y2)
print("Fim da operação para encontrar a raiz 2 e começo da operação para a raiz 3")

Raiz3 = Bisseccao(x3, y3)
print("Fim da operação para encontrar a raiz 3")

# Print dos resultados.
print(f"As raízes aproximadas são: {Raiz1}, {Raiz2}, {Raiz3}")