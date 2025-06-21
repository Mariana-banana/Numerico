
# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h, n, dydx):
    y = y0

    res = [y0]

    for i in range(1, n ):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
    
        res.append(y)

    return res

if __name__ == '__main__':

    # Python program to implement Runge Kutta method
    def dydx(x, y):
        return 1 - x + 4*y

    # Driver method
    x0 = 0
    y = 1
    x = 0.4
    h = 0.1
    n = 4

    res = rungeKutta(x0, y, x, h, n, dydx)
    for i, y in enumerate(res):
        print(f"Iteração {i}: y = {y}")


    # This code is contributed by Prateek Bhindwar