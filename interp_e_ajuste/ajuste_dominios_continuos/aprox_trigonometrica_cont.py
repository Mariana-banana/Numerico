import numpy as np
import math

def aprox_trigonometrica_cont(x_axis:list[float], y_axis:list[float]):
	N = len(x_axis)//2

	a0 = (1/(2*N))*sum(y for y in y_axis)
	a1 = (1/2)*sum(y_axis[i]*math.cos((i*np.pi)/2) for i in range(2*N))
	a2 = (1/2)*sum(y_axis[i]*math.sin((i*np.pi)/2) for i in range(2*N))

	return [a0, a1, a2]	

if __name__ == '__main__':
	j =   [1, 2, 3, 4]
	fxj = [3, 5, 7, 6]

	res = aprox_trigonometrica_cont(j, fxj)
	print(f"{round(res[0], 4)} {round(res[1], 4)}*cos(x) {round(res[2], 4)}*sen(x)")
