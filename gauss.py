import numpy as np
import sympy as sp

def gauss_legendre_integral(f_expr, a, b, n):
    x = sp.Symbol('x')
    f_lambdified = sp.lambdify(x, f_expr, 'numpy')

    # Obtém os nós e pesos da quadratura de Gauss-Legendre no intervalo [-1, 1]
    nodes, weights = np.polynomial.legendre.leggauss(n)

    # Mudança de variável para o intervalo [a, b]
    # x_i = 0.5 * (b - a) * t_i + 0.5 * (b + a)
    transformed_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
    transformed_weights = 0.5 * (b - a) * weights

    # Soma dos produtos peso * f(x_i)
    integral = sum(w * f_lambdified(xi) for xi, w in zip(transformed_nodes, transformed_weights))
    return integral

# Exemplo 1: Questão da imagem — ∫_{-1}^{1} x^5 dx com n = 2
x = sp.Symbol('x')
f_expr = x**5
resultado = gauss_legendre_integral(f_expr, -1, 1, n=2)
print(f"{f_expr}:", resultado)

# Exemplo 2: ∫_0^2 sqrt(x+1) dx com n=3
f_expr2 = sp.exp(-4*x)
resultado2 = gauss_legendre_integral(f_expr2, 2, 8, n=2)
print(f"{f_expr2}:", resultado2)


def gauss_legendre(f, a, b, n):
    # Nós e pesos para n = 2
    if n == 2:
        nodes = [-1/np.sqrt(3), 1/np.sqrt(3)]
        weights = [1, 1]
    else:
        raise ValueError("Este script só trata n=2, por enquanto.")

    result = 0
    for i in range(n):
        # Mudança de variável
        x_i = (b - a)/2 * nodes[i] + (b + a)/2
        result += weights[i] * f(x_i)

    result *= (b - a)/2
    return result

# Função da questão 17
f = lambda x: np.exp(-4*x)

#f = lambda x: x**5

# Intervalo de integração
a, b = 2, 8

# Cálculo
resultado = gauss_legendre(f, a, b, 2)
print(f"Resultado com Gauss-Legendre n=2: {resultado:.10f}")
