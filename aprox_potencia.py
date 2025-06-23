import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Dados fornecidos
#v = np.array([10, 20, 30, 40, 60, 70])
#mu = np.array([0.313, 0.250, 0.215, 0.192, 0.164, 0.154])

v = np.array([700, 710, 720, 730, 740, 780])
mu = np.array([97.71, 98.11, 98.49, 98.88, 99.26, 100.73])

# Transformação logarítmica
log_v = np.log(v)
log_mu = np.log(mu)

# Regressão linear sobre os logs
coef = np.polyfit(log_v, log_mu, 1)
b = coef[0]
ln_a = coef[1]
a = np.exp(ln_a)

# Função final: mu = a * v^b
def modelo_potencia(velocidade):
    return a * velocidade**b

# Cálculo dos valores pedidos
v_calcular = [50, 120]
mu_calculado = [modelo_potencia(vi) for vi in v_calcular]

# R²
mu_pred = modelo_potencia(v)
r2 = r2_score(mu, mu_pred)

# Resultados
print("=======================================")
print("   AJUSTE POR FUNÇÃO POTÊNCIA")
print("=======================================")
print(f"Modelo encontrado: μ = {a:.6f} * v^{b:.6f}")
print(f"Coeficiente de Determinação (R²): {r2:.6f}")
print("---------------------------------------")
for vi, mui in zip(v_calcular, mu_calculado):
    print(f"Para v = {vi} km/h, o coef. de atrito estimado é μ = {mui:.6f}")
print("=======================================")

# Gráfico
v_plot = np.linspace(5, 130, 300)
mu_plot = modelo_potencia(v_plot)

plt.figure(figsize=(10, 6))
plt.scatter(v, mu, color='blue', label='Dados Originais')
plt.plot(v_plot, mu_plot, color='red', label='Ajuste Potência')
plt.scatter(v_calcular, mu_calculado, color='green', marker='*', s=150, label='Pontos Estimados')
plt.title('Ajuste de μ = a * v^b')
plt.xlabel('Velocidade (km/h)')
plt.ylabel('Coef. de Atrito (μ)')
plt.grid(True)
plt.legend()
plt.show()
