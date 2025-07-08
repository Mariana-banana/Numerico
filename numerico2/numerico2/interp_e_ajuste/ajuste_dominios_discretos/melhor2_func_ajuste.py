import numpy as np

def choose_best_fit(x_axis, y_axis, tol=1e-2):
    x_axis = np.array(x_axis)
    y_axis = np.array(y_axis)
    dx = np.diff(x_axis)

    # Diferenças
    dy = np.diff(y_axis)
    ddy = np.diff(dy)
    dddy = np.diff(ddy)

    # Teste para reta
    if np.allclose(dy / dx, dy[0]/dx[0], rtol=tol):
        return "reta"
    # Teste para parábola
    elif np.allclose(ddy / dx[:-1]**2, ddy[0] / dx[0]**2, rtol=tol):
        return "parábola"
    # Teste para cúbica
    elif np.allclose(dddy / dx[:-2]**3, dddy[0] / dx[0]**3, rtol=tol):
        return "cúbica"
    # Teste para exponencial
    elif np.allclose(np.diff(np.log(y_axis)) / dx, np.diff(np.log(y_axis))[0] / dx[0], rtol=tol):
        return "exponencial"
    # Teste para potência
    elif np.allclose(np.diff(np.log(y_axis)) / np.diff(np.log(x_axis)), (np.diff(np.log(y_axis)) / np.diff(np.log(x_axis)))[0], rtol=tol):
        return "potência"
    else:
        return "desconhecida"

# Exemplo
x_test = [250, 330, 412, 485, 617]
y_test = [5720, 5260, 4450, 2780, 1506]
print(choose_best_fit(x_test, y_test, tol= 10))
