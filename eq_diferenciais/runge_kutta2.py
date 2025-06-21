# Python3 program to implement Runge
# Kutta method

# Finds value of y for a given x
# using step size h
# and initial value y0 at x0.


def rungeKutta(x0, y0, x, h):

    # Count number of iterations
    # using step size or
    # step height h
    n = round((x - x0) / h)

    # Iterate for number of iterations
    y = y0

    for i in range(1, n + 1):

                # Apply Runge Kutta Formulas        
        # to find next value of y
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)

        # Update next value of y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2)

        # Update next value of x
        x0 = x0 + h

        print(f"Iteração {i}: y = {y}")

    return y


# Driver Code
if __name__ == "__main__":

    # A sample differential equation
    def dydx(t, y):
        return 1 - t + 4*y

    x0 = 0
    y = 1
    x = 0.4
    h = 0.1

    rungeKutta(x0, y, x, h)
