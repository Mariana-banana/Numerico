import numpy as np

def simpson(f, a, b, n):
    h = (b - a)/(2*n)
    x = np.linspace(a, b, n+1)
    soma = 0
    
    print(f"Utilizando h = {h} e n = {n} subintervalos.")
    
    for i in range(n):
        x1 = x[i]
        x3 = x[i+1]
        x2 = (x1+x3)/2
        
        soma += (f(x1) + 4*f(x2) + f(x3))*(h/3)
    
    return soma
    
    
if __name__ == "__main__":
    def f(x):
        return 1/(1+x**4)

    # Intervalo e número de subintervalos
    a = 0
    b = 1
    n = 4  # Número de subintervalos

    # Cálculo da integral usando o método de Simpson
    resultado = simpson(f, a, b, n)

    print(f"Integral aproximada de f(x) no intervalo [{a}, {b}]: {resultado}")
    