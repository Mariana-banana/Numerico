import numpy as np

# Parâmetros
m = 5.0
k = 60.0
c = 0.6*m + 0.4*k  # c = 0.6m + 0.4k

# Sistema: q1' = q2, q2' = (q1 - c q2 - k q1)/m = (1-k)q1/m - (c/m) q2
def f(t, Q):
    q1, q2 = Q
    dq1dt = q2
    dq2dt = (q1 - c*q2 - k*q1)/m
    return np.array([dq1dt, dq2dt])

# Método de Runge-Kutta 4ª ordem
def rungeKuttaSistema(t0, Q0, t_final, h):
    n = int((t_final - t0)/h)
    Q = np.array(Q0, dtype=float)
    t = t0
    resultados = []
    for i in range(n+1):
        resultados.append([t, Q[0], Q[1]])
        k1 = h * f(t, Q)
        k2 = h * f(t + 0.5*h, Q + 0.5*k1)
        k3 = h * f(t + 0.5*h, Q + 0.5*k2)
        k4 = h * f(t + h, Q + k3)
        Q = Q + (k1 + 2*k2 + 2*k3 + k4)/6.0

        print(f"Iteração {i+1}: t = {t}, q1 = {Q[0]:.6f}, q2 = {Q[1]:.6f}")

        t = t + h
    return np.array(resultados)

# Condições iniciais
t0 = 0.0
Q0 = [0.0, 1.0]  # x(0) = 0, x'(0) = 1
t_final = 0.26
h = 0.0001

# Calcular
resultados = rungeKuttaSistema(t0, Q0, t_final, h)

# Mostrar o último ponto
t_final_calc, x_final, xdot_final = resultados[-1]
print(f"Solução numérica em t={t_final_calc}: x={x_final:.6f}, x'={xdot_final:.6f}")

# (opcional) Plotar a solução
import matplotlib.pyplot as plt

plt.plot(resultados[:,0], resultados[:,1], label='x(t)')
plt.plot(resultados[:,0], resultados[:,2], label="x'(t)")
plt.title('Solução numérica da EDO')
plt.xlabel('t')
plt.ylabel('Valores')
plt.legend()
plt.grid(True)
plt.show()
