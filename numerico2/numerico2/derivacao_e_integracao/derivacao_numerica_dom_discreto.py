def derivacao(x0, y0, x1, y1):
    # Derivada de primeira ordem (central)
    d1 = (y1 - y0) / (x1 - x0)
    # Derivada de segunda ordem (central)
    d2 = (y1 - 2*y0 + y0) / ((x1 - x0)**2)
    # Derivada de terceira ordem (central)
    d3 = (y1 - 2*y0 + y0 - y0) / ((x1 - x0)**3)
    # Derivada de quarta ordem (central)
    d4 = (y1 - 4*y0 + 6*y0 - 4*y0 + y0) / ((x1 - x0)**4)

    return d1, d2, d3, d4


if __name__ == "__main__":
    # Exemplo de uso
    x0 = 0.2
    y0 = 2.415  # f(x0)
    x1 = 0.6
    y1 = 2.907  # f(x1)

    derivada_1, derivada_2, derivada_3, derivada_4 = derivacao(x0, y0, x1, y1)

    print(f"Derivada 1ª ordem: {derivada_1}")
    print(f"Derivada 2ª ordem: {derivada_2}")
    print(f"Derivada 3ª ordem: {derivada_3}")
    print(f"Derivada 4ª ordem: {derivada_4}")