import numpy as np
import matplotlib.pyplot as plt

def calcular_area_poligono(x_coords, y_coords):
    """
    Calcula a área de um polígono usando a Fórmula do Laço (Shoelace Formula).
    As coordenadas dos vértices devem ser fornecidas em ordem.
    """
    # Garante que os inputs sejam arrays numpy
    x = np.array(x_coords)
    y = np.array(y_coords)
    
    # A mágica da Fórmula do Laço com numpy:
    # np.roll(y, -1) desloca o array y uma posição para a "esquerda",
    # fazendo com que x[i] seja multiplicado por y[i+1] de forma eficiente.
    soma1 = np.sum(x * np.roll(y, -1))
    soma2 = np.sum(y * np.roll(x, -1))
    
    # A área é a metade do valor absoluto da diferença
    area = 0.5 * np.abs(soma1 - soma2)
    
    return area

# --- DADOS DO PROBLEMA ---

# Coordenadas (x, y) extraídas dos dados fornecidos
pontos_x = [-712.78, 202.86, 705.75, 732.25, -702.21]
pontos_y = [795.71, 801.42, 349.95, -691.65, -575.54]

nomes_pontos = ['A', 'B', 'C', 'D', 'E']

# --- CÁLCULO E RESULTADO ---

area_terreno = calcular_area_poligono(pontos_x, pontos_y)

print("--- Cálculo da Área do Terreno ABCDE ---")
print("Coordenadas (x, y) utilizadas:")
for i in range(len(nomes_pontos)):
    print(f"  {nomes_pontos[i]}: ({pontos_x[i]}, {pontos_y[i]})")

print("\nUsando a Fórmula do Laço (Shoelace Formula)...")
print(f"\nA área do terreno é de aproximadamente: {area_terreno:.2f} metros quadrados.")

# --- VISUALIZAÇÃO DO TERRENO (OPCIONAL) ---

# Para fechar o polígono, adicionamos o primeiro ponto ao final da lista de plotagem
x_plot = pontos_x + [pontos_x[0]]
y_plot = pontos_y + [pontos_y[0]]

plt.figure(figsize=(10, 8))
plt.plot(x_plot, y_plot, marker='o', linestyle='-', label='Contorno do Terreno')
plt.fill(x_plot, y_plot, alpha=0.2, label=f'Área ≈ {area_terreno:,.2f} m²'.replace(',', '.'))

# Adiciona os nomes dos pontos no gráfico
for i, nome in enumerate(nomes_pontos):
    plt.text(pontos_x[i], pontos_y[i] + 10, f'{nome} ({pontos_x[i]}, {pontos_y[i]})')

plt.title("Visualização do Terreno ABCDE")
plt.xlabel("Coordenada X (metros)")
plt.ylabel("Coordenada Y (metros)")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box') # Garante a proporção correta dos eixos
plt.legend()
plt.show()