import sympy as sp
import numpy as np

def integra_com_erro(f_expr, a, b, erro_desejado=None, digse=None):
    x = sp.Symbol('x')
    f = f_expr
    f_lambdified = sp.lambdify(x, f, 'numpy')

    # Integral exata
    integral_exata = sp.integrate(f, (x, a, b)).evalf()
    valor_exato = float(integral_exata)

    # Se for fornecido digse, converte em erro relativo
    if digse is not None:
        erro_desejado = 0.5 * 10**(-digse)

    if erro_desejado is None:
        erro_desejado = 1e-6  # valor padrão

    # Segunda e quarta derivadas
    f2 = sp.diff(f, x, 2)
    f4 = sp.diff(f, x, 4)

    # Avaliar máximos numéricos
    x_vals = np.linspace(a, b, 1000)
    f2_lamb = sp.lambdify(x, f2, 'numpy')
    f4_lamb = sp.lambdify(x, f4, 'numpy')

    f2_max = np.max(np.abs(f2_lamb(x_vals)))
    f4_max = np.max(np.abs(f4_lamb(x_vals)))

    def erro_trapezio(h):
        return (b - a) / 12 * h**2 * f2_max

    def erro_simpson(h):
        return (b - a) / 180 * h**4 * f4_max

    # Método dos trapézios
    n_trap = 1
    while erro_trapezio((b - a)/n_trap) > erro_desejado:
        n_trap += 1

    def trapezio_integral(n):
        h = (b - a) / n
        x_pts = np.linspace(a, b, n+1)
        y_vals = f_lambdified(x_pts)
        T = y_vals[0] + y_vals[-1] + 2 * np.sum(y_vals[1:-1])
        return h / 2 * T

    approx_trap = trapezio_integral(n_trap)
    erro_abs_trap = abs(approx_trap - valor_exato)

    # Método de Simpson
    n_simp = 2
    while erro_simpson((b - a)/n_simp) > erro_desejado:
        n_simp += 2

    def simpson_integral(n):
        h = (b - a) / n
        x_pts = np.linspace(a, b, n + 1)
        y_vals = f_lambdified(x_pts)
        return h / 3 * (y_vals[0] + y_vals[-1]
                        + 4 * np.sum(y_vals[1:-1:2])
                        + 2 * np.sum(y_vals[2:-2:2]))

    approx_simp = simpson_integral(n_simp)
    erro_abs_simp = abs(approx_simp - valor_exato)

    # Resultados
    print("=== Integral Exata ===")
    print(f"∫_{a}^{b} f(x) dx = {valor_exato:.10f}")

    print("\n--- Método dos Trapézios ---")
    print(f"n = {n_trap}, h = {(b - a)/n_trap}")
    print(f"Aproximação = {approx_trap}")
    print(f"Erro absoluto = {erro_abs_trap}")

    print("\n--- Método de Simpson ---")
    print(f"n = {n_simp}, h = {(b - a)/n_simp}")
    print(f"Aproximação = {approx_simp}")
    print(f"Erro absoluto = {erro_abs_simp}")
    
x = sp.Symbol('x')

"""CALCULOS DE SIMPON E TRAPEZIOS COM ERRO, COM E SEM DIGSE"""

# Exemplo 1: ln
#f_expr = 1 / (2 * x)
#integra_com_erro(f_expr, 1, 3)

# Exemplo 2: exponencial
#f_expr = sp.exp(-x**3)
#integra_com_erro(f_expr, 0, 1)

# Exemplo 3: trigonometria
#f_expr = sp.sin(x)
#integra_com_erro(f_expr, 0, sp.pi)


#f_expr = 1 / (1 + x**4)
f_expr = sp.ln(x) / sp.exp(x)
integra_com_erro(f_expr, 1, 10)

#f_expr = 1 / (1 + x**4)
#integra_com_erro(f_expr, 0, 1, digse=4)

#f_expr = sp.exp(-x**3)
#integra_com_erro(f_expr, 0, 1)

"""2 CÓDIGOS DIFERENTES QUE CALCULAM PI COM SIMPSON, COM N VARIAVEL"""

# Exemplo específico da questão: calcular pi com 4 subintervalos por Simpson
f_expr_pi = 1 / (1 + x**2)

