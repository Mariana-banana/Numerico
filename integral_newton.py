import numpy as np
import scipy.integrate as sci
import sympy as sp # Importa a biblioteca simbólica

# --- Funções de Interpolação (as mesmas de antes) ---
def divididas(x, y):
    n = len(x)
    coef = np.array(y, dtype=float)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def newton_interp(x_data, y_data, x_eval):
    coef = divididas(x_data, y_data)
    n = len(coef)
    resultado = coef[-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x_eval - x_data[i]) + coef[i]
    return resultado

# --- NOVA FUNÇÃO PARA MOSTRAR O POLINÔMIO ---
def mostrar_polinomio_newton(x_data, y_data):
    """
    Calcula e exibe o polinômio interpolador de Newton nas formas
    de Newton e padrão (expandida).
    """
    coef = divididas(x_data, y_data)
    n = len(coef)
    
    # Cria um símbolo 'x' para a álgebra
    x_sym = sp.Symbol('x')
    
    # Constrói o polinômio na forma aninhada de Newton simbolicamente
    P_symbolic = coef[-1]
    for i in range(n-2, -1, -1):
        P_symbolic = P_symbolic * (x_sym - x_data[i]) + coef[i]

    # Expande a expressão para a forma padrão (ax^2 + bx + c)
    P_expandido = sp.expand(P_symbolic)
    
    print("\n--- Polinômio Interpolador Encontrado ---")
    print("Forma de Newton (como foi construído):")
    sp.pprint(P_symbolic, use_unicode=True) # sp.pprint formata a saída
    
    print("\nForma Padrão (simplificada):")
    sp.pprint(P_expandido, use_unicode=True)
    print("----------------------------------------")


# --- RESOLVENDO A QUESTÃO DA INTEGRAL ---
if __name__ == '__main__':
    
    # Passo 0: Dados da tabela (exemplo) para e^x
    x_tabela = [1.0, 1.5, 2.0]
    y_tabela = [2.7183, 4.4817, 7.3891]
    
    # --- NOVO PASSO: MOSTRAR O POLINÔMIO ---
    mostrar_polinomio_newton(x_tabela, y_tabela)
    
    # Passo 1: Criar a função aproximada g(x) = x * P(x)
    def g_aproximada(x):
        polinomio_P_em_x = newton_interp(x_tabela, y_tabela, x)
        return x * polinomio_P_em_x

    # Passo 2: Integrar a função aproximada de 1 a 2
    resultado_aproximado, _ = sci.quad(g_aproximada, 1, 2)
    
    # Passo 3: Comparar com o valor exato
    def g_exata(x):
        return x * np.exp(x)
    resultado_exato, _ = sci.quad(g_exata, 1, 2)

    print("\n--- Resultado da Integral Numérica ---")
    print(f"O valor aproximado da integral é: {resultado_aproximado:.6f}")
    print(f"O valor exato da integral é:     {resultado_exato:.6f}")