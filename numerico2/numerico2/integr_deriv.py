import sympy as sp

# =======================
# Configurações
# =======================
x = sp.symbols('x')
func = (sp.E**x)/(sp.sqrt(sp.E-x))      # Função f(x)
operacao = 'i'         # 'd' para derivar, 'i' para integrar
ordem = 1              # ordem da derivada ou da integral

# Para derivada:
ponto_avaliar = sp.pi/2  # ponto onde a derivada será avaliada

# Para integral definida:
a = 0               # limite inferior
b = 2              # limite superior

# =======================
# Cálculo simbólico
# =======================
expr = func
if operacao == 'd':
    for _ in range(ordem):
        expr = sp.diff(expr, x)
    valor = expr.evalf(subs={x: ponto_avaliar})
    print(f"{ordem}-ésima derivada de f(x) = {expr}")
    print(f"O valor da derivada em x={ponto_avaliar} é {valor}")

elif operacao == 'i':
    for _ in range(ordem):
        expr = sp.integrate(expr, x)
    valor = sp.integrate(func, (x, a, b)) if ordem == 1 else sp.integrate(expr, (x, a, b))
    print(f"{ordem}-ésima integral definida de f(x) de {a} até {b} é {valor.evalf()}")
    print(f"(Expressão simbólica da {ordem}-ésima integral: {expr})")

else:
    raise ValueError("Operação inválida. Use 'd' para derivar ou 'i' para integrar.")
