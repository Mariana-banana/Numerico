import numpy as np

# Tabela de dados
t = np.array([0.00, 0.10, 0.20, 0.30, 0.40])  
v = np.array([4.2, 7.5, 9.0, 10.5, 7.0])      

# Método dos Trapézios
def metodo_trapezios(x, y):
    soma = 0
    for i in range(1, len(x)):
        h = x[i] - x[i-1]
        soma += h * (y[i] + y[i-1]) / 2
    return soma


res = metodo_trapezios(t, v)

print(f"{res}")
