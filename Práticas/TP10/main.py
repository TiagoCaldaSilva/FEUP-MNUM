import numpy as np
import math as m
import sympy as sp

# FUNCTION DEFINITION
print("Function definition: ")


def f(x, y):
    return y ** 2 - 2 * x * y - 6 * y + 2 * (x ** 2) + 12 + m.cos(4 * x)


__x, __y = sp.symbols('x y')
first_diff_x = sp.diff(__y ** 2 - 2 * __x * __y - 6 * __y + 2 * (__x ** 2) + 12 + sp.cos(4 * __x), __x)
print("df/dx = {}".format(first_diff_x))
first_diff_y = sp.diff(__y ** 2 - 2 * __x * __y - 6 * __y + 2 * (__x ** 2) + 12 + sp.cos(4 * __x), __y)
print("df/dx = {}".format(first_diff_y))


def df_dx(x, y):
    return -2 * y + 4 * x - 4 * m.sin(4 * x)


def df_dy(x, y):
    return 2 * y - 2 * x - 6


second_diff_xx = sp.diff(-2 * __y + 4 * __x - 4 * sp.sin(4 * __x), __x)
print("df/dxx = {}".format(second_diff_xx))
second_diff_yy = sp.diff(2 * __y - 2 * __x - 6, __y)
print("df/dyy = {}".format(second_diff_yy))
second_diff_xy = sp.diff(-2 * __y + 4 * __x - 4 * sp.sin(4 * __x), __y)
print("df/dxy = {}".format(second_diff_xy))


def df_dxx(x, y):
    return 4 - 16 * m.cos(4 * x)


def df_dyy(x, y):
    return 2


def df_dxy(x, y):
    return -2


def g(x, y):
    return (x + 1) ** 2 + (y - 4) ** 2


first_diff_x = sp.diff(g(__x, __y), __x)
print("\ndg/dx = {}".format(first_diff_x))
first_diff_y = sp.diff(g(__x, __y), __y)
print("dg/dy = {}".format(first_diff_y))


def dg_dx(x, y):
    return 2 * x + 2


def dg_dy(x, y):
    return 2 * y - 8


second_diff_xx = sp.diff(dg_dx(__x, __y), __x)
print("dg/dxx = {}".format(second_diff_xx))
second_diff_yy = sp.diff(dg_dy(__x, __y), __y)
print("dg/dyy = {}".format(second_diff_yy))
second_diff_xy = sp.diff(dg_dx(__x, __y), __y)
print("dg/dxy = {}".format(second_diff_xy))


def dg_dxx(x, y):
    return 2


def dg_dyy(x, y):
    return 2


def dg_dxy(x, y):
    return 0


print("\nMethods application:")


def quadratic_method(x0, y0, error, function, function_diffs):
    x_old = x0 + 10
    y_old = y0 + 10
    while abs(x0 - x_old) >= error or abs(y0 - y_old) >= error:
        x_old = x0
        y_old = y0
        h_matrix = [[function_diffs[2](x_old, y_old), function_diffs[4](x_old, y_old)],
                    [function_diffs[4](x_old, y_old), function_diffs[3](x_old, y_old)]]

        gradient = [[function_diffs[0](x_old, y_old)],
                    [function_diffs[1](x_old, y_old)]]
        # print(np.dot(np.linalg.inv(h_matrix), gradient)[0][0], np.dot(np.linalg.inv(h_matrix), gradient)[1][0])
        x0 = x_old - np.dot(np.linalg.inv(h_matrix), gradient)[0][0]
        y0 = y_old - np.dot(np.linalg.inv(h_matrix), gradient)[1][0]
        if function(x0, y0) > function(x_old, y_old):
            x0 = x0 - 1
            y0 = y0 - 1
    return x0, y0


print("\nQuadratic method:")
x_, y_ = quadratic_method(1, 1, 10 ** -4, f, [df_dx, df_dy, df_dxx, df_dyy, df_dxy])
print("x = {} | y = {} | f(x, y) = {}".format(x_, y_, f(x_, y_)))

x_, y_ = quadratic_method(1, 1, 10 ** -4, g, [dg_dx, dg_dy, dg_dxx, dg_dyy, dg_dxy])
print("x = {} | y = {} | g(x, y) = {}".format(x_, y_, g(x_, y_)))


def hlm(x_old, y_old, lambda_, function_diffs):
    h = [[function_diffs[2](x_old, y_old), function_diffs[4](x_old, y_old)],
         [function_diffs[4](x_old, y_old), function_diffs[3](x_old, y_old)]]

    gradient = [[function_diffs[0](x_old, y_old)],
                [function_diffs[1](x_old, y_old)]]

    return np.dot(np.linalg.inv(h), gradient) + [[lambda_ * gradient[0][0]], [lambda_ * gradient[1][0]]]


def levenberg_marquardt(x, y, error, lambda_, function, functions_diffs):
    x_old = x + 10
    y_old = y + 10
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        h = hlm(x_old, y_old, lambda_, functions_diffs)
        x = x_old - hlm(x_old, y_old, lambda_, functions_diffs)[0][0]
        y = y_old - hlm(x_old, y_old, lambda_, functions_diffs)[1][0]
        if function(x, y) > function(x_old, y_old):
            lambda_ *= 2
        else:
            lambda_ /= 2
    return x, y


