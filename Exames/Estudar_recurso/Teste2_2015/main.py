import math as m


x_values = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75]
f_values = [0.36, 1.19, 1.32, 0.21, 1.15, 1.39,  0.12, 1.22, 0.6]


f_values_1 = [0.36, 1.15, 0.6]
f_values_0_50 = [0.36, 1.32, 1.15, 0.12, 0.6]


def ex1_0_25():
    result = 0
    h = 0.25
    for i, elem in enumerate(f_values):
        if i == 0 or i == len(f_values) - 1:
            result += elem
        elif i % 2:
            result += 4 * elem
        else:
            result += 2 * elem
    return result * h / 3


def ex1_1():
    result = 0
    h = 1
    for i, elem in enumerate(f_values_1):
        if i == 0 or i == len(f_values_1) - 1:
            result += elem
        elif i % 2:
            result += 4 * elem
        else:
            result += 2 * elem
    return result * h / 3


def ex1_0_50():
    result = 0
    h = 0.5
    for i, elem in enumerate(f_values_0_50):
        if i == 0 or i == len(f_values_0_50) - 1:
            result += elem
        elif i % 2:
            result += 4 * elem
        else:
            result += 2 * elem
    return result * h / 3


print("EX1:")
s = ex1_1()
s_ = ex1_0_50()
s__ = ex1_0_25()
print(s__)
error_ = (s__ - s_) / 15
print(error_)


def gauss_jacobi_4(x0, y0, z0, t0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    t = t0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    t0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error) and _it != it:
        print(x, y, z, t, _it)
        x0 = x
        y0 = y
        z0 = z
        t0 = t
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0 - matrix[0][3]*t0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x0 - matrix[1][2]*z0 - matrix[1][3]*t0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x0 - matrix[2][1]*y0 - matrix[2][3]*t0) / matrix[2][2]
        t = (b[3] - matrix[3][0]*x0 - matrix[3][1]*y0 - matrix[3][2]*z0) / matrix[3][3]
        _it += 1
    print(x, y, z, t, _it)
    return x, y, z, t


print("EX2:")
gauss_jacobi_4(0.25, 0.25, 0.25, 0.25, [[4.5, -1, -1, 1], [-1, 4.5, 1, -1], [-1, 2, 4.5, -1], [2, -1, -1, 4.5]], [1, -1, -1, 0], 10**-4, 2)


def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        _it += 1
    print(x0, y, _it)
    return y


def ex4_f(t, T):
    return -0.25*(T-45)


print("EX4:")
euler(1, 8, 23, ex4_f, 0.4, 10**-4, 2)
