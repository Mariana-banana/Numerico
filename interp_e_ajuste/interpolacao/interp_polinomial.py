import numpy as np
import matplotlib.pyplot as plt

# Dados
P = np.array([700, 710, 720, 730, 740, 780], dtype=float)
T = np.array([97.71, 98.11, 98.49, 98.88, 99.26, 100.73], dtype=float)

# Ajuste linear
coef_linear = np.polyfit(P, T, 1)
p_linear = np.poly1d(coef_linear)
erro_linear = np.mean((T - p_linear(P))**2)

# Ajuste quadrático
coef_quad = np.polyfit(P, T, 2)
p_quad = np.poly1d(coef_quad)
erro_quad = np.mean((T - p_quad(P))**2)

# Ajuste cúbico
coef_cub = np.polyfit(P, T, 3)
p_cub = np.poly1d(coef_cub)
erro_cub = np.mean((T - p_cub(P))**2)

# Exibir
print("Função linear:", p_linear)
print("Erro linear:", erro_linear)
print("Função quadrática:", p_quad)
print("Erro quadrático:", erro_quad)
print("Função cúbica:", p_cub)
print("Erro cúbico:", erro_cub)
