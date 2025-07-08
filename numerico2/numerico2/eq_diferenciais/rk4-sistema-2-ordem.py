import numpy as np

m = 5
k = 60
c = 0.6
c = 0.6*m + 0.4*k

# Sistema da EDO
# q1' = q2
# q2' = 9*sin(t) - 20*q2 - 125*q1
def f(t, Q):
    q1, q2 = Q
    dq1dt = q2
    dq2dt = 9*np.sin(t) - 20*q2 - 125*q1
    return np.array([dq1dt, dq2dt])

# Método de Runge-Kutta de 4ª ordem para sistemas
def rungeKuttaSistema(t0, Q0, t_final, h):
    n = int((t_final - t0)/h)
    Q = np.array(Q0, dtype=float)
    t = t0
    for i in range(n):
        k1 = h * f(t, Q)
        k2 = h * f(t + 0.5*h, Q + 0.5*k1)
        k3 = h * f(t + 0.5*h, Q + 0.5*k2)
        k4 = h * f(t + h, Q + k3)
        Q = Q + (k1 + 2*k2 + 2*k3 + k4)/6.0
        t = t + h
        
        print(f"Iteração {i+1}: t = {t:.2f}, q1 = {Q[0]:.6f}, q2 = {Q[1]:.6f}")
        
    return Q

# Condições iniciais
t0 = 0.0
Q0 = [0.0, 1]  # q(0) e q'(0)
t_final = 2
h = 0.1

# Chamada do método
solucao = rungeKuttaSistema(t0, Q0, t_final, h)
print(f"Solução numérica em t={t_final}: q={solucao[0]:.6f}, q'={solucao[1]:.6f}")
