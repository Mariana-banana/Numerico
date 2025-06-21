# Dados fornecidos
x = [0.2, 0.4, 0.6, 0.8, 1.0]
f = [2.415, 2.637, 2.907, 3.193, 3.381]
h = 0.2

# Índices:
# f(x0) = f[1] = f(0.4)
# f(x0+h) = f[2] = f(0.6)
# f(x0-h) = f[0] = f(0.2)
# f(x0+2h) = f[3] = f(0.8)
# f(x0-2h) = N/A (não existe! usamos aproximação inferior para f''' nesse caso)

# 1ª derivada centrada
f1 = (f[2] - f[0]) / (2 * h)

# 2ª derivada centrada
f2 = (f[2] - 2*f[1] + f[0]) / (h ** 2)

# 3ª derivada centrada (usando os pontos ao redor)
f3 = (f[3] - 2*f[2] + 2*f[0] - f[1-1]) / (2 * h ** 3)  # f[-1] == f[0] (já está presente)

print("Aproximações em x = 0.4:")
print(f"f'(0.4)   ≈ {f1:.6f}")
print(f"f''(0.4)  ≈ {f2:.6f}")
print(f"f'''(0.4) ≈ {f3:.6f}")
