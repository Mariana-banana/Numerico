import sympy as sp

def diferencas_divididas(x, y):
    """
    Calcula a tabela da diferença dividida de Newton com x arbitrário.
    
    Parâmetros:
    x: lista de valores x (deve ter o mesmo tamanho que y)
    y: lista de valores f(x)

    Retorna:
    - A tabela de diferenças divididas
    - O polinômio interpolador como string simbólica
    """
    n = len(x)
    
    # Inicializa a tabela com zeros
    tabela = [[0 for _ in range(n)] for _ in range(n)]
    
    # Primeira coluna é apenas y
    for i in range(n):
        tabela[i][0] = y[i]

    # Preenche a tabela de diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            numerador = tabela[i + 1][j - 1] - tabela[i][j - 1]
            denominador = x[i + j] - x[i]
            tabela[i][j] = numerador / denominador

    # Construção do polinômio como string
    termos = []
    for j in range(n):
        coef = tabela[0][j]
        if coef == 0:
            continue
        termo = f"{coef:.6f}"
        for k in range(j):
            termo += f"*(x - {x[k]:.6f})"
        termos.append(termo)

    polinomio = " + ".join(termos)

    return tabela, polinomio

if __name__ == '__main__':
    x_axis = ([10, 20, 30, 40, 60, 70])
    y_axis = ([0.313, 0.250, 0.215, 0.192, 0.164, 0.154])

    valores_para_avaliar = x_axis + [50, 120]

    tabela, polinomio = diferencas_divididas(x_axis, y_axis)

    print("Tabela de diferenças divididas:")
    for linha in tabela:
        print(["{:.6f}".format(val) if val != 0 else "0" for val in linha])

    print("\nPolinômio interpolador de Newton:")
    print("P(x) =", polinomio)
    print("\n-----------------\nP(x) =", sp.simplify(polinomio), "\n-----------------\n")

    for val in valores_para_avaliar:
        resultado = eval(polinomio.replace("x", str(val)))
        print(f"P({val}) = {resultado:.6f}")
