import numpy as np
import matplotlib.pyplot as plt

# --- Dados do Problema ---
# P(mm Hg) é a variável independente (x)
# T (°C) é a variável dependente (y)
P = np.array([700, 710, 720, 730, 740, 780])
T = np.array([97.71, 98.11, 98.49, 98.88, 99.26, 100.73])

# --- Passo 1: Linearização do Modelo Potência ---
# O modelo y = a * x^b se torna ln(y) = ln(a) + b * ln(x).
# Isso é uma reta Y = A + B*X, onde:
# Y = ln(y), X = ln(x), A = ln(a), e B = b.
try:
    log_P = np.log(P)
    log_T = np.log(T)
except ValueError:
    print("Erro: Os dados devem ser positivos para a aproximação por potência.")
    exit()

# --- Passo 2: Ajuste Linear (Regressão) nos Dados Logarítmicos ---
# Ajusta um polinômio de grau 1 (uma reta) aos dados transformados.
# np.polyfit(X, Y, 1) retorna [B, A] da equação Y = B*X + A.
coefs = np.polyfit(log_P, log_T, 1)
b = coefs[0]
A = coefs[1]

# --- Passo 3: Encontrar os Coeficientes Originais 'a' e 'b' ---
# O expoente 'b' é o próprio coeficiente angular (slope) da reta.
# O coeficiente 'a' é a exponencial do coeficiente linear (intercept), pois A = ln(a).
a = np.exp(A)

# --- Passo 4: Exibir os Resultados ---
print("--- Aproximação por Função Potência: y = a * x^b ---")
print(f"Coeficiente 'a' encontrado: {a:.4f}")
print(f"Coeficiente 'b' (expoente) encontrado: {b:.4f}")
print(f"\nA função potência que melhor se ajusta é: T(P) = {a:.4f} * P^{b:.4f}\n")

# --- Passo 5: Visualização Gráfica ---
# Gera pontos para uma curva suave do modelo ajustado
P_plot = np.linspace(min(P), max(P), 200)
# Calcula os valores T correspondentes usando a função potência encontrada
T_plot = a * (P_plot ** b)

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(P, T, color='red', label='Dados Originais')
plt.plot(P_plot, T_plot, color='blue', label=f'Ajuste Potência: T = {a:.2f} * P^{b:.2f}')
plt.xlabel("Pressão (P em mm Hg)")
plt.ylabel("Temperatura (T em °C)")
plt.title("Ajuste de Curva Potência: Temperatura de Ebulição vs. Pressão")
plt.grid(True)
plt.legend()
plt.show()