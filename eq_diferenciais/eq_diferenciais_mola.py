def massa_mola_diferencas_finitas(m, k, h, ya, yaa, n_passos):
    """
    Resolve a equação de uma mola massa com diferenças finitas centrais.

    Argumentos:
        m (float): massa (kg)
        k (float): constante da mola (N/m)
        y0 (float): deslocamento inicial (m)
        h (float): passo de tempo (s)
        n_passos (int): número de passos a calcular

    Retorna:
        lista com os valores de y a cada passo
    """
    omega2 = (k / m)
    y = [0.0] * (n_passos + 1)

    y[0] = yaa
    y[1] = ya

    print(omega2)


    # Iteração por diferenças finitas
    for n in range(1, n_passos):
        y[n + 1] = 2*y[n] - y[n-1] + h**2*(-omega2*y[n])

    return y

# Exemplo de uso com os dados do enunciado
if __name__ == "__main__":
    m = 5.0         # massa (kg)
    k = 48.0        # constante da mola (kg/m)
    y0 = 0.02       # deslocamento inicial (m)
    h = 0.1         # passo de tempo (s)
    n_passos = 100   # número de passos
    ya = 0.02          # Aproximação segundo termo
    yaa = 0.02         # Aproximação primeiro termo
 
    resultados = massa_mola_diferencas_finitas(m, 10*k, h, ya, yaa, n_passos)

    for i, y in enumerate(resultados):
        print(f"t = {i*h:.2f} s -> y = {y:.5f} m")
