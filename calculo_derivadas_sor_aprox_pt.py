import numpy as np
from scipy.interpolate import interp1d

# =======================
# ÁREA DE ENTRADA
# =======================
x_vals = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
f_vals = np.array([2.415, 2.637, 2.907, 3.193, 3.381])

x_ponto = 0.4  # Pode ser qualquer valor dentro do intervalo dos dados

# =======================
# INTERPOLAÇÃO
# =======================
# Função interpolada (cúbica por padrão)
f_interp = interp1d(x_vals, f_vals, kind='cubic', fill_value="extrapolate")

# Espaçamento h (usar o mínimo entre espaçamentos consecutivos)
h_list = np.diff(x_vals)
h = np.min(h_list)

# Pontos ao redor de x_ponto para diferenças centralizadas
x_m2h = x_ponto - 2*h
x_mh  = x_ponto - h
x_ph  = x_ponto + h
x_p2h = x_ponto + 2*h

# Avaliação dos valores interpolados
f_m2h = f_interp(x_m2h)
f_mh  = f_interp(x_mh)
f_0   = f_interp(x_ponto)
f_ph  = f_interp(x_ph)
f_p2h = f_interp(x_p2h)

# =======================
# CÁLCULO DAS DERIVADAS
# =======================
# 1ª Derivada
f1 = (f_ph - f_mh) / (2*h)

# 2ª Derivada
f2 = (f_ph - 2*f_0 + f_mh) / (h**2)

# 3ª Derivada
f3 = (f_p2h - 2*f_ph + 2*f_mh - f_m2h) / (2*h**3)

# =======================
# RESULTADOS
# =======================
print(f"f'({x_ponto}) ≈ {f1:.6f}")
print(f"f''({x_ponto}) ≈ {f2:.6f}")
print(f"f'''({x_ponto}) ≈ {f3:.6f}")
