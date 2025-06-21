import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# ===================================================================
#                    ÁREA DE CONFIGURAÇÃO
# ===================================================================
# 1. Insira os dados do seu problema
# x_data = np.array([250, 330, 412, 485, 617])
# y_data = np.array([5720, 5260, 4450, 2780, 1506])

x_data = np.array([10, 20, 30, 40, 60, 70])
y_data = np.array([0.313, 0.25, 0.215, 0.192, 0.164, 0.154])

# 2. Escolha o grau do polinômio
grau_do_polinomio = 3

# 3. (NOVO) Coloque aqui os valores de X que você quer calcular.
#    Deixe a lista vazia [] se não quiser calcular nenhum ponto.
pontos_para_calcular = [50, 120]
# ===================================================================


# --- 1. Cálculo da Regressão ---
coeficientes = np.polyfit(x_data, y_data, grau_do_polinomio)
polinomio = np.poly1d(coeficientes)
y_pred = polinomio(x_data)


# --- 2. Cálculo do Coeficiente R² ---
r2 = r2_score(y_data, y_pred)


# --- 3. Apresentação dos Resultados ---
print("==============================================")
print(f"  REGRESSÃO POLINOMIAL DE GRAU {grau_do_polinomio}")
print("==============================================")
print("\nFórmula da Função Encontrada:")
print(np.round(polinomio, 6)) # Arredonda para 6 casas decimais
print("\n----------------------------------------------")
print(f"Coeficiente de Determinação (R²): {r2:.6f}")
if r2 > 0.98:
    print("-> Análise: O ajuste é EXCELENTE.")
else:
    print("-> Análise: O ajuste pode não ser o ideal.")
print("==============================================")


# --- 4. (NOVO) CÁLCULO DE PONTOS ESPECÍFICOS ---
if pontos_para_calcular:
    print("\n  CÁLCULO DE PONTOS ESPECÍFICOS")
    print("----------------------------------------------")
    valores_calculados_y = []
    for ponto_x in pontos_para_calcular:
        ponto_y = polinomio(ponto_x)
        valores_calculados_y.append(ponto_y)
        print(f"-> Para x = {ponto_x}, o resultado é y = {ponto_y:.6f}")
    print("==============================================")


# --- 5. Geração do Gráfico ---
plt.figure(figsize=(10, 6))
# Plota os dados originais
plt.scatter(x_data, y_data, color='blue', label='Dados Originais', zorder=5)

# Plota a curva da regressão
x_grafico = np.linspace(x_data.min() - 20, x_data.max() + 120, 400) # Extendi o eixo para ver a extrapolação
y_grafico = polinomio(x_grafico)
plt.plot(x_grafico, y_grafico, color='red', label=f'Ajuste (Grau {grau_do_polinomio})')

# (NOVO) Plota os pontos calculados no gráfico, se houver
if pontos_para_calcular:
    plt.scatter(pontos_para_calcular, valores_calculados_y, 
                color='green', marker='*', s=150, label='Pontos Calculados', zorder=6)

plt.title('Regressão Polinomial')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True)
plt.show()