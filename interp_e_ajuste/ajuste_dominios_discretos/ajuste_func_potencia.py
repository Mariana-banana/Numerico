import numpy as np

def ajuste_potencia(x_axis:list[float], y_axis:list[float]):
	n = len(x_axis)

	if len(x_axis) != len(y_axis):
		print("Warning: x_axis e y_axis com larguras diferentes. Verifique se está correto.")

	a11 = sum(1 for _ in range(n))
	a12 = sum(np.log(x) for x in x_axis)
	a21 = sum(np.log(x) for x in x_axis)
	a22 = sum(np.log(x)**2 for x in x_axis)

	b0 = sum(np.log(y) for y in y_axis)
	b1 = sum(np.log(x_axis[i])*np.log(y_axis[i]) for i in range(n))

	A = np.array([[a11, a12],
		          [a21, a22]])

	B = np.array([b0, b1])

	print(A, B)

	return np.linalg.solve(A, B)

if __name__ == '__main__':

	x_axis = [10, 20, 30, 40, 60, 70]
	y_axis = [0.313, 0.250, 0.215, 0.192, 0.164, 0.154]
 
	res = ajuste_potencia(x_axis, y_axis)

	print(f"y = {round(np.e**res[0], 10)} * x^{round(res[1], 10)}")