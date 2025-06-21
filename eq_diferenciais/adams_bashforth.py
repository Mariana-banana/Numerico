from runge_kutta4 import rungeKutta

def adams_bashforth_4(y_n, h, f_vals):
    """
    Aplica o método de Adams-Bashforth de quarta ordem.
    
    Parâmetros:
    - y_n: valor atual de y (y_n)
    - h: passo
    - f_vals: lista ou tupla com os 4 valores anteriores de f: [f_n, f_{n-1}, f_{n-2}, f_{n-3}]
    
    Retorna:
    - y_{n+1}: próxima aproximação de y
    """
    if len(f_vals) != 4:
        raise ValueError("f_vals deve conter exatamente 4 valores: [f_n, f_{n-1}, f_{n-2}, f_{n-3}]")

    f_n3, f_n2, f_n1, f_n = f_vals

    y_next = y_n + ((h / 24) * ((55 * f_n) - (59 * f_n1) + (37 * f_n2) - (9 * f_n3)))

    return y_next

def dydx(x, y):
	return 1 - x + 4*y

if __name__ == '__main__':

    # Driver method
    x0 = 0
    y = 1
    h = 0.1
    x = 0.4
    n = 4
    
    res = rungeKutta(x0, y, x, h, n, dydx)
    for i, y in enumerate(res):
        print(f"Iteração {i}: y = {y}")

    res2 = adams_bashforth_4(res[-1], h, res)

    print(f"Iteração {len(res)} por Adam Bashforth: {res2}")