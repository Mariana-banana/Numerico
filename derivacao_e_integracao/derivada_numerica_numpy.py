import numpy as np
from numpy.polynomial import Polynomial

# Dados
x = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
y = np.array([2.415, 2.637, 2.907, 3.193, 3.381])

# Ajustar um polinômio de grau 4 (pontos suficientes)
p = Polynomial.fit(x, y, deg=4)

# Derivadas
p1 = p.deriv(1)  # 1ª derivada
p2 = p.deriv(2)  # 2ª derivada
p3 = p.deriv(3)  # 3ª derivada
p4 = p.deriv(4)  # 4ª derivada

# Avaliando em x=0.4
x_eval = 0.4
print(f"f'(0.4) ≈ {p1(x_eval):.6f}")
print(f"f''(0.4) ≈ {p2(x_eval):.6f}")
print(f"f'''(0.4) ≈ {p3(x_eval):.6f}")
print(f"f''''(0.4) ≈ {p4(x_eval):.6f}")