import numpy as np
import matplotlib.pyplot as plt

def metodo_rk2(f, y0, t0, h, t_final):
    """Resolve um PVI y' = f(t, y) usando Runge-Kutta de 2ª Ordem (Ponto Médio)."""
    tempos = [t0]
    y_atual = np.array(y0, dtype=float)
    valores_y = [y_atual]
    t_atual = t0
    
    num_passos = int(round((t_final - t0) / h))
    for _ in range(num_passos):
        k1 = f(t_atual, y_atual)
        k2 = f(t_atual + 0.5 * h, y_atual + 0.5 * h * k1)
        y_atual = y_atual + h * k2
        t_atual += h
        tempos.append(t_atual)
        valores_y.append(y_atual)
        
    return np.array(tempos), np.array(valores_y)

def metodo_rk4(f, y0, t0, h, t_final):
    """Resolve um PVI y' = f(t, y) usando Runge-Kutta de 4ª Ordem."""
    tempos = [t0]
    y_atual = np.array(y0, dtype=float)
    valores_y = [y_atual]
    t_atual = t0
    
    num_passos = int(round((t_final - t0) / h))
    for _ in range(num_passos):
        k1 = f(t_atual, y_atual)
        k2 = f(t_atual + 0.5 * h, y_atual + 0.5 * h * k1)
        k3 = f(t_atual + 0.5 * h, y_atual + 0.5 * h * k2)
        k4 = f(t_atual + h, y_atual + h * k3)
        y_atual = y_atual + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t_atual += h
        tempos.append(t_atual)
        valores_y.append(y_atual)
        
    return np.array(tempos), np.array(valores_y)

def executar_problema(problema):
    """
    Função principal genérica que resolve e exibe os resultados para um dado problema.
    """
    print(f"--- Resolvendo: {problema['nome']} ---")
    print(f"Parâmetros: t_final = {problema['t_final']}, h = {problema['h']}")
    
    # Resolve com ambos os métodos
    tempos_rk2, res_rk2 = metodo_rk2(problema['f'], problema['y0'], problema['t0'], problema['h'], problema['t_final'])
    tempos_rk4, res_rk4 = metodo_rk4(problema['f'], problema['y0'], problema['t0'], problema['h'], problema['t_final'])

    # Exibe o resultado final com lógica corrigida para não dar erro
    y_final_rk2 = res_rk2[-1]
    y_final_rk4 = res_rk4[-1]

    print(f"\nResultados Finais em t = {problema['t_final']}:")
    if np.isscalar(y_final_rk2): # Verifica se o resultado é um único número
        label = problema['labels'][0]
        print(f"  {label}:")
        print(f"    RK2: {y_final_rk2:.6f}")
        print(f"    RK4: {y_final_rk4:.6f}")
    else: # Se for um vetor (sistema de equações)
        for i, label in enumerate(problema['labels']):
            print(f"  {label}:")
            print(f"    RK2: {y_final_rk2[i]:.6f}")
            print(f"    RK4: {y_final_rk4[i]:.6f}")
    
    # Plota o gráfico de forma genérica
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    fig.suptitle(f"Comparação de Métodos: {problema['nome']} (h={problema['h']})")
    
    if res_rk2.ndim == 1: # Se o array de resultados tem 1 dimensão
        ax.plot(tempos_rk2, res_rk2, 'o--', label=f"RK2 - {problema['labels'][0]}", alpha=0.8)
        ax.plot(tempos_rk4, res_rk4, '-', label=f"RK4 - {problema['labels'][0]}", linewidth=2)
    else: # Se for um sistema, plota cada variável
        for i, label in enumerate(problema['labels']):
            ax.plot(tempos_rk2, res_rk2[:, i], 'o--', label=f'RK2 - {label}', alpha=0.8)
            ax.plot(tempos_rk4, res_rk4[:, i], '-', label=f'RK4 - {label}', linewidth=2)
            
    ax.set_xlabel("Tempo (t)")
    ax.set_ylabel("Valor")
    ax.grid(True)
    ax.legend()
    plt.show()

