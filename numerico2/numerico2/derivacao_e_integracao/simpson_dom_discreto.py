def simpson_pontos(X, Y):
    n = len(X)
    h = (X[-1] - X[0]) / (n - 1)
    soma = 0.0

    for i in range(n):
        if i == 0 or i == n-1:
            soma_parc = Y[i]
        elif i % 2 == 1:
            soma_parc = 4 * Y[i]
        else:
            soma_parc = 2 * Y[i]

        soma += soma_parc

    return soma * h / 3

# Exemplo de uso
if __name__ == "__main__":
    X = [0, 1, 2, 3, 4]       # precisa ter número ímpar de pontos (par de subintervalos)
    Y = [0.7, 2.6, 3.9, 2.1, 0.2]
    resultado = simpson_pontos(X, Y)
    print(f"Integral aproximada = {resultado:.6f}")
