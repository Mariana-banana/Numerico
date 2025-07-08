import numpy as np

def f(x, z, y):
    return z**2 - y + np.exp(x)

def g(x, z, y):
    return z - y**2 - np.exp(x)

# Condições iniciais
x0 = 0
z0 = 0
y0 = 1
h = 0.1
n = int((1 - x0) / h)

# -----------------------
# MÉTODO RK2
# -----------------------
x, z, y = x0, z0, y0
for i in range(n):
    # k1
    k1z = f(x, z, y)
    k1y = g(x, z, y)
    
    # k2
    k2z = f(x + h, z + h * k1z, y + h * k1y)
    k2y = g(x + h, z + h * k1z, y + h * k1y)
    
    # Atualiza
    z += (h / 2) * (k1z + k2z)
    y += (h / 2) * (k1y + k2y)
    x += h

print(f"--- RK2 ---\nz(1) ≈ {z:.4f}\ny(1) ≈ {y:.4f}")

# -----------------------
# MÉTODO RK4
# -----------------------
x, z, y = x0, z0, y0
for i in range(n):
    # k1
    k1z = f(x, z, y)
    k1y = g(x, z, y)
    
    # k2
    k2z = f(x + h/2, z + h/2 * k1z, y + h/2 * k1y)
    k2y = g(x + h/2, z + h/2 * k1z, y + h/2 * k1y)
    
    # k3
    k3z = f(x + h/2, z + h/2 * k2z, y + h/2 * k2y)
    k3y = g(x + h/2, z + h/2 * k2z, y + h/2 * k2y)
    
    # k4
    k4z = f(x + h, z + h * k3z, y + h * k3y)
    k4y = g(x + h, z + h * k3z, y + h * k3y)
    
    # Atualiza
    z += (h / 6) * (k1z + 2*k2z + 2*k3z + k4z)
    y += (h / 6) * (k1y + 2*k2y + 2*k3y + k4y)
    x += h

print(f"\n--- RK4 ---\nz(1) ≈ {z:.4f}\ny(1) ≈ {y:.4f}")
