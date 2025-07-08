import numpy as np
import matplotlib.pyplot as plt

# Exemplo de questão:
# Seja u'=11-t^2 com u(2)=1. Aproxime u(4) usando h=0.01 e o método de Euler.
# Analisando
# u(2*) = 1**:
# No código vira u(1) = 1** e t(1) = 2 (índice do u(x) na questão)
# aproxime u(4***) -> T = 4***
# chama euler(0.01) no painel do scilab, o último é o resultado

# EDO: u'(t) = sin(u)
def f(t, u):
    return np.sin(u)

def euler(h, u0, ti, tf):
    # Calcula N e ajusta h, igual ao Scilab
    if h < 1:
        N = int((tf - ti) / h)
    else:
        N = int(h)
        h = (tf - ti) / N

    # Inicializa vetores para armazenar solução
    t = np.zeros(N+1)
    u = np.zeros(N+1)
    t[0] = ti
    u[0] = u0

    # Método de Euler
    for n in range(N):
        t[n+1] = t[n] + h
        u[n+1] = u[n] + h * f(t[n], u[n])

    ultimo = u[-1]

    # Plota a solução
    plt.plot(t, u, 'b.-')
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.grid(True)
    plt.title('Solução EDO (Método de Euler)')
    plt.show()

    return ultimo, t, u

# Exemplo de uso
ultimo, t, u = euler(h=0.1, u0=1.0, ti=0.0, tf=10.0)
print("Último valor:", ultimo)


# Detalhes:

# ordem de precisao: depende do erro do termo anterior, e é proporcional ao valor de h  -  O(h³): ordem 2
# erro de truncamento local (ETL): em uma iteração, é proporcional a h²/2*|u''|  -  O(h²): ordem 1
# erro de truncamento global: depois de fazer n iterações, proporcional a Th/2|u''|  -  O(h)


# CONVERGÊNCIA: un tende à solução do problema -> o método de Euler é convergente

# CONSISTÊNCIA: se lim(ETL/h) = 0 quando h tende a 0, então o método é consistente

# ESTABILIDADE: |1 + hλ| < 1
# Domínio de estabilidade de Euler: conjunto de todos os z tal que |1+z| < 1
# z = hλ

# Teorema: um método número consistente é convergente sss ele é estável

# metodo de euler implicito: un+1 = un + h*f(tn+1,un+1)
# necessário utilizar junto método de Newton e da bissecção
# vantagem: esse método é incondicionalmente estável: sempre estável independente do valor de h

# método trapezoidal também é implícito: un+1 = un + h/2 * (f(tn,un) + f(tn+1, un+1))
# vantagens: é incondicinalmente estável e o erro é de ordem 2
