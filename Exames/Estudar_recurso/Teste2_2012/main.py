import math as m


def cubatura(x0, xf, y0, yf):
    hx = (xf - x0) / 2
    hy = (yf - y0) / 2
    soma_vertices = 1.1 + 6.3 + 1.2 + 2.6
    soma_medios = 2.1 + 1.5 + 2.2 + 1.4
    centro = 4.9
    result = (hx * hy) / 9 * (soma_vertices + 4 * soma_medios + 16 * centro)
    print(result)


print("EX1:")
cubatura(0, 1.8, 0, 1.8)


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
        x = (b[0] - matrix[0][1] * y0 - matrix[0][2] * z0 - matrix[0][3] * t0) / matrix[0][0]
        y = (b[1] - matrix[1][0] * x - matrix[1][2] * z0 - matrix[1][3] * t0) / matrix[1][1]
        z = (b[2] - matrix[2][0] * x - matrix[2][1] * y - matrix[2][3] * t0) / matrix[2][2]
        t = (b[3] - matrix[3][0] * x - matrix[3][1] * y - matrix[3][2] * z) / matrix[3][3]
        _it += 1
    print(x, y, z, t, _it)
    return x, y, z, t


print("EX2:")
gauss_seidel_4(0, 0, 0, 0, [[4.8, -1, -1, 1], [-1, 4.8, 1, -1], [-1, 2, 4.8, -1], [2, -1, -1, 4.8]],
               [1, -1, -1, 0], 10 ** -4, 2)


def ex4_f(u, v):
    return u*(u/2 + 1)*(v**3) + (u + 5/2)*(v**2)


def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        # print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        # _it += 1
    # print(x0, y, _it)
    return y


def qc_value_euler_rk(method, h0, x0, xf, y, function, it, order, error):
    s = method(x0, xf, y, function, h0, error, it)
    s_ = method(x0, xf, y, function, h0 / 2, error, it)
    s__ = method(x0, xf, y, function, h0 / 4, error, it)
    qc = (s_ - s) / (s__ - s_)
    print(s, h0)
    print(s_, h0/2)
    print(s__, h0/4)
    print(qc)
    while int(qc + 0.5) != 2**order:
        h0 /= 2
        s = method(x0, xf, y, function, h0, error, it)
        s_ = method(x0, xf, y, function, h0 / 2, error, it)
        s__ = method(x0, xf, y, function, h0 / 4, error, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


print("EX4:")
qc_value_euler_rk(euler, 0.08, 1, 1.8, 0.1, ex4_f, 100, 1, 10**-4)
