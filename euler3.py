import numpy as np

def sistema(x, z, y):
    dz = z**2 - y + np.exp(x)
    dy = z - y**2 - np.exp(x)
    return dz, dy

# Condições iniciais
x = 0
z = 0
y = 1
h = 0.1  # passo
n = 10   # até x=1

for i in range(n):
    dz, dy = sistema(x, z, y)
    z += h * dz
    y += h * dy
    x += h

print(f"z(1) ≈ {z:.4f}")
print(f"y(1) ≈ {y:.4f}")
