import numpy as np
import matplotlib.pyplot as plt

def avg(l:list[float]) -> float:
    return sum(l)/len(l)

def analise(X, Y):
    
    if(len(X) != len(Y)):
        print("WARNING: Tamanho dos vetores de entrada é diferente!!")

    print("-----------------------------------------------")

    X = np.array(X)
    Y = np.array(Y)
    
    print("Reta:")
    A = np.diff(X)
    B = np.diff(Y)
    with np.errstate(divide='ignore', invalid='ignore'):
        buf = B / A
    print(buf, sum(abs(avg(buf) - val) for val in buf))

    print("\nParábola:")
    A = np.diff(X**2)
    B = np.diff(Y)**2
    with np.errstate(divide='ignore', invalid='ignore'):
        buf = B / A
    print(buf, sum(abs(avg(buf) - val) for val in buf))

    print("\nCúbica:")
    A = np.diff(X**3)
    B = np.diff(Y)**3
    with np.errstate(divide='ignore', invalid='ignore'):
        buf = B / A
    print(buf, sum(abs(avg(buf) - val) for val in buf))

    print("\nExponencial:")
    A = np.diff(X)
    with np.errstate(divide='ignore', invalid='ignore'):
        B = np.diff(np.log(Y))
        buf = B / A
    print(buf, sum(abs(avg(buf) - val) for val in buf))

    print("\nPotência:")
    with np.errstate(divide='ignore', invalid='ignore'):
        A = np.diff(np.log(X))
        B = np.diff(np.log(Y))
        buf = B / A
    print(buf, sum(abs(avg(buf) - val) for val in buf))

    print("-----------------------------------------------")
    

    plt.plot(X, Y, 'g.', label='Dados')
    plt.title('Pontos analisados')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
   # plt.show()

if __name__ == '__main__':

    x_axis = [10, 20, 30, 40, 60, 70] 
    y_axis = [0.313, 0.250, 0.215, 0.192, 0.164, 0.154]

    analise(x_axis, y_axis)
