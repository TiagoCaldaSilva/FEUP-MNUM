import math as m


def ex1_f(x):
    return m.sin(x) + x**5 - 0.2*x + 1


def bisection(a, b, it, error, function):
    middle = (b + a) / 2
    _it = 0
    while abs(b - a) > error and _it != it:
        print(a, b, _it)
        middle = (b + a) / 2
        if function(a) * function(middle) < 0:
            b = middle
        else:
            a = middle
        _it += 1
    print(a, b, middle, _it)
    print("Erro absoluto/Amplitude = {}" .format(a - b))
    print("Erro relativo = {}" .format((a-b)/middle))
    return middle


print("EX1:")
bisection(-1, 0, 6, 10**-4, ex1_f)


def newton_system(guess_x, guess_y, function, gradient, error, it):
    _it = 0
    new_x = guess_x
    new_y = guess_y
    guess_x += error * 10
    guess_y += error * 10
    while (abs(new_x - guess_x) > 0 or abs(new_y - guess_y) > 0) and _it != it:
        print(new_x, new_y, _it)
        guess_x = new_x
        guess_y = new_y
        new_x = guess_x - ((function[0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - function[1](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)) / (gradient[0][0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - gradient[1][0](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)))
        new_y = guess_y - ((function[1](guess_x, guess_y) * gradient[0][0](guess_x, guess_y) - function[0](guess_x, guess_y) * gradient[1][0](guess_x, guess_y)) / (gradient[0][0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - gradient[1][0](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)))
        _it += 1
    print(new_x, new_y, _it)
    return new_x, new_y


def ex2_1(x, y):
    return x**2 - y - 1.2


def ex2_2(x, y):
    return -x + y**2 - 1


def ex2_d1x(x, y):
    return 2*x


def ex2_d1y(x, y):
    return -1


def ex2_d2x(x, y):
    return -1


def ex2_d2y(x, y):
    return 2*y


print("EX2:")
newton_system(1, 1, [ex2_1, ex2_2], [[ex2_d1x, ex2_d1y], [ex2_d2x, ex2_d2y]], 10**-4, 2)


def trap(x0, xf, h, function, it):
    _it = 1
    result = function(x0) + function(xf)
    x0 += h
    while x0 != xf and _it != it:
        result += 2*function(x0)
        x0 += h
        # _it += 1
    return result * h/2


def simpson(x0, xf, h, function, it):
    _it = 1
    result = function(x0) + function(xf)
    x0 += h
    while x0 != xf and _it != it:
        if _it % 2:
            result += 4 * function(x0)
        else:
            result += 2 * function(x0)
        x0 += h
        _it += 1
    return result * h/3


def qc_value_s_t(method, h0, x0, xf, function, it, order):
    s = method(x0, xf, h0, function, it)
    s_ = method(x0, xf, h0 / 2, function, it)
    s__ = method(x0, xf, h0 / 4, function, it)
    qc = (s_ - s) / (s__ - s_)
    print(s, h0)
    print(s_, h0/2)
    print(s__, h0/4)
    while int(qc + 0.5) != 2**order:
        print(h0)
        h0 /= 2
        s = method(x0, xf, h0, function, it)
        s_ = method(x0, xf, h0 / 2, function, it)
        s__ = method(x0, xf, h0 / 4, function, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


def ex3_f(x):
    return m.sqrt(1 + ((1.5*m.exp(1.5*x))**2))


print("EX3:")
print("Trap:")
qc_value_s_t(trap, 0.25, 0, 2, ex3_f, 1000, 2)
print("Simpson:")
qc_value_s_t(simpson, 0.25, 0, 2, ex3_f, 1000, 4)


def ex4_f(t, T):
    return -0.25*(T - 59)


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
euler(2, 8, 2, ex4_f, 0.5, 10**-4, 2)


def ex5_f(x):
    return -5 * m.cos(x) + m.sin(x) + 10


def aurea(x1, x2, function, error, it):
    _it = 0
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    while abs(x1 - x2) > error and _it != it:
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        print(x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4), _it)
        if function(x3) > function(x4):
            x2 = x4
        else:
            x1 = x3
        _it += 1
    print(x1, x2, _it)
    print("Amplitude = {}".format(abs(x1 - x2)))
    return x1, x2


print("EX5:")
aurea(2, 4, ex5_f, 10**-4, 3)


def gradient(x, y, h, gradient_xy, function, error, it):
    _it = 0
    x_old = x + error * 10
    y_old = y + error * 10
    while (abs(x - x_old) > error or abs(y - y_old) > error) and _it != it:
        print(x, y, function(x, y), gradient_xy[0](x, y), gradient_xy[1](x, y), _it)
        x_old = x
        y_old = y
        x -= h * gradient_xy[0](x_old, y_old)
        y -= h * gradient_xy[1](x_old, y_old)
        if function(x, y) < function(x_old, y_old):
            h *= 2
        else:
            h /= 2
            x = x_old
            y = y_old
            x_old += error * 10
            y_old += error * 10
        _it += 1
    print(x, y, function(x, y), gradient_xy[0](x, y), gradient_xy[1](x, y), _it)
    return x, y


def ex6_f(x, y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x


def ex6_dfx(x, y):
    return 6*x - y - 8


def ex6_dfy(x, y):
    return -x + 11 + 2*y


print("EX6:")
gradient(2, 2, 1, [ex6_dfx, ex6_dfy], ex6_f, 10**-4, 1)
