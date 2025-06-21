def resolver_sistema_explicito(h, n, z0, z1, y0, y1, f_zpp, f_ypp):
    x = 0
    za = z0      # z_n
    zaa = z1     # z_{n-1}
    ya = y0      # y_n
    yaa = y1     # y_{n-1}

    for _ in range(n):
        z = 2*za - zaa + h**2 * f_zpp(x, za, ya)
        y = 2*ya - yaa + h**2 * f_ypp(x, za, ya)
        x += h
        zaa = za
        za = z
        yaa = ya
        ya = y

    return za, ya	


if __name__ == '__main__':
	import math

	# Definindo as equações do sistema
	def f_zpp(x, z, y):
	    return z**2 - y + math.exp(x)

	def f_ypp(x, z, y):
	    return z - y**2 - math.exp(x)

	# Resolvendo o sistema
	h = 0.0001
	n = 10000
	z0 = 0
	z1 = 0
	y0 = 1
	y1 = y0 + 2*h  # valor fictício como no SCILAB

	z_final, y_final = resolver_sistema_explicito(h, n, z0, z1, y0, y1, f_zpp, f_ypp)
	print(f"z({n*h}) ≈ {z_final}")
	print(f"y({n*h}) ≈ {y_final}")
