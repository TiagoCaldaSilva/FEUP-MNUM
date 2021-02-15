import math as m


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


print("EX1:")
gauss_jacobi_4(0.25, 0.25, 0.25, 0.25, [[4.5, -1, -1, 1], [-1, 4.5, 1, -1], [-1, 2, 4.5, -1], [2, -1, -1, 4.5]], [1, -1, -1, 0], 10**-4, 2)


def ex2_f(t, x):
    return m.sin(2*x)+m.sin(2*t)


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
        print(x, y, _it)
        y += delta(x, y, h, function)
        x += h
        # _it += 1
    print(x, y, _it)
    return y


def qc_value_euler_rk(method, h0, x0, xf, y, function, it, order, error):
    s = method(x0, xf, y, function, h0, error, it)
    s_ = method(x0, xf, y, function, h0 / 2, error, it)
    s__ = method(x0, xf, y, function, h0 / 4, error, it)
    qc = (s_ - s) / (s__ - s_)
    # print(s, h0)
    # print(s_, h0/2)
    # print(s__, h0/4)
    print(qc)
    while int(qc + 0.5) != 2**order:
        h0 /= 2
        s = method(x0, xf, y, function, h0, error, it)
        s_ = method(x0, xf, y, function, h0 / 2, error, it)
        s__ = method(x0, xf, y, function, h0 / 4, error, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    # print("erro relativo estimado = {}" .format(error / s__))


print("EX2:")
print("rk4 values:")
rk4(1, 1.5, 1, ex2_f, 0.5/4, 10**-4, 100)
print("qc:")
qc_value_euler_rk(rk4, 0.5, 1, 1.5, 1, ex2_f, 100, 4, 10**-4)
