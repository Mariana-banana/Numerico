import numpy as np
import math

# g(x) = a0 + a1 cos x + b1 sen x

def aprox_trigonometrica_cont(x_axis:list[float], y_axis:list[float]):
	N = len(x_axis)//2

	a0 = 0
	a1 = 0
	b1 = 0

	a0 = (1/(2*N))*sum(y for y in y_axis)
	a1 = (1/N)*sum(y_axis[i]*math.cos((i*np.pi)/2) for i in range(2*N))
	b1 = (1/N)*sum(y_axis[i]*math.sin((i*np.pi)/2) for i in range(2*N))

	return [a0, a1, b1]	

if __name__ == '__main__':
	x_axis = [-1,1,2,3]
	y_axis = [-1,1,3,4]

	res = aprox_trigonometrica_cont(x_axis, y_axis)

	print(f"{res[0]} {res[1]}*sen(x) {res[2]}*cos(x)")
