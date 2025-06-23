import numpy as np

# =======================
# ÁREA DE ENTRADA
# =======================
# Valores de x e f(x)
x_vals = [0.2, 0.4, 0.6, 0.8, 1.0]
f_vals = [2.415, 2.637, 2.907, 3.193, 3.381]

# Ponto de interesse
x_ponto = 0.4

# =======================
# CÁLCULO DAS DERIVADAS
# =======================

# Índice do ponto de interesse
i = x_vals.index(x_ponto)

# Espaçamento h (assumindo espaçamento constante)
h = x_vals[1] - x_vals[0]

# 1ª Derivada Central
f1 = (f_vals[i + 1] - f_vals[i - 1]) / (2 * h)

# 2ª Derivada Central
f2 = (f_vals[i + 1] - 2 * f_vals[i] + f_vals[i - 1]) / (h ** 2)

# 3ª Derivada Central
# Utiliza pontos à esquerda e à direita de x - requer 2 antes e 2 depois
f3 = (f_vals[i + 2] - 2 * f_vals[i + 1] + 2 * f_vals[i - 1] - f_vals[i - 2]) / (2 * h ** 3)

# =======================
# RESULTADOS
# =======================
print(f"f'({x_ponto}) ≈ {f1:.6f}")
print(f"f''({x_ponto}) ≈ {f2:.6f}")
print(f"f'''({x_ponto}) ≈ {f3:.6f}")
