import math as m


def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        _it += 1
    print(x0, y, _it)
    return y


def ex1_f(t, x):
    return -0.25*(x - 37)


euler(5, 1000, 3, ex1_f, 0.4, 10**-4, 2)


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


def ex4_f(x):
    return 2*m.log(2*x)


print("EX4:")
picard_peano(1.1, ex4_f, 10**-4, 1)


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
    # while int(qc + 0.5) != 2**order:
    #     h0 /= 2
    #     s = method(x0, xf, h0, function, it)
    #     s_ = method(x0, xf, h0 / 2, function, it)
    #     s__ = method(x0, xf, h0 / 4, function, it)
    #     qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


def ex5_f(x):
    return m.sqrt(1 + ((2.5*m.exp(2.5*x))**2))


print("EX5:")
print("Trap")
qc_value_s_t(trap, 0.125, 0, 1, ex5_f, 100, 2)
print("Simpson")
qc_value_s_t(simpson, 0.125, 0, 1, ex5_f, 100, 4)


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
    print(a, b, _it)
    return middle


def ex7_f(x):
    return x**3 - 10*m.sin(x) + 2.8


print("EX7:")
bisection(1.5, 4.2, 2, 10**-4, ex7_f)
