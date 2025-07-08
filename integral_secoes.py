import numpy as np
import scipy.integrate as sci
import sympy as sp
import matplotlib.pyplot as plt

# --- Suas funções de Interpolação (estão corretas) ---
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

# --- RESOLVENDO O PROBLEMA DO VOLUME ---
if __name__ == '__main__':
    
    # Dados da seção transversal do sólido
    x_tabela = np.array([0, 5, 10, 15, 20, 25, 30])
    y_tabela = np.array([0, 3, 4, 4.6, 4, 3, 0])
    comprimento_solido = 50.0 # em metros

    # --- PASSO 1: Criar a função que descreve a curva da seção ---
    # Esta função é o próprio polinômio interpolador P(x), que representa y(x).
    def funcao_da_secao(x):
        return newton_interp(x_tabela, y_tabela, x)

    # --- PASSO 2: Calcular a área da seção transversal ---
    # Integramos a função da seção P(x) nos limites corretos [0, 30].
    limite_inferior = x_tabela[0]  # 0
    limite_superior = x_tabela[-1] # 30
    
    area_da_secao, erro_estimado = sci.quad(funcao_da_secao, limite_inferior, limite_superior)

    # --- PASSO 3: Calcular o volume do sólido ---
    # Volume = Área da Seção * Comprimento
    volume_total = area_da_secao * comprimento_solido
    
    # --- PASSO 4: Exibir os resultados ---
    print("\n--- Cálculo do Volume do Sólido ---")
    print(f"Dados da seção: x = {x_tabela}, y = {y_tabela}")
    print(f"Comprimento do sólido: {comprimento_solido} m")
    print("-" * 35)
    print(f"1. A área da seção transversal (∫ y(x) dx de {limite_inferior} a {limite_superior}) é:")
    print(f"   Área ≈ {area_da_secao:.4f} m²")
    print("\n2. O volume total (Área × Comprimento) é:")
    print(f"   Volume ≈ {volume_total:.4f} m³")
    print("-" * 35)

    # Opcional: Visualizar a seção transversal para verificação
    x_plot = np.linspace(limite_inferior, limite_superior, 200)
    y_plot = funcao_da_secao(x_plot)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x_plot, y_plot, label='Curva da Seção (Polinômio Interpolador)')
    plt.fill_between(x_plot, y_plot, alpha=0.3, label=f'Área da Seção ≈ {area_da_secao:.2f} m²')
    plt.scatter(x_tabela, y_tabela, color='red', zorder=5, label='Pontos Originais')
    plt.title("Seção Transversal do Sólido")
    plt.xlabel("x (metros)")
    plt.ylabel("y (metros)")
    plt.grid(True)
    plt.legend()
    plt.show()