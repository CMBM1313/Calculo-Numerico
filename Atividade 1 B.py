def converter(n, base):
    if base == 10:
        return n

    result = expoente = 0
    while n > 0:
        n, digito = divmod(n, base)
        result += (10 ** expoente) * digito
        expoente += 1

    return result

x = int(input("Número Inteiro "))
y = float(input("Número do Erro "))
print(converter(x, 2))
print(converter(y, 2))