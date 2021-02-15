import math as m


def ex1(guess, function, diff, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        print(guess, new_guess, function(guess), _it)
        guess = new_guess
        new_guess = guess - (function(guess) / diff(guess))
        _it += 1
    return new_guess


def ex1_f(x):
    return (x - 2.6) + (m.cos(x + 1.1))**3


def ex1_df1(x):
    return 1 - 3*((m.cos(x + 1.1)) ** 2)*m.sin(x + 1.1)


print("EX1:")
ex1(1.8, ex1_f, ex1_df1, 10**-4, 2)


def ex4_f(x):
    return 5*m.cos(x)-m.sin(x)


def ex4(x1, x2, function, error, it):
    _it = 0
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    while abs(x1 - x2) > error and _it != it:
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        print(x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4), _it)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
        _it += 1
    print("Amplitude = {}" .format(abs(x1-x2)))
    return x1, x2


print("EX2:")
ex4(2, 4, ex4_f, 10**-4, 3)


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


def ex5(x, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, _it)
        y += delta(x, y, h, function)
        x += h
        _it += 1
    print(x, y, _it)
    return y


def ex5_f(t, x):
    return m.sin(x) + m.sin(2*t)


print("EX5:")
ex5(1, 1.5, 1, ex5_f, 0.5, 10**-4, 10)
print("2a")
ex5(1, 1.5, 1, ex5_f, 0.5 / 2, 10**-4, 10)
print("3a")
ex5(1, 1.5, 1, ex5_f, 0.5 / 4, 10**-4, 10)


def qc_value_euler_rk(method, h0, x0, xf, y, function, it, order, error):
    s = method(x0, xf, y, function, h0, error, it)
    s_ = method(x0, xf, y, function, h0 / 2, error, it)
    s__ = method(x0, xf, y, function, h0 / 4, error, it)
    qc = (s_ - s) / (s__ - s_)
    print("QC= {}".format(qc))
    while int(qc + 0.5) != 2**order:
        h0 /= 2
        s = method(x0, xf, y, function, h0, error, it)
        s_ = method(x0, xf, y, function, h0 / 2, error, it)
        s__ = method(x0, xf, y, function, h0 / 4, error, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


qc_value_euler_rk(ex5, 0.5, 1, 1.5, 1, ex5_f, 10, 4, 10**-4)