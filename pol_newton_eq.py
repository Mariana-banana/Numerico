import numpy as np

def divididas(x, y):
    """
    Calcula a tabela de diferenças divididas de Newton.
    Retorna os coeficientes do polinômio interpolador.
    """
    n = len(x)
    coef = np.array(y, dtype=float)
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
    for i in range(n - 2, -1, -1):
        resultado = resultado * (x - x_data[i]) + coef[i]
    return resultado

def pontos_mais_proximos(x_dados, y_dados, x_alvo, grau):
    """
    Seleciona os (grau + 1) pontos mais próximos de x_alvo.
    """
    dados_ordenados = sorted(zip(x_dados, y_dados), key=lambda p: abs(p[0] - x_alvo))
    mais_proximos = sorted(dados_ordenados[:grau + 1])
    x_selecionados = [p[0] for p in mais_proximos]
    y_selecionados = [p[1] for p in mais_proximos]
    return x_selecionados, y_selecionados

# --- Dados do problema ---
alongamentos = [10, 15, 20, 25, 30, 35]
cargas = [105, 172, 253, 352, 473, 619]

# Grau do polinômio de Newton
grau = 3

# Pontos alvo a interpolar
x_alvos = [12, 22, 31]

# Cálculo e impressão
for x_alvo in x_alvos:
    x_interp, y_interp = pontos_mais_proximos(alongamentos, cargas, x_alvo, grau)
    carga_estimada = newton_interp(x_interp, y_interp, x_alvo)
    print(f"Carga estimada para alongamento de {x_alvo} mm: {carga_estimada:.6f} kgf")
