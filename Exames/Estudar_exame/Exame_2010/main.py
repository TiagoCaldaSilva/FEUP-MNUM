import math as m


def ex1_f(x):
    return 2 * m.log(2 * x)


def ex1(x, function, it):
    _it = 0
    while it != _it:
        print(_it, x)
        x = function(x)
        _it += 1


ex1(0.9, ex1_f, 2)
print("residuos = {}" .format(1.1755733298042381 - 0.9))


def ex3_f(x, t):
    return m.sin(t) + m.sin(2 * x)


def d1(x, t, h, function):
    return h * function(x, t)


def d2(x, t, h, function):
    return h * function(x + h / 2, t + d1(x, t, h, function) / 2)


def d3(x, t, h, function):
    return h * function(x + h / 2, t + d2(x, t, h, function) / 2)


def d4(x, t, h, function):
    return h * function(x + h, t + d3(x, t, h, function))


def delta(x, t, h, function):
    return d1(x, t, h, function) / 6 + d2(x, t, h, function) / 3 + d3(x, t, h, function) / 3 + d4(x, t, h, function) / 6


def ex3_rk4_a(x, t, h, function, it):
    _it = 0
    while _it != it:
        print(_it, x, t)
        t += delta(x, t, h, function)
        x += h
        _it += 1


print("EX3: 1ª")
ex3_rk4_a(1, 0, 0.5, ex3_f, 2)
print("EX3: 2ª")
ex3_rk4_a(1, 0, 0.5 / 2, ex3_f, 3)
print("EX3: 3ª")
ex3_rk4_a(1, 0, 0.5 / 4, ex3_f, 5)


def ex3_rk4_b(x, t, h, function, it):
    _it = 0
    while _it != it:
        print(_it, x, t)
        t += delta(x, t, h, function)
        x += h
        _it += 1
    return t


result = ex3_rk4_b(1, 0, 0.5, ex3_f, 1)
result_ = ex3_rk4_b(1, 0, 0.5 / 2, ex3_f, 2)
result__ = ex3_rk4_b(1, 0, 0.5 / 4, ex3_f, 4)
qc = (result_ - result) / (result__ - result_)
print(qc)
result = ex3_rk4_b(1, 0, 0.5 / 8, ex3_f, 1)
result_ = ex3_rk4_b(1, 0, 0.5 / 16, ex3_f, 2)
result__ = ex3_rk4_b(1, 0, 0.5 / 32, ex3_f, 4)
qc = (result_ - result) / (result__ - result_)
print(qc, 0.5/8)


def ex5_f(x, y):
    return 6*x**2 - x*y + 12*y + y**2 - 8 *x


def ex5_fdy(x, y):
    return -x + 12 + 2 * y


def ex5_fdx(x, y):
    return 12 * x - y - 8


def ex5_gradient(x, y, h, function, gradient, it):
    _it = 0
    while _it != it:
        print(_it, x, y, function(x, y), gradient[0](x, y), gradient[1](x, y))
        x_old = x
        y_old = y
        _it += 1
        x = x_old - h * gradient[0](x_old, y_old)
        y = y_old - h * gradient[1](x_old, y_old)


ex5_gradient(0, 0, 0.25, ex5_f, [ex5_fdx, ex5_fdy], 2)


