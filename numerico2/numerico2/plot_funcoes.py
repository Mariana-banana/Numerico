import numpy as np
import matplotlib.pyplot as plt

def plot_funcoes_e_pontos(funcoes=None, pontos=None, intervalo=(-10, 10), num_amostras=500):
    """
    Plota um número arbitrário de funções e pontos num mesmo gráfico,
    e indica qual função melhor se ajusta aos pontos com base no erro quadrático médio.

    Parâmetros:
    -----------
    funcoes : list[callable]
        Lista com funções Python que aceitam um número (ex: lambda x: x**2).
    pontos : list[tuple]
        Lista de pontos (x, y) que serão plotados.
    intervalo : tuple
        Intervalo para o eixo x (mín, máx).
    num_amostras : int
        Quantidade de amostras para traçar as funções.

    Retorna:
    --------
    índice da melhor função e seu erro médio quadrático.
    """
    if funcoes is None:
        funcoes = []
    if pontos is None or len(pontos) == 0:
        pontos = []
        melhor_funcao = None
        print("Nenhum ponto fornecido para ajuste.")
    else:
        x_pontos, y_pontos = zip(*pontos)

    # Gerar eixo x para traçar as curvas
    x = np.linspace(intervalo[0], intervalo[1], num_amostras)

    # Plotar cada função
    for f in funcoes:
        y = f(x)
        nome = f.__name__ if hasattr(f, "__name__") else "função"
        plt.plot(x, y, label=nome)

    # Plotar os pontos
    if pontos:
        plt.scatter(x_pontos, y_pontos, color='red', zorder=5, label='pontos')

    # Calcular erro médio quadrático entre cada função e os pontos
    melhor_funcao = None
    menor_erro = float('inf')
    if pontos and funcoes:
        for i, f in enumerate(funcoes):
            # avaliar a função nos x dos pontos
            y_pred = np.array([f(xi) for xi in x_pontos])
            erro_medio = np.mean((y_pred - np.array(y_pontos))**2)
            
            print(f"{funcoes[i].__name__}: Erro médio quadrático = {erro_medio:.4f}" if melhor_funcao is not None else f"{f.__name__}: Erro médio quadrático = {erro_medio}")
            
            if erro_medio < menor_erro:
                menor_erro = erro_medio
                melhor_funcao = i

    # Configurações do gráfico
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.grid(True)
    plt.title('Funções e Pontos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    if melhor_funcao is not None:
        nome_melhor = funcoes[melhor_funcao].__name__ if hasattr(funcoes[melhor_funcao], "__name__") else f"função {melhor_funcao}"
        print(f"A função que melhor se ajusta aos pontos é '{nome_melhor}' com erro quadrático médio = {menor_erro}.")
        return melhor_funcao, menor_erro
    return None, None

def min_x(pontos):
    return min(x for x, _ in pontos) if pontos else None

def max_x(pontos):
    return max(x for x, _ in pontos) if pontos else None


def f(x):
    return -3.525*x**2 -4.205*x + 0.495

def g(x):
    return 3.525*x**2 -4.345*x + 0.549

def h(x):
    return 3.525*x**2 -4.205*x + 0.495

def i(x):
    return 3.51*x**2  -4*x + 0.5

def j(x):
    return 3.4999999999999987*x**2 -4.099999999999997*x + 0.3999999999999996

x_axis = [0,1,2,3] 
y_axis = [0.2,1,5,20]
 
pontos = [(x_axis[i], y_axis[i]) for i in range(len(x_axis))]
print(pontos)
funcoes=[f, g, h, i, j]
min_intervalo = min_x(pontos) - 1
max_intervalo = max_x(pontos) + 1

plot_funcoes_e_pontos(
    funcoes=funcoes,
    pontos=pontos,
    intervalo=(min_intervalo, max_intervalo)
)
