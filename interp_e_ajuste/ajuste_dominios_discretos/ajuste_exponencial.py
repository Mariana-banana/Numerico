import numpy as np

def ajuste_exponencial(x_axis:list[float], y_axis:list[float]):

	if(len(x_axis) != len(y_axis)):
		print("WARNING: Tamanho dos vetores de entrada é diferente!!!!")

	a11 = sum(1 for _ in range(len(x_axis))) #segunda diagonal 1

	a12 = sum(x for x in x_axis) #segunda diagonal 2
	a21 = sum(x for x in x_axis)

	a22 = sum(x**2 for x in x_axis) #segunda diagonal 3

	b0 = sum(np.log(y) for y in y_axis)
	b1 = sum(x_axis[i]*np.log(y_axis[i]) for i in range(len(x_axis)))

	if len(x_axis) != len(y_axis):
		print("Warning: x_axis e y_axis com larguras diferentes. Verifique se está correto.")

	A = np.array([[a11, a12],
		         [a21, a22]])

	B = np.array([b0, b1])

	print(A,B)

	return np.linalg.solve(A, B)

if __name__ == "__main__":
	x_axis = [250, 330, 412, 485, 617]
	y_axis = [5720, 5260, 4450, 2780, 1506]

	res = ajuste_exponencial(x_axis, y_axis)
	print(res)

	print(f"f(x) = {round(np.e**res[0], 10)} * e^({round(res[1], 10)}x) ")