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
        try:
            return np.e**(-x**2)
        except ZeroDivisionError:
            return 0

    # Intervalo e número de subintervalos
    a = 0
    b = 1
    n = 22  # Número de subintervalos

    
    resultado1 = simpson(f, a, b, n)
    print(f"Integral aproximada de f(x) no intervalo [{a}, {b}]: {resultado1}")

    resultado2 = simpson(f, a, b, n-1)
    print(f"Integral aproximada de f(x) no intervalo [{a}, {b}]: {resultado2}")

    print(f"{abs(resultado1 - resultado2)}")