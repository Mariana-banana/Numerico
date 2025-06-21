import numpy as np
from numpy.polynomial.legendre import legval, leggauss, Legendre
import math

def aproximar_com_legendre(f, grau, a=-1, b=1):

    # Transformar f para o intervalo [-1, 1], se necessário
    def f_padrao(x):
        x_real = 0.5 * (b - a) * x + 0.5 * (b + a)  # transformação afim
        return f(x_real)

    # Nós e pesos de quadratura de Gauss-Legendre
    xg, wg = leggauss(grau + 1)

    # Coeficientes da expansão de Legendre
    coeficientes = []
    for n in range(grau + 1):
        Pn = Legendre.basis(n)(xg)
        # Produto interno <f, Pn>
        integrando = f_padrao(xg) * Pn
        cn = (2 * n + 1) / 2 * np.sum(wg * integrando)
        coeficientes.append(cn)

    coeficientes = np.array(coeficientes)

    # Função de aproximação: soma c_n * Pn(x)
    def aproximacao(x):
        # Mapear x para [-1,1] se estiver em [a,b]
        x_ref = 2 * (np.array(x) - a) / (b - a) - 1
        return legval(x_ref, coeficientes)

    return aproximacao, coeficientes


if __name__ == '__main__':  
    import matplotlib.pyplot as plt

    f = lambda x: np.sin(x)
    grau = 2
    a = 0
    b = math.pi

    aprox, coefs = aproximar_com_legendre(f, grau, a, b)

    print(coefs)

    x = np.linspace(a, b, 500)
    plt.plot(x, f(x), label='Função original')
    plt.plot(x, aprox(x), label='Aproximação de Legendre', linestyle='--')
    plt.legend()
    plt.title("Aproximação com Polinômios de Legendre")
    plt.grid(True)
    plt.show()