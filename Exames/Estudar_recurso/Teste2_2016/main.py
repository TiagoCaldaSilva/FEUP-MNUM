import math as m


def ex1_C(t, T, C):
    return - m.exp(-0.5/(T + 273))*C


def ex1_T(t, T, C):
    return 20*m.exp(-0.5/(T+273))*C - 0.5*(T-20)


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


print("EX1:")
print("Euler:")
euler_system(0, 8, 15,  1, [ex1_T, ex1_C], 0.25, 10**-4, 2)
print("RK4:")
rk4_system(0, 8, 15,  1, [ex1_T, ex1_C], 0.25, 10**-4, 2)


def qc_value_euler_rk_system(method, h0, x0, xf, y, z, functions, it, order, error):
    _y, _z = method(x0, xf, y, z, functions, h0, error, it)
    y_, z_ = method(x0, xf, y, z, functions, h0 / 2, error, it*2)
    y__, z__ = method(x0, xf, y, z, functions, h0 / 4, error, it*4)
    qcy = (y_ - _y) / (y__ - y_)
    qcz = (z_ - _z) / (z__ - z_)
    # print(_y, h0)
    # print(y_, h0/2)
    # print(y__, h0/4)
    # print(qcy)
    print(_z, h0)
    print(z_, h0/2)
    print(z__, h0/4)
    print(qcz)
    # while int(qcy + 0.5) != 2**order or int(qcz + 0.5) != 2**order:
    #     h0 /= 2
    #     _y, _z = method(x0, xf, y, z, functions, h0, error, it)
    #     y_, z_ = method(x0, xf, y, z, functions, h0 / 2, error, it)
    #     y__, z__ = method(x0, xf, y, z, functions, h0 / 4, error, it)
    #     qcy = (y_ - _y) / (y__ - y_)
    #     qcz = (z_ - _z) / (z__ - z_)

    error_y = (y__ - y_) / (2**order - 1)
    error_z = (z__ - z_) / (2 ** order - 1)
    # print("qcy = {} | erro absoluto estimado y = {} | h = {}" .format(qcy, error_y, h0))
    print("qcz = {} | erro absoluto estimado z = {} | h = {}" .format(qcz, error_z, h0))
    # print("erro relativo estimado y = {}" .format(error / y__))
    # print("erro relativo estimado z = {}".format(error / z__))


print("qc")
qc_value_euler_rk_system(euler_system, 0.25, 0, 8, 15, 1, [ex1_T, ex1_C], 2, 1, 10**-4)


print("EX2:")
x_values = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6]
f_values_0_20 = [0.18, 0.91, 0.83, 1.23, 0.88, 1.37, 0.8, 1.34, 0.43]

f_values_0_40 = [0.18, 0.83, 0.88, 0.8, 0.43]

f_values_0_80 = [0.18, 0.88, 0.43]


def ex2_0_2():
    result = 0
    h = 0.2
    for i, v in enumerate(f_values_0_20):
        if i == 0 or i == len(f_values_0_20) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


def ex2_0_4():
    result = 0
    h = 0.4
    for i, v in enumerate(f_values_0_40):
        if i == 0 or i == len(f_values_0_40) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


def ex2_0_8():
    result = 0
    h = 0.8
    for i, v in enumerate(f_values_0_80):
        if i == 0 or i == len(f_values_0_80) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


s80 = ex2_0_8()
s40 = ex2_0_4()
s20 = ex2_0_2()

error_ = (s20 - s40) / 15

print(s20, error_)


def ex4(t, T):
    return -0.25*(T-42)


def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        _it += 1
    print(x0, y, _it)
    return y


print("EX4:")
euler(5, 20, 10, ex4, 0.4, 10**-4, 2)


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


print("EX5:")
gauss_seidel_4(0, 0, 0, 0, [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2], [-1, 0.25, 4, 2], [2, 4, 1, 8]], [2.5, 3.8, 10, 7], 10**-4, 1)
