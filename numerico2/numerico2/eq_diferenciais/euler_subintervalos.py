import numpy as np
import matplotlib.pyplot as plt

def euler_num_subintervalos(f, u0, ti, tf, N, plot=True):
    """
    Método de Euler para resolver y'(t) = f(t, y), com N subintervalos.

    Parâmetros:
    -----------
    f : função(t, y)
        Função que define a EDO y' = f(t, y).
    u0 : float
        Condição inicial y(ti) = u0.
    ti : float
        Tempo inicial.
    tf : float
        Tempo final.
    N : int
        Número de subintervalos.
    plot : bool
        Se True, plota a solução.

    Retorno:
    --------
    t : ndarray
        Vetor com os tempos.
    u : ndarray
        Vetor com a solução numérica y(t).
    """
    h = (tf - ti) / N
    t = np.linspace(ti, tf, N+1)
    u = np.zeros(N+1)
    u[0] = u0

    # Itera pelo método de Euler
    for n in range(N):
        u[n+1] = u[n] + h * f(t[n], u[n])
        print(f"Iteração {n+1}: t = {t[n+1]:.4f}, u = {u[n+1]:.4f}")
        

    # Plota a solução
    if plot:
        plt.plot(t, u, 'b.-')
        plt.xlabel('t')
        plt.ylabel('y(t)')
        plt.grid(True)
        plt.title('Solução EDO (Método de Euler)')
        plt.show()

    return t, u

# Exemplo de uso:
# EDO: y' = sin(y), y(0) = 1, t ∈ [0, 2], N=100
# f = lambda t, y: np.sin(y)
# t, u = euler_num_subintervalos(f, u0=1.0, ti=0.0, tf=2.0, N=100)

f = lambda t, y: np.sin(y)
t, u = euler_num_subintervalos(f, u0=1.0, ti=0.0, tf=2.0, N=100)
