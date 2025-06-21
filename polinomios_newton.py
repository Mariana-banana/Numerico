def divididas(x, y):
    """
    Calcula a tabela de diferenças divididas de Newton.
    Retorna os coeficientes do polinômio interpolador.
    """
    n = len(x)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def newton_interp(x_data, y_data, x):
    """
    Avalia o polinômio de Newton no ponto x usando os dados fornecidos.
    """
    coef = divididas(x_data, y_data)
    n = len(coef)
    resultado = coef[-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - x_data[i]) + coef[i]
    return resultado

# Dados
# d_cm = [30, 35, 40]
# E = [0.99826, 0.99818, 0.99828]

d_cm = [250, 330, 412, 485, 617]
E = [5720, 5260, 4450, 2780, 1506]

# Ponto a interpolar
d_alvo = 37.5

# Calcular valor interpolado
E_interpolado = newton_interp(d_cm, E, d_alvo)

print(f"Valor estimado de E para {d_alvo} cm: {E_interpolado:.8f} N/C")
