import numpy as np
from math import comb

# ===================================================================
#                      ÁREA DE CONFIGURAÇÃO
# ===================================================================

# 1. Defina a sua função f(x)
def f(x):
    # Exemplo: f(x) = x^4. Vamos calcular sua 3ª derivada.
    return np.cos(2 * x)

# 2. Ponto 'x' onde a derivada será calculada
x_ponto = 0.7

# 3. Ordem da derivada que você quer calcular (1, 2, 3, etc.)
ordem_da_derivada = 2

# 4. Lista de valores de 'h' para testar
h_valores = [0.1, 0.01, 0.001]

# ===================================================================
#             FUNÇÃO GENERALIZADA (NÃO PRECISA MEXER)
# ===================================================================

def derivada_numerica(func, x, n, h):
    """
    Calcula a n-ésima derivada de uma função 'func' em um ponto 'x'
    usando a fórmula de diferenças finitas centradas de ordem n.

    Args:
        func: A função a ser derivada.
        x: O ponto de avaliação.
        n: A ordem da derivada (1, 2, 3, ...).
        h: O tamanho do passo.

    Returns:
        A aproximação numérica da n-ésima derivada.
    """
    soma = 0.0
    # Fórmula geral: 1/h^n * Σ [(-1)^k * (n C k) * f(x + (n/2 - k)h)]
    for k in range(n + 1):
        termo_sinal = (-1)**k
        coef_binomial = comb(n, k) # (n C k) - Combinação de n, k a k
        ponto_f = x + (n / 2 - k) * h
        soma += termo_sinal * coef_binomial * func(ponto_f)

    return soma / (h**n)

# ===================================================================
#                         EXECUÇÃO
# ===================================================================

print("=====================================================")
print(f"  Cálculo da Derivada de Ordem {ordem_da_derivada} em x = {x_ponto}")
print("=====================================================")

for h in h_valores:
    resultado = derivada_numerica(f, x_ponto, ordem_da_derivada, h)
    print(f"Para h = {h}:    f^({ordem_da_derivada})({x_ponto}) ≈ {resultado:.6f}")

# Para referência, o valor real de f'''(x) para f(x)=x^4 é 24x.
# Em x=2, o valor real é 24 * 2 = 48.
valor_real = 24 * x_ponto
print("-----------------------------------------------------")
print(f"Valor Real de Referência: {valor_real}")
print("=====================================================")

# Defina a Função f(x): Na área de configuração, altere a linha return np.cos(2 * x) para qualquer função que desejar. Por exemplo, para f(x)=x 
# 3
#  +5x−10, você escreveria return x**3 + 5*x - 10.
# np.log(x) 
# np.exp(x)