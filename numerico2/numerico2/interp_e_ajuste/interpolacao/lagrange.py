import sympy as sp

def lagrange_symbolic(x_axis, y_axis):
    """
    Gera a forma simbólica dos polinômios de Lagrange e o polinômio de interpolação.

    :param x_axis: lista de valores de x
    :param y_axis: lista de valores de y correspondentes
    :return: (L_list, P) onde:
             L_list é a lista de polinômios base L_i(x),
             P é o polinômio de Lagrange completo P(x)
    """
    x = sp.Symbol('x')
    n = len(x_axis)
    L_list = []

    for i in range(n):
        xi = x_axis[i]
        li = 1
        for j in range(n):
            if i != j:
                xj = x_axis[j]
                li *= (x - xj) / (xi - xj)
        L_list.append(sp.simplify(li))

    # Polinômio de Lagrange completo
    P = sum(y_axis[i] * L_list[i] for i in range(n))
    P = sp.simplify(P)

    return L_list, P

if __name__ == '__main__':

    x_axis = [700, 710, 720, 730, 740, 780]
    y_axis = [97.71, 98.11, 98.49, 98.88, 99.26, 100.73]

    L_list, P = lagrange_symbolic(x_axis, y_axis)

    # Mostrar os polinômios L_i(x)
    for i, L in enumerate(L_list):
        print(f"L_{i}(x) = {L}")

    # Mostrar o polinômio de Lagrange completo
    print(f"\nP(x) = {P}")