# --- ÁREA DE CONFIGURAÇÃO: DEFINA SEUS PROBLEMAS AQUI ---
if __name__ == '__main__':
    
    # IMPORTANTE: Modificar essa função para funções que variam em determinados intervalos
    # Caso a variação seja mto brusca, como nesse caso, é melhor usar RK2 pois diferentes execuções de RK4 podem divergir (mesma magnitude mas sinais opostos)
    def velocidade_variavel(t, y):
        if 1 <= t <= 5:
            return 2 * t
        elif 5 < t <= 14:
            return 5 * t**2 + 3
        else:
            # Caso o tempo saia do intervalo definido, retorna 0 ou lança um erro
            return 0

    # 2. Agora, criamos o dicionário do problema com essa função
    problema_movimento = {
        "nome": "Movimento com Velocidade Variável (Questão 6)",
        "f": velocidade_variavel,
        "y0": 4.0,         # Condição inicial: x(2) = 4
        "t0": 2.0,         # O tempo inicial é t=2
        "t_final": 9.0,    # Queremos o resultado em t=9
        "h": 0.025,        # Passo dado no enunciado
        "labels": ["Posição x(t) (m)"]
    }
    
    # Problema da Questão 20 lista (Estrutura Amortecida)
    problema_20 = {
        "nome": "Estrutura Amortecida (Questão 20 lista)",
        "f": lambda t, y: np.array([
            y[1],                       # Equação para y1' (ou x')
            -11.8 * y[0] - 5.4 * y[1]   # Equação para y2' (ou x'')
        ]),
        "y0": [0, 1],          # Condições iniciais: [x(0), ẋ(0)]
        "t0": 0.0,
        "t_final": 5.0,        # Simulamos por 5s para ver o comportamento
        "h": 0.1,              # Passo dado no enunciado
        "labels": ["Posição x(t)", "Velocidade v(t)"]
}

    
    # Problema 1: Equação única x' = x^2
    problema_x_ao_quadrado = {
        "nome": "Equação Simples (x' = x^2)",
        "f": lambda t, y: y**2,
        "y0": 1.0,
        "t0": 0.0,
        "t_final": 1.0,
        "h": 0.125,
        "labels": ["x(t)"]
    }
    
    problema_paraquedista = {
        "nome": "Velocidade de um Paraquedista (Questão 25)",
        "f": lambda t, y: (1 - (y**2)/40) * 9.81,
        "y0": 70,
        "t0": 0.0,
        "t_final": 20,
        "h": 0.1,
        "labels": ["x(t)"]
    }
    
    problema_x_do_i = {
        "nome": "Equação Simples (x' = x^2)",
        "f": lambda t, y: (110/3) - 5 * y,
        "y0": 0.0,
        "t0": 0.0,
        "t_final": 0.5,
        "h": 0.1,
        "labels": ["x(t)"]
    }
    
    # Problema 2: Sistema Linear (Questão 22)
    problema_sistema_linear = {
        "nome": "Sistema Linear (Questão 22)",
        "f": lambda t, y: np.array([
            7 * y[0] - 4 * y[1],
            -9 * y[0] + 7 * y[1]
        ]),
        "y0": [4, 1],
        "t0": 0.0,
        "t_final": 1.0,
        "h": 0.1,
        "labels": ["x(t)", "y(t)"]
    }
    
    # Problema do Circuito RLC (Questão 26)
    problema_rlc = {
        "nome": "Circuito RLC Forçado",
        "f": lambda t, y: np.array([
            y[1],                                   # Equação para y1' (q')
            9*np.sin(t) - 125*y[0] - 20*y[1]        # Equação para y2' (q'')
        ]),
        "y0": [0.2, 0],            # Condições iniciais: [q(0), q'(0)]
        "t0": 0.0,
        "t_final": 2.0,            # Objetivo é encontrar a solução no intervalo [0, 2]
        "h": 0.1,                  # Escolhemos um passo razoável
        "labels": ["Carga q(t) (C)", "Corrente q'(t) (A)"]
    }

    problema_camada_limite = {
        "nome": "Escoamento em Camada Limite (Questão 23)",
        
        # Nossa EDO de 1ª ordem. 't' no código é 'x' no problema,
        # e 'y' no código é a velocidade 'U'.
        "f": lambda t, y: -(1 + t) / (1.23 * y),
        
        # Condição inicial U(0)=1. Como é uma única equação, y0 é um número.
        "y0": 1.0,
        
        # Parâmetros da simulação
        "t0": 0.0,
        "t_final": 1.0,    # O intervalo é [0, 1]
        "h": 0.1,          # Usando um passo razoável
        
        # Rótulo para o gráfico
        "labels": ["Velocidade U(x)"]
    }
    

    # --- ESCOLHA QUAL PROBLEMA EXECUTAR AQUI ---
    # Basta atribuir o dicionário do problema desejado à variável 'problema_ativo'
    
    problema_ativo = problema_paraquedista
    # problema_ativo = problema_sistema_linear
    
    # Executa a função principal com o problema escolhido
    executar_problema(problema_ativo)