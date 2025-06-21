import numpy as np

def ajustar_exponencial(pontos):
    # Extrai x e y dos pontos
    X = np.array([p[0] for p in pontos])
    Y = np.array([p[1] for p in pontos])

    # Aplica log em Y (atenção: y deve ser > 0)
    logY = np.log(Y)

    # Monta matriz para ajuste linear: [x, 1]
    A = np.vstack([X, np.ones_like(X)]).T

    # Resolve por mínimos quadrados
    b, log_a = np.linalg.lstsq(A, logY, rcond=None)[0]

    # Converte de volta para a
    a = np.exp(log_a)

    return a, b

# Exemplo com os pontos fornecidos
pontos = [(0, 1.5), (1, 2.5), (2, 3.5), (3, 5), (4, 7.5)]
a, b = ajustar_exponencial(pontos)

print(f"Função ajustada: y = {a:.6f} * e^({b:.6f}x)")
