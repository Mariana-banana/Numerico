import numpy as np

def regra_trapezio(f, a, b, n):
    """
    Calcula a integral de f(x) de 'a' até 'b' usando a Regra dos Trapézios
    com 'n' subintervalos.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Fórmula: h/2 * [y0 + 2y1 + 2y2 + ... + yn]
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

def regra_simpson(f, a, b, n):
    """
    Calcula a integral de f(x) de 'a' até 'b' usando a Regra 1/3 de Simpson
    com 'n' subintervalos.
    """
    # Validação: n deve ser par para a Regra 1/3 de Simpson
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par para a Regra de Simpson.")
        
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Fórmula: h/3 * [y0 + 4y1 + 2y2 + 4y3 + ... + yn]
    soma_impares = np.sum(y[1:-1:2])
    soma_pares = np.sum(y[2:-1:2])
    
    integral = (h / 3) * (y[0] + y[-1] + 4 * soma_impares + 2 * soma_pares)
    return integral


# --- ÁREA DE CONFIGURAÇÃO E EXECUÇÃO ---
if __name__ == '__main__':
    
    # 1. Defina a sua função a ser integrada
    def f(x):
        return np.pi * (100 - x**2)

    # 2. Defina o intervalo de integração
    a = 0.0
    b = 10.0
    
    print("--- Resultados para a integral de ln(x)/e^x de 1 a 10 ---")
    
    # --- Simulação para "Regra Simples de Simpson" (n=2) ---
    n_simples = 2
    resultado_simples = regra_simpson(f, a, b, n_simples)
    resultado_simples *= 2
    print(f"\nResultado com Simpson para n={n_simples}: {resultado_simples:.10f}")
    
    # --- Simulação para "Regra Composta com 4 nós" (n=4) ---
    # Nota: 4 nós geralmente implica n=3. Mas para Simpson 1/3, n deve ser par.
    # A interpretação mais provável é n=4 subintervalos (5 nós).
    n_composto = 4
    resultado_composto = regra_simpson(f, a, b, n_composto)
    print(f"Resultado com Simpson para n={n_composto}: {resultado_composto:.10f}")
    
    # --- Verificação do valor de Trapézio do enunciado ---
    # O valor 1,359... no enunciado parece ser um erro de digitação.
    # Vamos calcular o valor correto com n=2 para mostrar.
    resultado_trapezio_n2 = regra_trapezio(f, a, b, 2)
    print(f"\nTeste: Resultado com Trapézios para n=2: {resultado_trapezio_n2:.10f}")