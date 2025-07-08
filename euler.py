import numpy as np
import matplotlib.pyplot as plt

def metodo_euler_sistema(f, y0, t0, h, t_final):
    """
    Resolve um sistema de EDOs y' = f(t, y) usando o Método de Euler.
    'y' é um vetor que representa o estado do sistema.
    """
    tempos = [t0]
    valores_y = [np.array(y0, dtype=float)]
    
    t_atual = t0
    y_atual = np.array(y0, dtype=float)

    # Loop para iterar até o tempo final
    num_passos = int((t_final - t0) / h)
    for _ in range(num_passos):
        y_proximo = y_atual + h * f(t_atual, y_atual)
        t_atual += h
        
        tempos.append(t_atual)
        valores_y.append(y_proximo)
        y_atual = y_proximo
        
    return np.array(tempos), np.array(valores_y)

# --- DEFINIÇÃO DO PROBLEMA (PREDADOR-PRESA) ---
if __name__ == '__main__':
    # A função F(t, Y) que define o sistema de EDOs
    def f_problema(t, y):
        x_pop, y_pop = y  # Desempacota o vetor de estado
        
        # Equações do sistema
        dxdt = 2 * x_pop - 0.02 * x_pop * y_pop
        dydt = 0.0005 * x_pop * y_pop - 0.8 * y_pop
        
        return np.array([dxdt, dydt])
        #return y**2

    # Condições Iniciais: x(0) = 3000, y(0) = 120
    y_inicial = [0.1]
    t_inicial = 1
    
    # Parâmetros da Simulação
    passo_h = 0.1
    tempo_final = 2.0 # Objetivo: encontrar o estado em t=10
    
    # --- RESOLVENDO E EXIBINDO OS RESULTADOS ---
    tempos, populacoes = metodo_euler_sistema(f_problema, y_inicial, t_inicial, passo_h, tempo_final)
    
    populacao_final = populacoes[-1]
    
    print("--- Resultado da Simulação em t = 10 ---")
    print(f"População de Presas (x) em t=10: {populacao_final[0]:.4f}")
    print(f"População de Predadores (y) em t=10: {populacao_final[1]:.4f}")

    # --- Plotar o Gráfico ---
    plt.figure(figsize=(12, 7))
    plt.plot(tempos, populacoes[:, 0], label='Presas (x)', color='green')
    plt.plot(tempos, populacoes[:, 1], label='Predadores (y)', color='red')
    plt.xlabel("Tempo (t)")
    plt.ylabel("População")
    plt.title("Modelo Predador-Presa pelo Método de Euler")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # Para a questão 2 do pdf exercicios
    
'''    # Condição Inicial: x(0) = 1
    y_inicial = 1.0  # Agora é um único número, não uma lista
    t_inicial = 0

    # Parâmetros da Simulação
    # Vamos definir os dois valores de h que o problema pede
    h1 = 0.25
    h2 = 0.125
    tempo_final = 1.0  # O objetivo é encontrar x(1)
    
    # --- RESOLVENDO PARA CADA VALOR DE h ---

    # Caso 1: h = 0.25
    tempos1, resultados1 = metodo_euler_sistema(f_problema, y_inicial, t_inicial, h2, tempo_final)
    resultado_final_1 = resultados1[-1] # Pega o último valor calculado
    print(f"--- Resultado para h = {h2} ---")
    print(f"O valor aproximado de x(1) é: {resultado_final_1:.6f}")
'''