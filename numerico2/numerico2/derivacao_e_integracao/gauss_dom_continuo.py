import scipy.integrate as sci
import numpy as np

def gauss(f, a, b, n):
    return sci.fixed_quad(f, a, b, n=n)[0]

if __name__ == '__main__':
    def f(x):
        return (x**3)/(np.pow(np.e, x) - 1)

    # Intervalo
    a = 0
    b = 2
    n = 3

    # Cálculo da integral usando o método de Gauss
    resultado = gauss(f, a, b, n)

    print(f"Integral aproximada de f(x) no intervalo [{a}, {b}]: {resultado}")