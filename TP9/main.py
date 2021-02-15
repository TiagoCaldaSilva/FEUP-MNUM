import math
import sympy as sp

number_b = (math.sqrt(5) - 1) / 2
number_a = number_b ** 2


def f_u(x):
    return (2*(x**2) + 1) - 5*math.cos(10*x)


def f(x, y):
    return (y**2) - (2 * x * y) - (6 * y) + 2 * (x ** 2) + 12


def g(x, y):
    return (x + 1)**2 + (y - 4)**2 + math.sin(x)


__x, __y = sp.symbols('x y')
dif = sp.diff(f(__x, __y), __x)
print("df/dx = {}".format(dif))
dif = sp.diff(f(__x, __y), __y)
print("df/dy = {}" .format(dif))
dif = sp.diff((__x + 1)**2 + (__y - 4)**2 + sp.sin(__x), __x)
print("dg/dx = {}".format(dif))
dif = sp.diff((__x + 1)**2 + (__y - 4)**2 + sp.sin(__x), __y)
print("dg/dy = {}" .format(dif))


def df_dx(_x, _y):
    return 4 * _x - 2 * _y


def df_dy(_x, _y):
    return -2 * _x + 2 * _y - 6


def dg_dx(x, y):
    return 2 * x + math.cos(x) + 2


def dg_dy(x, y):
    return 2 * y - 8


def u_optimization_minimum(x1, x2, error):
    while abs(x1-x2) > error:
        x3 = x1 + number_a * (x2 - x1)
        x4 = x1 + number_b * (x2 - x1)
        if f_u(x3) < f_u(x4):
            x2 = x4
        else:
            x1 = x3
    return min([x1, x2, x3, x4])


def u_optimization_maximum(x1, x2, error):
    while abs(x1-x2) > error:
        x3 = x1 + number_a * (x2 - x1)
        x4 = x1 + number_b * (x2 - x1)
        if f_u(x3) > f_u(x4):
            x2 = x4
        else:
            x1 = x3
    return max([x1, x2, x3, x4])


minimum = u_optimization_minimum(-1, 0, 0.0001)
print("Min: {}".format(minimum))
maximum = u_optimization_maximum(-1, 0, 0.0001)
print("Max: {}".format(maximum))


def m_optimization_minimum(x, y, error, f_m, df_m):
    # h = 1 mudado na teorica para ex
    h = 0.01
    x_old = x + error * 10
    y_old = y + error * 10
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        x = x_old - h * df_m[0](x_old, y_old)
        y = y_old - h * df_m[1](x_old, y_old)
        if f_m(x, y) > f_m(x_old, y_old):
            h /= 2
            x = x_old
            y = y_old
            x_old += error * 10
            y_old += error * 10
        else:
            h *= 2
    return x, y, f_m(x, y)


def m_optimization_maximum(x, y, error, f_m, df_m):
    h = 1
    x_old = x + error * 10
    y_old = y + error * 10
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        x = x_old - h * df_m[0](x_old, y_old)
        y = y_old - h * df_m[1](x_old, y_old)
        if f_m(x, y) < f_m(x_old, y_old):
            h /= 2
            x = x_old
            y = y_old
            x_old += error * 10
            y_old += error * 10
        else:
            h *= 2
    return x, y, f_m(x, y)


x_, y_, value = m_optimization_minimum(1, 1, 0.01, f, [df_dx, df_dy])
print("F -> Min: x = {} \t| y = {} \t| f(x, y) = {}" .format(x_, y_, value))
x_, y_, value = m_optimization_minimum(0, 0, 0.01, g, [dg_dx, dg_dy])
print("G -> Min: x = {} \t| y = {} \t| f(x, y) = {}" .format(x_, y_, value))


def aula_teorica(x, y):
    return math.sin(x) + math.sin(y)


def d_aula_dx(x, y):
    return math.cos(x)


def d_aula_dy(x, y):
    return math.cos(y)


x_, y_, value = m_optimization_minimum(2,-2, 0.001, aula_teorica, [d_aula_dx, d_aula_dy])
print("F -> Min: x = {} \t| y = {} \t| f(x, y) = {}" .format(x_, y_, value))
