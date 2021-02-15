import math as m


f_values_1 = [0, 0.062057145,  1.0558914326, 5.3775128776, 17.0202629818, 41.5748215863, 86.2292060414, 159.7687706061, 272.5762067482, 436.6315430847, 665.5121453814, 974.3927165529, 1380.0452966628, 1900.8392629238, 2556.7413296971, 3369.3155484932, 4361.7233079714]
f_values_2 = [0, 1.0558914326, 17.0202629818, 86.2292060414, 272.5762067482, 665.5121453814, 1380.0452966628, 2556.7413296971, 4361.7233079714]
f_values_4 = [0, 17.0202629818, 272.5762067482, 1380.0452966628, 4361.7233079714]
f_values_8 = [0, 272.5762067482, 4361.7233079714]


def ex1_1():
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


def ex1_2():
    result = 0
    h = 2
    for i, v in enumerate(f_values_2):
        if i == 0 or i == len(f_values_2) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


def ex1_4():
    result = 0
    h = 4
    for i, v in enumerate(f_values_4):
        if i == 0 or i == len(f_values_4) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


def ex1_8():
    result = 0
    h = 8
    for i, v in enumerate(f_values_8):
        if i == 0 or i == len(f_values_8) - 1:
            result += v
        elif i % 2:
            result += 4 * v
        else:
            result += 2 * v
    return result * h / 3


print("EX1:")
s = ex1_8()
s_ = ex1_4()
s__ = ex1_2()
s___ = ex1_1()
print(s)
print(s_)
print(s__)
print(s___)
qc_1 = (s_ - s) / (s__ - s_)
qc_2 = (s__ - s_) / (s___ - s__)
error_1 = (s__ - s_) / 15
error_2 = (s___ - s__) / 15
print(qc_1, error_1)
print(qc_2, error_2)


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


print("EX3:")
gauss_seidel_4(-0.81959, 1.40167, 2.15095, 0.11019, [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2], [-1, 0.25, 4, 2], [2, 4, 1, 8]], [2.5, 3.8, 10, 7], 10**-4, 1)


def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        # print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        # _it += 1
    # print(x0, y, _it)
    return y


def ex4_f(t, x):
    return t * (t / 2 + 1) * (x ** 3) + (t + 5/2) * (x ** 2)


def qc_value_euler_rk(method, h0, x0, xf, y, function, it, order, error):
    s = method(x0, xf, y, function, h0, error, it)
    s_ = method(x0, xf, y, function, h0 / 2, error, it)
    s__ = method(x0, xf, y, function, h0 / 4, error, it)
    qc = (s_ - s) / (s__ - s_)
    print(s, h0)
    print(s_, h0/2)
    print(s__, h0/4)
    print(qc)
    # while int(qc + 0.5) != 2**order:
    #     h0 /= 2
    #     s = method(x0, xf, y, function, h0, error, it)
    #     s_ = method(x0, xf, y, function, h0 / 2, error, it)
    #     s__ = method(x0, xf, y, function, h0 / 4, error, it)
    #     qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


print("EX4:")
print("Euler")
qc_value_euler_rk(euler, 0.08, 1, 1.8, 0.1, ex4_f, 100, 1, 10**-4)


def delta1(x, y, h, function):
    return h * function(x, y)


def delta2(x, y, h, function):
    return h * function(x + h/2, y + delta1(x, y, h, function) / 2)


def delta3(x, y, h, function):
    return h * function(x + h/2, y + delta2(x, y, h, function) / 2)


def delta4(x, y, h, function):
    return h * function(x + h, y + delta3(x, y, h, function))


def delta(x, y, h, function):
    return delta1(x, y, h, function)/6 + delta2(x, y, h, function)/3 + delta3(x, y, h, function)/3 + delta4(x, y, h, function)/6


def rk4(x, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        # print(x, y, _it)
        y += delta(x, y, h, function)
        x += h
        # _it += 1
    # print(x, y, _it)
    return y


def ex4_b_f(u, v):
    return u * (u/2 + 1) * (v**3) + (u + 5/2)* (v**2)


print("RK4:")
qc_value_euler_rk(rk4, 0.16, 1, 2.6, 0.1, ex4_b_f, 1000, 4, 10**-4)


def ex5_z(t, y, z):
    return 0.5 + t**2 + t*z


def ex5_y(t, y, z):
    return z


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


print("EX5:")
print("Euler")
euler_system(0, 8, 0, 1, [ex5_y, ex5_z], 0.25, 10**-4, 2)
print("RK4:")
rk4_system(0, 8, 0, 1, [ex5_y, ex5_z], 0.25, 10**-4, 2)
