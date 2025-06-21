import numpy as np

def ajuste_polinomio(x_axis:list[float], y_axis:list[float], g:int):
	
	if len(x_axis) != len(y_axis):
		print("WARNING: x_axis e y_axis com larguras diferentes. Verifique se está correto.")
		exit(1)

	A = np.empty(shape=(g, g))

	for i in range(g):
		for j in range(g):
			A[i][j] = sum(x**(i + j) for x in x_axis)

	B = np.array([0]*g)

	for i in range(g):
		B[i] = sum((x_axis[j]**i)*y_axis[j] for j in range(len(x_axis)))

	print(A, B) 

	return np.linalg.solve(A, B)

if __name__ == '__main__':

	x_axis = ([250,330,412,485,617])
	y_axis = ([5720,5260,4450,2780,1506])
	g = 3 # grau do polinomio de aproximaçao

	valores_para_avaliar = x_axis + [380, 730]

	res = ajuste_polinomio(x_axis, y_axis, g + 1)

	print("--------------------------------------------\n")

	i = g
	for x in res[::-1]:
		print(f"{round(x,10)}x^{i} + ", end = "")
		i -= 1

	print("\n\n--------------------------------------------\n")

	for val in valores_para_avaliar:
		resultado = sum(coef * (val ** i) for i, coef in enumerate(res))
		print(f"f({val}) = {resultado}")
