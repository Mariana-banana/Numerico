import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def spline_cubico_interpolador(x_axis, y_axis, num_pontos=100, plot=False):

    # Garantir que os vetores são arrays numpy
    x = np.array(x_axis)
    y = np.array(y_axis)

    # Checagem básica
    if len(x) != len(y):
        raise ValueError("x_axis e y_axis devem ter o mesmo tamanho")
    if not np.all(np.diff(x) > 0):
        raise ValueError("x_axis deve estar em ordem crescente")

    # Criar spline cúbico
    spline = CubicSpline(x, y, bc_type='natural')

    coefs = spline.c  # coeficientes: shape (4, n-1)
    for i in range(len(x) - 1):
        a, b, c, d = coefs[:, i]
        print(f"No intervalo [{x[i]}, {x[i+1]}]:")
        print(f"  S(x) = {a:.6f}(x - {x[i]})^3 + {b:.6f}(x - {x[i]})^2 + {c:.6f}(x - {x[i]}) + {d:.6f}")


    # Criar pontos interpolados
    x_interp = np.linspace(x[0], x[-1], num_pontos)
    y_interp = spline(x_interp)

    # Plotar, se solicitado
    if plot:
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, 'o', label='Pontos Originais')
        plt.plot(x_interp, y_interp, '-', label='Spline Cúbico')
        plt.title('Interpolação por Spline Cúbico')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

    return x_interp, y_interp, spline

if __name__ == '__main__':
    x_axis = [10, 15, 20, 25, 30 , 35]
    y_axis = [105, 172, 253, 352, 473, 619]

    spline = None

    x_interp, y_interp, spline = spline_cubico_interpolador(x_axis, y_axis, plot=True)
    
    valores_para_avaliar = x_axis + [12, 22, 31]

    for val in valores_para_avaliar:
        resultado = spline(val)
        print(f"P({val}) = {resultado:.6f}")
