import numpy as np

# Definindo a função f(x) = sqrt(3x + 5)
def f(x):
    return 1/(2*x)

# Intervalo e passo
a = 1
b = 3
h = 0.0001

# Criar os pontos x
x = np.arange(a, b + h, h)
y = f(x)

# Aplicando a fórmula dos trapézios
def metodo_trapezios(y, h):
    n = len(y) - 1
    return h * (y[0] + 2 * np.sum(y[1:n]) + y[n]) / 2

# Cálculo


integral = metodo_trapezios(y, h)

print(f"Integral aproximada com h = {h} de f(x) no intervalo {a, b}: {integral}")
