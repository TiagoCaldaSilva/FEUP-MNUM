import math as m


def picard_peano(guess, g, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        print(new_guess, g(new_guess), _it)
        guess = new_guess
        new_guess = g(guess)
        _it += 1
    print(new_guess, g(new_guess), _it)
    return new_guess


def ex2_f(x):
    return 2*m.log(2*x)


picard_peano(0.9, ex2_f, 10**-4, 1)


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
        _it += 1
    # print(x, y, _it)
    return y


def ex3_f(t, x):
    return m.sin(x) + m.sin(2*t)


print("EX3:")
rk4(1, 1.5, 0, ex3_f, 0.5, 10**-4, 100)
rk4(1, 1.5, 0, ex3_f, 0.25, 10**-4, 100)
rk4(1, 1.5, 0, ex3_f, 0.125, 10**-4, 100)


def qc_value_euler_rk(method, h0, x0, xf, y, function, it, order, error):
    s = method(x0, xf, y, function, h0, error, it)
    s_ = method(x0, xf, y, function, h0 / 2, error, it)
    s__ = method(x0, xf, y, function, h0 / 4, error, it)
    qc = (s_ - s) / (s__ - s_)
    while int(qc + 0.5) != 2**order:
        print(qc, h0)
        h0 /= 2
        s = method(x0, xf, y, function, h0, error, it)
        s_ = method(x0, xf, y, function, h0 / 2, error, it)
        s__ = method(x0, xf, y, function, h0 / 4, error, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


qc_value_euler_rk(rk4, 0.5, 1, 1.5, 0, ex3_f, 100, 4, 10**-4)


def gradient(x, y, h, gradient_xy, function, error, it):
    _it = 0
    x_old = x + error * 10
    y_old = y + error * 10
    print(gradient_xy[0](x, y), gradient_xy[1](x, y))
    while (abs(x - x_old) > error or abs(y - y_old) > error) and _it != it:
        print(x, y, function(x, y), _it)
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
    print(x, y, function(x, y), _it)
    return x, y


def ex5_f(x, y):
    return 6*x**2 - x*y + 12*y + y**2 - 8*x


def ex5_fx(x, y):
    return 12*x - y - 8


def ex5_fy(x, y):
    return -x + 12 + 2*y


print("EX5:")
gradient(0, 0, 0.25, [ex5_fx, ex5_fy], ex5_f, 10**-4, 1)