def simpson_pi_4_subintervals(f_expr, a, b, n=6):
    """Calcula pi usando a regra de Simpson com a forma robusta de fatiamento."""
    
    f_lamb = sp.lambdify(x, f_expr, 'numpy')
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f_lamb(x_vals)
    
    # Separação robusta dos termos
    soma_impares = np.sum(y_vals[1:-1:2]) # Soma y1, y3
    soma_pares = np.sum(y_vals[2:-2:2]) # Soma y2

    # Aplica a fórmula de Simpson
    integral = (h / 3) * (y_vals[0] + y_vals[-1] + 4 * soma_impares + 2 * soma_pares)
    
    pi_aprox = 4 * integral
    
    print("\n=== Estimativa de π usando Simpson com 4 subintervalos (CORRIGIDO) ===")
    print(f"Aproximação de π = {pi_aprox:.10f}")
    print(f"Erro absoluto = {abs(np.pi - pi_aprox):.10f}")

# Executa a função
#simpson_pi_4_subintervals(f_expr_pi, 0, 1)

def calcular_pi_simpson(n):
    """
    Calcula uma aproximação de π usando a Regra de Simpson para um número n genérico
    de subintervalos.

    Argumentos:
        n (int): O número de subintervalos. Deve ser um número par.

    Retorna:
        float: O valor aproximado de π.
    """
    # 1. Validação: Garante que n é um número par
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par para a Regra de Simpson.")

    # 2. Configuração do problema
    a = 0  # Limite inferior da integral
    b = 1  # Limite superior da integral
    h = (b - a) / n

    # 3. Cria os pontos x e calcula os valores de y
    x_vals = np.linspace(a, b, n + 1)
    y_vals = 1 / (1 + x_vals**2)

    # 4. Soma os termos usando o fatiamento robusto
    soma_impares = np.sum(y_vals[1:-1:2]) # Soma y1, y3, ..., y(n-1)
    soma_pares = np.sum(y_vals[2:-1:2])   # Soma y2, y4, ..., y(n-2)

    # 5. Calcula a integral e o valor de pi
    integral = (h / 3) * (y_vals[0] + y_vals[-1] + 4 * soma_impares + 2 * soma_pares)
    pi_aprox = 4 * integral
    
    # 6. Retorna o valor calculado
    return pi_aprox

# Exemplo de uso da função genérica

# Teste para n=4 (para conferir com o resultado anterior)
#pi_para_n4 = calcular_pi_simpson(6)
#print(f"Para n = 4,   π ≈ {pi_para_n4:.15f}")

# Teste para n=10
#pi_para_n10 = calcular_pi_simpson(10)
#print(f"Para n = 10,  π ≈ {pi_para_n10:.15f}")

# Teste para n=100
#pi_para_n100 = calcular_pi_simpson(100)
#print(f"Para n = 100, π ≈ {pi_para_n100:.15f}")

# Valor real de π para comparação
#print(f"Valor Real, π = {np.pi:.15f}")

"""TRAPÉZIOS COM h VARIÁVEL"""

def trapezio_integral_manual(f_expr, a, b, n):
    x = sp.Symbol('x')
    f_lambdified = sp.lambdify(x, f_expr, 'numpy')
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f_lambdified(x_vals)
    T = y_vals[0] + y_vals[-1] + 2 * np.sum(y_vals[1:-1])
    return h / 2 * T

f_expr = sp.sqrt(3*x + 5)
resultado = trapezio_integral_manual(f_expr, 1, 8, 7)
print(f"Resultado com n=7 e h=1: {resultado}")

import numpy as np

# 1. Função numericamente estável para f(x)
def f_debye_segura(x):
    """
    Calcula x**3 / (e**x - 1), tratando o caso especial x=0.
    Usa np.where para funcionar com arrays inteiros de uma só vez.
    """
    # Condição: onde x é 0?
    # Se for verdade: use o valor 0.0 (o limite da função)
    # Se for falso: use a fórmula normal
    return np.where(x == 0, 0.0, (x**3) / (np.exp(x) - 1))

# 2. Implementação da Regra dos Trapézios
def integral_trapezios(f, a, b, n):
    """
    Calcula a integral de uma função 'f' usando a Regra dos Trapézios.
    """
    h = (b - a) / n
    x_pontos = np.linspace(a, b, n + 1)
    y_valores = f(x_pontos) # A função segura já lida com o array
    
    # Fórmula dos Trapézios
    soma = y_valores[0] + y_valores[-1] + 2 * np.sum(y_valores[1:-1])
    return (h / 2) * soma

# --- Resolvendo a Questão 19 ---
# Parâmetros do problema
a, b, n = 0, 2, 3


# Etapa A: Calcular a integral usando a função segura
integral_I = integral_trapezios(f_debye_segura, a, b, n)

# Etapa B: Calcular o valor final de D(2)
#D_2 = (3/8) * integral_I

print("--- Resultado Corrigido (Questão 19) ---")
print(f"Valor da integral (I): {integral_I:.6f}")
#print(f"Resultado final para D(2): {D_2:.4f}")