import numpy as np # É uma boa prática importar numpy se for usar arrays no futuro

def divididas(x, y):
    """
    Calcula a tabela de diferenças divididas de Newton.
    Retorna os coeficientes do polinômio interpolador.
    """
    n = len(x)
    # Usar np.array garante que a cópia e as operações sejam numéricas
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
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - x_data[i]) + coef[i]
    return resultado

# --- Dados do Problema do Calor Específico (Questão 4) ---
# Nomes das variáveis ajustados para maior clareza
T_celsius = [30, 35, 40]
c_especifico = [0.99826, 0.99818, 0.99828]

# Ponto a interpolar
T_alvo = 37.5

# Calcular valor interpolado
c_interpolado = newton_interp(T_celsius, c_especifico, T_alvo)

# Print ajustado para o contexto correto
print(f"Valor estimado do calor específico para {T_alvo}°C: {c_interpolado:.8f}")