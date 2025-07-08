import numpy as np
import matplotlib.pyplot as plt
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# Definição do sistema de equações diferenciais
# state: um vetor [x, y]
# t: o tempo atual (independente neste caso, mas necessário para a forma geral)
def modelo(t, state):
    """
    Modelo do sistema de equações diferenciais.
    Exemplo:
    x' = 2x - 0.02xy
    y' = 0.0005xy - 0.8y
    """
    x, y = state
    dxdt = -0.9*y                   
    dydt = -0.8*x
    return np.array([dxdt, dydt])

# Função Runge-Kutta de 4ª ordem para resolver sistemas de EDOs
def runge_kutta_sistema(t0, y0, t_final, h):
    """
    Resolve um sistema de EDOs usando o método RK4.

    Args:
        t0 (float): Tempo inicial.
        y0 (list or np.array): Vetor de condições iniciais [x0, y0, ...].
        t_final (float): Tempo final da simulação.
        h (float): Tamanho do passo.

    Returns:
        tuple: Uma tupla contendo a lista de tempos e a lista de vetores de solução.
    """
    # Número de iterações
    n = int((t_final - t0) / h)
    
    # ---- CORREÇÃO APLICADA AQUI ----
    # Inicializa o vetor de solução y com as condições iniciais,
    # garantindo que o tipo seja float para aceitar resultados decimais.
    y = np.array(y0, dtype=float)
    
    # Listas para armazenar os resultados para visualização
    t_valores = [t0]
    y_valores = [y.copy()]

    # Itera para o número de passos
    for _ in range(n):
        # Aplica as fórmulas de Runge-Kutta para vetores
        k1 = h * modelo(t0, y)
        k2 = h * modelo(t0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * modelo(t0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * modelo(t0 + h, y + k3)

        # Atualiza o próximo valor do vetor y 
        y += (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        # Atualiza o tempo
        t0 += h
        
        # Armazena os novos valores
        t_valores.append(t0)
        y_valores.append(y.copy())

        print(f"t = {t0:10f}, x = {y[0]:10f}, y = {y[1]:10f}")

    return t_valores, np.array(y_valores)

# --- Seção Principal (Driver) ---

# Condições iniciais e parâmetros do problema
t0 = 0.0  # Tempo inicial
t_final = 1.4742  # Tempo final da simulação
condicoes_iniciais = [1000, 800]  # y0 = [x(0), y(0)]
h = 0.00001

# Chama a função para resolver o sistema
t_resultados, y_resultados = runge_kutta_sistema(t0, condicoes_iniciais, t_final, h)

# Extrai os valores finais
#valor_final_x = y_resultados[-1, 0]
#valor_final_y = y_resultados[-1, 1]