import scipy.integrate as sci
import numpy as np

def gauss(f, a, b, n):
    return sci.quad(f, a, b)[0]

if __name__ == '__main__':
    def f(x):
        #return (x**3)/(np.pow(np.e, x) - 1)
        return np.exp(-4*x)

    # Intervalo
    a = 2
    b = 8
    n = 2

    # Cálculo da integral usando o método de Gauss
    resultado = gauss(f, a, b, n)

    print(f"Integral aproximada de f(x) no intervalo [{a}, {b}]: {resultado}")