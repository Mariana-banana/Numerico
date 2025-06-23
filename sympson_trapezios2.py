import numpy as np
from math import ceil, sqrt
from scipy.integrate import quad

# Método dos Trapézios
def trapezios(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return h * soma / 2

# Método de Simpson
def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n deve ser par para o método de Simpson.")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        soma += 2 * f(a + i * h)
    return h * soma / 3

# Cálculo de n mínimo dado erro para trapézios
def n_para_erro_trapezios(f2max, a, b, erro):
    return ceil(sqrt((f2max * (b - a)**3) / (12 * erro)))

# Cálculo de n mínimo dado erro para Simpson
def n_para_erro_simpson(f4max, a, b, erro):
    n = ceil(((f4max * (b - a)**5) / (180 * erro))**0.25)
    return n + (n % 2)  # garantir par

# Funções das questões
def f13(x):
    return np.exp(-x**2)

def f14(x):
    return 1 / (2 * x)

def f15(x):
    return 1 / (1 + x**4)

# CONFIGURAÇÕES (MODIFIQUE APENAS ESTA PARTE PARA OUTRAS QUESTÕES)
f = f13        # função da questão (f13, f14, f15, ou defina outra)
a, b = 0, 1     # intervalo de integração
n = 1000        # número de subintervalos para métodos
erro_desejado = 1e-5  # erro máximo tolerado (para h)

# --- EXECUÇÃO ---
print(f"\nIntegração de f(x) no intervalo [{a}, {b}]:")
print(f"Trapézios com n={n}: {trapezios(f, a, b, n):.10f}")
print(f"Simpson com n={n if n % 2 == 0 else n+1}: {simpson(f, a, b, n if n % 2 == 0 else n+1):.10f}")
real, _ = quad(f, a, b)
print(f"Valor real (quad): {real:.10f}")

# Se desejar calcular n necessário para erro
# Para isso, informe f2max ou f4max manualmente conforme a questão
if f == f14:
    f2max = 1      # Máximo de |f''(x)| no intervalo [1, 3]
    f4max = 15     # Máximo de |f⁽⁴⁾(x)| no intervalo [1, 3]
    n_trap = n_para_erro_trapezios(f2max, a, b, erro_desejado)
    n_simp = n_para_erro_simpson(f4max, a, b, erro_desejado)
    print(f"\n>> Para erro ≤ {erro_desejado:.0e} em f14(x)=1/(2x):")
    print(f"Trapézios: n mínimo = {n_trap}")
    print(f"Simpson:   n mínimo = {n_simp}")