print("\nlevenberg_marquardt: ")
x_, y_ = levenberg_marquardt(1, 1, 10 ** -4, 0.05, f, [df_dx, df_dy, df_dxx, df_dyy, df_dxy])
print("x = {} | y = {} | f(x, y) = {}".format(x_, y_, f(x_, y_)))

x_, y_ = levenberg_marquardt(0, 0, 10 ** -4, 0.35, g, [dg_dx, dg_dy, dg_dxx, dg_dyy, dg_dxy])
print("x = {} | y = {} | g(x, y) = {}".format(x_, y_, g(x_, y_)))


def aula_teorica(x, y):
    return m.sin(x) + m.sin(y)


def d_aula_dx(x, y):
    return m.cos(x)


def d_aula_dy(x, y):
    return m.cos(y)


def d_aula_dxy(x, y):
    return 0


def d_aula_dxx(x, y):
    return -m.sin(x)


def d_aula_dyy(x, y):
    return -m.sin(y)


print("\nQuadratic method:")
x_, y_ = quadratic_method(4, -2, 10 ** -4, aula_teorica, [d_aula_dx, d_aula_dy, d_aula_dxx, d_aula_dyy, d_aula_dxy])
print("x = {} | y = {} | f(x, y) = {}".format(x_, y_, aula_teorica(x_, y_)))

print("\nlevenberg_marquardt: ")
x_, y_ = levenberg_marquardt(4, -2, 10 ** -4, 0.05, aula_teorica,
                             [d_aula_dx, d_aula_dy, d_aula_dxx, d_aula_dyy, d_aula_dxy])
print("x = {} | y = {} | f(x, y) = {}".format(x_, y_, aula_teorica(x_, y_)))


def rikcy(x, y):
    return m.sin(x / 2) + x ** 2 - m.cos(y)


def dricky_dx(x, y):
    return m.cos(x / 2) / 2 + 2 * x


def dricky_dy(x, y):
    return m.sin(y)


def dricky_dxdx(x, y):
    return -m.sin(x / 2) / 4 + 2


def dricky_dydy(x, y):
    return m.cos(y)


def dricky_dxdy(x, y):
    return 0


print("\nlevenberg_marquardt RICKY: ")
x_, y_ = levenberg_marquardt(10, -1, 0.001, 0.05, rikcy, [dricky_dx, dricky_dy, dricky_dxdx, dricky_dydy, dricky_dxdy])
print("x = {} | y = {} | f(x, y) = {}".format(x_, y_, rikcy(x_, y_)))


# def f(x, y):
#     return y ** 2 - 2 * x * y - 6 * y + 2 * (x ** 2) + 12 + m.cos(4 * x)

def mf_dx(x, y):
    return -2*y+4*x-m.sin(4*x)*4


def mf_dy(x, y):
    return 2*y -2*x -6


def mf_dxx(x, y):
    return 4-m.cos(4*x)*16


def mf_dyx(x, y):
    return -2


def mf_dyy(x, y):
    return 2


def mf_dxy(x, y):
    return -2


def my_quadratic(x, y, h, g, f, error):
    x_old = x + 10 * error
    y_old = y + 10 * error
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        det = h[0][0](x_old, y_old)*h[1][1](x_old, y_old) - h[1][0](x_old, y_old)*h[0][1](x_old, y_old)
        x -= (h[1][1](x_old, y_old)*g[0](x_old, y_old) - h[0][1](x_old, y_old)*g[1](x_old, y_old)) / det
        y -= (h[0][0](x_old, y_old)*g[1](x_old, y_old) - h[0][1](x_old, y_old)*g[0](x_old, y_old)) / det
    return x , y


x_value, y_value = my_quadratic(1, 1, [[mf_dxx, mf_dyx], [mf_dxy, mf_dyy]], [mf_dx, mf_dy], f, 10 ** -4)
print("my test = {} | {}".format((x_value, y_value), f(x_value, y_value)))


def my_lavenberg(x, y, h, g, lam,f, error):
    x_old = x + 10 * error
    y_old = y + 10 * error
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        det = h[0][0](x_old, y_old)*h[1][1](x_old, y_old) - h[1][0](x_old, y_old)*h[0][1](x_old, y_old)
        quad1 = (h[1][1](x_old, y_old)*g[0](x_old, y_old) - h[0][1](x_old, y_old)*g[1](x_old, y_old)) / det
        quad2 = (h[0][0](x_old, y_old)*g[1](x_old, y_old) - h[0][1](x_old, y_old)*g[0](x_old, y_old)) / det
        x -= (quad1 + lam*g[0](x_old, y_old))
        y -= (quad2 + lam*g[1](x_old, y_old))
        if f(x, y) < f(x_old, y_old):
            lam /= 2
        else:
            lam *= 2
    return x , y


x_value, y_value = my_lavenberg(1, 1, [[mf_dxx, mf_dyx], [mf_dxy, mf_dyy]], [mf_dx, mf_dy],0.05, f, 10 ** -4)
print("my test = {} | {}".format((x_value, y_value), f(x_value, y_value)))


