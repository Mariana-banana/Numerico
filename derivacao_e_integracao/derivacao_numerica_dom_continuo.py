import math

def derivadas(f, x, h=1e-5):
    """
    Calcula a derivada 1ª e 2ª de f(x) no ponto x usando diferenças finitas centrais.

    Parâmetros:
    f : função que recebe um float e retorna um float
    x : ponto onde derivar
    h : passo para a aproximação numérica

    Retorna:
    (derivada_1, derivada_2, derivada_3, derivada_4) como uma tupla
    """
    # Derivada de primeira ordem (central)
    d1 = (f(x+h) - f(x-h)) / (2*h)
    # Derivada de segunda ordem (central)
    d2 = (f(x+h) - 2*f(x) + f(x-h)) / (h**2)
    # Derivada de terceira ordem (central)
    d3 = (f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h)) / (2*h**3)
    # Derivada de quarta ordem (central)
    d4 = (f(x+2*h) - 4*f(x+h) + 6*f(x) - 4*f(x-h) + f(x-2*h)) / (h**4)
    
    return d1, d2, d3, d4

# ========================
# EXEMPLO DE USO
# ========================

if __name__ == "__main__":

    # Testando com f(x) = x^3 - 2x + 1
    funcao = lambda x: math.cos(x*2)

    ponto = 0.7
    h = 0.001
    derivada_1, derivada_2, derivada_3, derivada_4 = derivadas(funcao, ponto, h)

    print(f"Derivada 1ª ordem em x={ponto}: {derivada_1}")
    print(f"Derivada 2ª ordem em x={ponto}: {derivada_2}")
    print(f"Derivada 3ª ordem em x={ponto}: {derivada_3}")
    print(f"Derivada 4ª ordem em x={ponto}: {derivada_4}")
