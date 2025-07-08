import numpy as np

def f(x, y):
    return ((x*y)**2) * np.sin((x**2)*y) - y

def runge_kutta_ord2(n, y0, a, b):
    """
    Resolve um problema de valor inicial com Runge-Kutta de 2ª ordem.
    
    Parâmetros:
    n  - número de passos
    y0 - valor inicial
    a  - início do intervalo
    b  - fim do intervalo
    
    Retorna:
    valor aproximado y no ponto b
    """
    h = (b - a) / n
    
    print(f"Utilizando h = {h} e n = {n} passos.")
    
    y = np.zeros(n + 1)
    y[0] = y0
    x = a

    for i in range(n):
        k1 = f(x, y[i])
        k2 = f(x + h, y[i] + h * k1)
        y[i + 1] = y[i] + (h / 2) * (k1 + k2)
        
        print(f"Resultado aproximado em x = {x + h}: {y[i + 1]:.10f}")
        
        x = x + h
    
    return y[-1]

# Exemplo de uso:
if __name__ == "__main__":
    n = 20
    y0 = 1
    a = 0
    b = 1
    
    resultado = runge_kutta_ord2(n, y0, a, b)
    print(f"Resultado em x = {b}: {resultado}")
