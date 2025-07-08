import numpy as np

def interp_polinomial(x_axis:list[float], y_axis:list[float], g:int):
	A = np.empty(shape=(g, g))
	B = np.array([0]*g)

	for i in range(g):
		A[i] = [x_axis[i]**k for k in range(g)]

	for i in range(g):
		B[i] = y_axis[i]

	print(A, B,"\n")

	res = np.linalg.solve(A, B)

	return res

if __name__ == '__main__':
	x_axis = [0.1, 0.2, 0.3, 0.4]
	y_axis = [4, 16, -4, -16]
	g = 3

	res = interp_polinomial(x_axis, y_axis, g + 1)

	i = len(res) -1

	for x in res[::-1]:
		print(f"{round(x,4)}x^{i} ", end="")
		i -= 1

	print("")