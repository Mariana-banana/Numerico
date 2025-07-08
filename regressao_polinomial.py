import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Dados da tabela
P = np.array([700, 710, 720, 730, 740, 780], dtype=float)  # Pressão (mm Hg)
T = np.array([97.71, 98.11, 98.49, 98.88, 99.26, 100.73], dtype=float)  # Temperatura (°C)

P = np.array([5, 15, 25, 35])
T = np.array([10, 15, 20, 13])

# Ajuste polinomial de grau 2 (parabólico é suficiente nesse caso)
grau = 2
coefs = np.polyfit(P, T, grau)  # Ajusta um polinômio de grau 2

# Criação da função polinomial para uso e visualização
p = np.poly1d(coefs)

# Exibir função ajustada
print("Função ajustada (polinômio):")
print(p)

# Avaliar erro médio quadrático (opcional)
T_pred = p(P)
erro_medio = np.mean((T - T_pred)**2)
print(f"Erro médio quadrático: {erro_medio:.6f}")

# Visualização
P_plot = np.linspace(min(P), max(P), 200)
T_plot = p(P_plot)

plt.scatter(P, T, color='red', label='Dados originais')
plt.plot(P_plot, T_plot, label='Ajuste polinomial (grau 2)')
plt.xlabel("Pressão (mm Hg)")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura de ebulição da água vs Pressão")
plt.grid(True)
plt.legend()
plt.show()
