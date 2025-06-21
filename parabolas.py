import numpy as np

def ajustar_parabola(pontos):
    # Separar os pontos em X e Y
    X = np.array([p[0] for p in pontos])
    Y = np.array([p[1] for p in pontos])

    # Monta a matriz A com [x^2, x, 1]
    A = np.vstack([X**2, X, np.ones_like(X)]).T

    # Resolve o sistema normal (mínimos quadrados)
    coeficientes = np.linalg.lstsq(A, Y, rcond=None)[0]
    
    return coeficientes  # retorna a, b, c

# Exemplo com os pontos dados
# pontos = [(-3, 3), (0, 1), (2, 1), (4, 3)]
pontos = [(0, 1.5), (1, 2.5),(2, 3.5),(3,5), (4, 7.5)]

a, b, c = ajustar_parabola(pontos)

print(f"Parábola ajustada: y = {a:.6f}x² + {b:.6f}x + {c:.6f}")
