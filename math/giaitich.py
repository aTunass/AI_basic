import sympy
import numpy as np
x = sympy.Symbol('x')
f = x**2 + 2*x + 1
print('dao ham cua f la: ',sympy.diff(f,x))

"""Gia phuong trinh vi phan
y'' - y=0
y(0) = 1
y'(0) = 0
"""
from scipy.integrate import solve_ivp
def func(t,y):
    y1, y2 = y
    return [y2, y1]
sol = solve_ivp(func, [0,10], [1,0], t_eval=np.linspace(0,10,101))
print(sol[0])