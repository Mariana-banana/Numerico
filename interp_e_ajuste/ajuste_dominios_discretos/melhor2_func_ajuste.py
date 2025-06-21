import numpy as np
from numpy.polynomial import Polynomial
from scipy.optimize import curve_fit

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)

# Funções que vamos usar
def exp_func(x, a, b):
    return a * np.exp(b*x)

def power_func(x, a, b):
    return a * np.power(x, b)

# Dados de exemplo
x_axis = np.array([10, 20, 30, 40, 60, 70])
y_axis = np.array([0.313, 0.250, 0.215, 0.192, 0.164, 0.154])

# Armazenar R²
r2_scores = {}

# 1) Linear
p_linear = Polynomial.fit(x_axis, y_axis, deg=1)
y_pred_linear = p_linear(x_axis)
r2_scores['linear'] = r_squared(y_axis, y_pred_linear)

# 2) Quadrática
p_quad = Polynomial.fit(x_axis, y_axis, deg=2)
y_pred_quad = p_quad(x_axis)
r2_scores['quadratic'] = r_squared(y_axis, y_pred_quad)

# 3) Cúbica
p_cubic = Polynomial.fit(x_axis, y_axis, deg=3)
y_pred_cubic = p_cubic(x_axis)
r2_scores['cubic'] = r_squared(y_axis, y_pred_cubic)

# 4) Exponencial
try:
    params_exp, _ = curve_fit(exp_func, x_axis, y_axis, p0=(1, 0.1))
    y_pred_exp = exp_func(x_axis, *params_exp)
    r2_scores['exponential'] = r_squared(y_axis, y_pred_exp)
except RuntimeError:
    r2_scores['exponential'] = -np.inf

# 5) Potência
try:
    params_power, _ = curve_fit(power_func, x_axis, y_axis, p0=(1, 1))
    y_pred_power = power_func(x_axis, *params_power)
    r2_scores['power'] = r_squared(y_axis, y_pred_power)
except RuntimeError:
    r2_scores['power'] = -np.inf

# Encontrar o melhor
best_fit = max(r2_scores, key=r2_scores.get)

for score in r2_scores.items():
    print(f"R² para ajuste {score[0]}: {score[1]:.4f}")

print(f"\nMelhor tipo de ajuste: {best_fit}")
