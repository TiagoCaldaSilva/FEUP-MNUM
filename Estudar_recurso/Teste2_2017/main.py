import math as m


def gauss_seidel_4(x0, y0, z0, t0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    t = t0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    t0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error or abs(t - t0) > error) and _it != it:
        print(x, y, z, t, _it)
        x0 = x
        y0 = y
        z0 = z
        t0 = t
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0 - matrix[0][3]*t0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x - matrix[1][2]*z0 - matrix[1][3]*t0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x - matrix[2][1]*y - matrix[2][3]*t0) / matrix[2][2]
        t = (b[3] - matrix[3][0]*x - matrix[3][1]*y - matrix[3][2]*z) / matrix[3][3]
        _it += 1
    print(x, y, z, t, _it)
    return x, y, z, t


print("EX2:")
gauss_seidel_4(2.12687, 2.39858, 3.99517, -3.73040, [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2], [-1, 0.25, 4, 2], [2, 4, 1, 8]], [25, 10, 7, -12], 10**-4, 1)


f_values_0_25 = [1.04, 0.37, 0.38, 1.49, 1.08, 0.13, 0.64, 0.84, 0.12]

f_values_0_50 = [1.04, 0.38, 1.08, 0.64, 0.12]

f_values_1 = [1.04, 1.08, 0.12]


def ex3_25():
    result = 0
    h = 0.25
    for i, v in enumerate(f_values_0_25):
        if i == 0 or i == len(f_values_0_25) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


def ex3_50():
    result = 0
    h = 0.50
    for i, v in enumerate(f_values_0_50):
        if i == 0 or i == len(f_values_0_50) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


def ex3_1():
    result = 0
    h = 1
    for i, v in enumerate(f_values_1):
        if i == 0 or i == len(f_values_1) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


s = ex3_1()
s_ = ex3_50()
s__ = ex3_25()
error_ = (s__ - s_) / 15
print("EX3:")
print(s__, error_)


def cubatura():
    hx = 1
    hy = 1
    soma_vertices = 7.3 + 1.2 + 1.1 + 7.7
    soma_medios = 2.1 + 1.5 + 2.2 + 1.4
    centro = 3.1
    result = (hx * hy) / 4 * (soma_vertices + 2*soma_medios + 4*centro)
    print(result)


print("EX4:")
cubatura()


def ex6_y(t, y, z):
    return z


def ex6_z(t, y, z):
    return 2 + t**2 + t*z


def euler_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, z, _it)
        y_old = y
        y += functions[0](x, y, z) * h
        z += functions[1](x, y_old, z) * h
        x += h
        _it += 1
    print(x, y, z, _it)
    return y, z


def delta1_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x, y, z)
    return h * function[1](x, y, z)


def delta2_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h/2, y + delta1_system(x, y, z, h, function, char) / 2, z + delta1_system(x, y, z, h, function, 'z') / 2)
    return h * function[1](x + h/2, y + delta1_system(x, y, z, h, function, 'y') / 2, z + delta1_system(x, y, z, h, function, char) / 2)


def delta3_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h/2, y + delta2_system(x, y, z, h, function, char) / 2, z + delta2_system(x, y, z, h, function, 'z') / 2)
    return h * function[1](x + h/2, y + delta2_system(x, y, z, h, function, 'y') / 2, z + delta2_system(x, y, z, h, function, char) / 2)


def delta4_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h, y + delta3_system(x, y, z, h, function, char), z + delta3_system(x, y, z, h, function, 'z'))
    return h * function[1](x + h, y + delta3_system(x, y, z, h, function, 'y'), z + delta3_system(x, y, z, h, function, char))


def delta_system(x, y, z, h, function, char):
    return delta1_system(x, y, z, h, function, char)/6 + delta2_system(x, y, z, h, function, char)/3 + delta3_system(x, y, z, h, function, char)/3 + delta4_system(x, y, z, h, function, char)/6


def rk4_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, z, _it)
        y_old = y
        y += delta_system(x, y_old, z, h, functions, 'y')
        z += delta_system(x, y_old, z, h, functions, 'z')
        x += h
        _it += 1
    print(x, y, z, _it)
    return y, z


print("EX6:")
print("Euler:")
euler_system(1, 8, 1, 0, [ex6_y, ex6_z], 0.25, 10**-4, 2)
print("RK4:")
rk4_system(1, 8, 1, 0, [ex6_y, ex6_z], 0.25, 10**-4, 2)
