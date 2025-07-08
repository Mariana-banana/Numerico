import numpy as np

def interpolar_polinomial(x, y, grau, novos_x):
    """
    Interpola um polinômio de grau especificado para os dados (x, y)
    e retorna os valores interpolados para novos_x.

    Parâmetros:
    -----------
    x : array-like
        Valores conhecidos da variável independente.
    y : array-like
        Valores conhecidos da variável dependente.
    grau : int
        Grau do polinômio para interpolação.
    novos_x : array-like
        Novos valores da variável independente para calcular os interpolados.

    Retorna:
    --------
    novos_y : numpy.ndarray
        Valores interpolados correspondentes a novos_x.
    """
    coef = np.polyfit(x, y, grau)
    poly = np.poly1d(coef)
    novos_y = poly(novos_x)
    return novos_y


if __name__ == '__main__':
    # Teste com dados de exemplo
    x_axis = [10, 20, 30, 40, 60, 70]
    y_axis = [0.313, 0.250, 0.215, 0.192, 0.164, 0.154]

    grau = 10

    valores_para_avaliar = x_axis + [50, 120]
    res = interpolar_polinomial(x_axis, y_axis, grau=grau, novos_x=valores_para_avaliar)

    for xi, ci in zip(valores_para_avaliar, res):
        print(f"f({xi}) = {ci:.6f}")