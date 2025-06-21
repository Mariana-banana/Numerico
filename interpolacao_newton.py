import numpy as np

def interpolar_newton(x_data, y_data, grau, ponto_x):
    """
    Realiza a interpolação polinomial de Newton.

    Args:
        x_data (list or np.array): Lista de coordenadas x conhecidas.
        y_data (list or np.array): Lista de coordenadas y conhecidas.
        grau (int): O grau do polinômio a ser usado (n).
        ponto_x (float): O ponto x no qual se deseja interpolar o valor y.

    Returns:
        float: O valor y interpolado.
    """
    x_data = np.array(x_data, dtype=float)
    y_data = np.array(y_data, dtype=float)
    
    num_pontos = grau + 1

    # --- Passo 1: Encontrar os 'num_pontos' mais próximos de 'ponto_x' ---
    # Calcula a distância de cada ponto em x_data até o ponto_x
    distancias = np.abs(x_data - ponto_x)
    
    # Pega os índices que ordenariam o array de distâncias
    indices_ordenados = np.argsort(distancias)
    
    # Seleciona os índices dos 'num_pontos' mais próximos
    indices_proximos = np.sort(indices_ordenados[:num_pontos])
    
    x_local = x_data[indices_proximos]
    y_local = y_data[indices_proximos]

    # --- Passo 2: Calcular a tabela de diferenças divididas ---
    tabela = np.zeros([num_pontos, num_pontos])
    tabela[:, 0] = y_local  # A primeira coluna é y

    for j in range(1, num_pontos):
        for i in range(j, num_pontos):
            numerador = tabela[i, j - 1] - tabela[i - 1, j - 1]
            denominador = x_local[i] - x_local[i - j]
            tabela[i, j] = numerador / denominador

    # Os coeficientes do polinômio de Newton são a diagonal da tabela
    coeficientes = np.diag(tabela)

    # --- Passo 3: Avaliar o polinômio no ponto_x ---
    resultado = coeficientes[0]
    termo_produto = 1.0

    for i in range(1, num_pontos):
        termo_produto *= (ponto_x - x_local[i - 1])
        resultado += coeficientes[i] * termo_produto

    return resultado

# --- DADOS DO PROBLEMA DA MOLA ---
# Eixo X: Alongamento (mm)
x_mola = [10, 15, 20, 25, 30, 35]
# Eixo Y: Carga (kgf)
p_mola = [105, 172, 253, 352, 473, 619]

# Pontos que queremos encontrar
pontos_a_encontrar = [12, 22, 31]
# Grau do polinômio especificado no problema
grau_do_polinomio = 3

print("--- Resolução do Problema da Mola ---")
for ponto in pontos_a_encontrar:
    carga_calculada = interpolar_newton(x_mola, p_mola, grau_do_polinomio, ponto)
    # Imprime com 6 casas decimais, conforme solicitado anteriormente
    print(f"Para um alongamento de {ponto} mm, a carga é de {carga_calculada:.6f} kgf")