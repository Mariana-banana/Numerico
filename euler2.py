import numpy as np
import matplotlib.pyplot as plt

def metodo_euler_sistema(f, y0, t0, h, t_final):
    """
    Resolve um sistema de EDOs y' = f(t, y) usando o Método de Euler.
    'y' pode ser um número ou um vetor que representa o estado do sistema.
    """
    # Garante que a condição inicial seja um array numpy para consistência
    y0 = np.array(y0, dtype=float)

    tempos = [t0]
    valores_y = [y0]
    
    t_atual = t0
    y_atual = y0

    # Calcula o número de passos para garantir que o tempo final seja alcançado
    num_passos = int(round((t_final - t0) / h))
    
    for _ in range(num_passos):
        # A fórmula de Euler é aplicada aqui
        y_proximo = y_atual + h * f(t_atual, y_atual)
        t_atual += h
        
        tempos.append(t_atual)
        valores_y.append(y_proximo)
        y_atual = y_proximo
        
    return np.array(tempos), np.array(valores_y)

# --- DEFINIÇÃO DO PROBLEMA: u' = u*t ---
if __name__ == '__main__':
    # 1. Mudar a função f(t, y) para representar a nova equação u' = u*t
    #    Usamos 'u' como a variável dependente em vez de 'y'.
    def f_problema(t, u):
        #return u * t
        return np.sin(u)
        
    # 2. Atualizar as condições iniciais e os parâmetros da simulação
    # Condição Inicial: u(1) = 0.1
    u_inicial = 1    # 0.1  # Agora é um único número (escalar)
    t_inicial = 0.0  # 1    # O tempo inicial é 1

    # Parâmetros da Simulação
    passo_h = 0.02
    tempo_final = 2.0    # Objetivo: encontrar u(2)
    
    # --- RESOLVENDO E EXIBINDO OS RESULTADOS ---
    tempos, resultados_u = metodo_euler_sistema(f_problema, u_inicial, t_inicial, passo_h, tempo_final)
    
    # 3. Ajustar a exibição do resultado final
    # O resultado será um array de valores. Pegamos o último.
    # Como a função retorna um array 2D mesmo para um caso escalar, 
    # pegamos o último elemento com resultados_u[-1].
    resultado_final = resultados_u[-1]
    
    print(f"--- Aproximação de u(t) em t = {tempo_final} ---")
    print(f"Usando o Método de Euler com passo h = {passo_h}")
    # Usamos :.6f para mostrar o resultado com 6 casas decimais para maior precisão
    print(f"O valor aproximado de u({tempo_final}) é: {resultado_final:.6f}")

    # --- Plotar o Gráfico (Opcional, mas útil para visualização) ---
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, resultados_u, label=f'u(t) - Euler com h={passo_h}', color='blue', marker='o', linestyle='--')
    plt.xlabel("Tempo (t)")
    plt.ylabel("Valor de u(t)")
    plt.title("Solução de u' = u*t pelo Método de Euler")
    plt.grid(True)
    plt.legend()
    plt.show()