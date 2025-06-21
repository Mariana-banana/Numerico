import sympy as sp

def minimos_quadrados_continuo(f_expr, base_funcs, a, b):
    """
    Aplica o método dos mínimos quadrados em domínio contínuo.

    Parâmetros:
    - f_expr: expressão simbólica da função f(x)
    - base_funcs: lista de funções base [phi_0(x), phi_1(x), ..., phi_n(x)]
    - a, b: limites de integração

    Retorna:
    - Aproximação simbólica phi(x)
    - Lista de coeficientes [c0, c1, ..., cn]
    """
    x = sp.symbols('x')
    n = len(base_funcs)
    A = sp.zeros(n, n)
    B = sp.zeros(n, 1)

    for i in range(n):
        for j in range(n):
            A[i, j] = sp.integrate(base_funcs[i] * base_funcs[j], (x, a, b))
        B[i] = sp.integrate(f_expr * base_funcs[i], (x, a, b))

    C = A.LUsolve(B)

    # Construção da função aproximada phi(x)
    phi = sum(C[i] * base_funcs[i] for i in range(n))
    
    return phi.simplify(), [c.simplify() for c in C]

if __name__ == '__main__':

    x = sp.symbols('x') # variáveis
    f = x**2            # função
    base = [1, x]       
    a = 1               # intervalo à esquerda
    b = 2               # intervalo à direita 

    phi, coeficientes = minimos_quadrados_continuo(f, base, a, b)

    print("Função aproximada phi(x):")
    print(phi)

    print("\nCoeficientes:")
    for i, c in enumerate(coeficientes):
        print(f"c{i} = {c}")
