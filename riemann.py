import numpy as np

def f(x):
    return (2*np.pi*(x*(9-x**2)))

def riemann(f, a, b, error):
    x = b
    fb = (f(x))
    x = a
    fa = (f(x))
    sl = np.abs((b-a)*(fb - fa))
    n = sl/error
    dx = (b-a) / n
    x = np.linspace(a, b, n+1)
    re = np.sum(f(x)*dx)

    return re
    

print(riemann(f, 2, 3, 0.001))

