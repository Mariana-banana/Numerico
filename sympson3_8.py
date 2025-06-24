import numpy as np

def f_debye_segura(x):
    return np.where(x == 0, 0.0, (x**3) / (np.exp(x) - 1))

def integral_trapezios(f, a, b, n):
    h = (b - a) / n
    x_pontos = np.linspace(a, b, n + 1)
    y_valores = f(x_pontos)
    soma = y_valores[0] + y_valores[-1] + 2 * np.sum(y_valores[1:-1])
    return (h / 2) * soma

def integral_simpson_3_8(f, a, b):
    """
    Calcula a integral usando a Regra 3/8 de Simpson (n=3).
    """
    n = 3
    h = (b - a) / n
    x0, x1, x2, x3 = np.linspace(a, b, n + 1)
    
    # Fórmula: 3h/8 * [y0 + 3y1 + 3y2 + y3]
    integral = (3 * h / 8) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3))
    return integral

# --- Resolvendo a Questão 19 ---
a, b = 0, 2

# Valor exato (para referência)
valor_exato = 1.176342

# Cálculo pelos métodos numéricos com n=3
integral_trap = integral_trapezios(f_debye_segura, a, b, 3)
integral_simp38 = integral_simpson_3_8(f_debye_segura, a, b)

# --- Comparando os Resultados ---
print("--- Comparação de Métodos para a Integral (n=3) ---")
print(f"Regra 3/8 de Simpson (n=3):   {integral_simp38:.6f}")
print(f"Regra dos Trapézios (n=3):    {integral_trap:.6f}")

# Cálculo final de D(2) usando o método mais preciso
D_2 = (3/8) * integral_simp38
print(f"\nResultado final para D(2) usando Simpson 3/8: {D_2:.4f}")