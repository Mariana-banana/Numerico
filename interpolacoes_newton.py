def divididas(x, y):
    n = len(x)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def newton_interp(x_data, y_data, x):
    coef = divididas(x_data, y_data)
    n = len(coef)
    resultado = coef[-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - x_data[i]) + coef[i]
    return resultado

# Dados (ignoramos x=1, e queremos descobrir f(1))
# x_dados = [-2, -1, 0, 2, 3]
# y_dados = [-7, 0, 1, 9, 28]

# Avaliar f(1)
# x_alvo = 1

# x_dados = [5, 7.5, 10, 12.5, 15]
# y_dados = [26, 11.56, 6.50, 4.16, 2.88]
# x_alvo = 8.5

x_dados = [30, 35, 40]
y_dados = [0.99826, 0.99818, 0.99828]
x_alvo = 37.5
f1 = newton_interp(x_dados, y_dados, x_alvo)

print(f"O valor de f(1) = α estimado por interpolação é: {f1:.6f}")
