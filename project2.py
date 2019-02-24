import numpy as np
import math as mth

def f(x):
    return ((np.e**x**2))

def Simpson(f, a, b, error, helper):

    er =((helper*(b-a)**5)/(180*error))**(1/4)
    n = mth.ceil(er / 2.) * 2
    integ = 0.0
    dx = (b-a) / n
    x = a
    for i in range(0, n // 2):
        integ += f(x) + (2.0 * f(x + dx))
        x += 2 * dx
    integ = (2.0 * integ) - f(a) + f(b)
    integ = dx * integ / 3.0
    return integ

def Trapazoidal(f, a, b, error, helper):
    er = ((helper*(b-a)**3)/(12*error))**(1/2)
    n = mth.ceil(er/ 2.) *2
    dx = (b-a) / n
    integ = 0.0
    integ += f(a)/2.0
    for i in range(1, n):
        integ += f(a + i*dx)
    integ += f(b)/2.0
    return integ * dx

print(Simpson(f, 0, 2, .00001, 76*np.e))
print(Trapazoidal(f, 0, 2, .00001, 76*np.e))

