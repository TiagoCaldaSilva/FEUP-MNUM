import math as m


def ex1_f(x):
    return (x - 2.6) + (m.cos(x + 1.1))**3


def ex1_df(x):
    return 1 - 3 * (m.cos(x + 1.1)**2)*m.sin(x + 1.1)


def ex1(guess, function, diff, it):
    _it = 0
    while _it != it:
        print(guess, function(guess), _it)
        guess = guess - function(guess) / diff(guess)
        _it += 1


ex1(1.8, ex1_f, ex1_df, 2)


def ex4_f(x):
    return 5*m.cos(x) - m.sin(x)


B = (m.sqrt(5) - 1) / 2
A = B**2


def ex4_aurea(x1, x2, function, it):
    _it = 0
    while _it != it:
        _it += 1
        x3 = x1 + A*(x2 - x1)
        x4 = x1 + B*(x2 - x1)
        print(x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4),_it)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
    print("Final: [{}, {}] -> Amplitude = {}".format(x1, x2, x2 - x1))


ex4_aurea(2, 4, ex4_f, 3)


def ex5_f(t, x):
    return m.sin(x) + m.sin(2*t)


def d1(t, x, h, function):
    return h * function(t, x)


def d2(t, x, h, function):
    return h * function(t + h / 2, x + d1(t, x, h, function) / 2)


def d3(t, x, h, function):
    return h * function(t + h / 2, x + d2(t, x, h, function) / 2)


def d4(t, x, h, function):
    return h * function(t + h, x + d3(t, x, h, function))


def delta(t, x, h, function):
    return d1(t, x, h, function)/6 + d2(t, x, h, function)/3 + d3(t, x, h, function)/3 + d4(t, x, h, function)/6


def ex5_rk4(t, x, tf, h, function):
    while t != tf:
        print(t, x)
        x += delta(t, x, h, function)
        t += h
    print(t, x)
    return x


print("S:")
value = ex5_rk4(1, 1, 1.5, 0.5, ex5_f)
print("S':")
value_ = ex5_rk4(1, 1, 1.5, 0.5 / 2, ex5_f)
print("S'':")
value__ = ex5_rk4(1, 1, 1.5, 0.5 / 4, ex5_f)
print("QC = {}" .format((value_ - value) / (value__ - value_)))
