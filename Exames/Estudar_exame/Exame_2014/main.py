import math as m


def ex1_v_(t, x, v, k):
    return (-k * x - 1 * v) / 20


def ex1_x_(t, x, v, k):
    return v


def ex1_euler(t, x, v, h, f1, f2, tf, k, error):
    while abs(tf - t) > error:
        t_old = t
        x_old = x
        v_old = v
        t += h
        x += f1(t_old, x_old, v_old, k)*h
        v += f2(t_old, x_old, v_old, k)*h
    print(t, x, v)


ex1_euler(0, 1, 0, 0.1, ex1_x_, ex1_v_, 1.5, 5, 10**-4)
ex1_euler(0, 1, 0, 0.1, ex1_x_, ex1_v_, 1.5, 20, 10**-4)
ex1_euler(0, 1, 0, 0.1, ex1_x_, ex1_v_, 1.5, 40, 10**-4)


def ex2_newton(guess, f, diff, _it):
    it = 0
    while it != _it:
        print(guess, f(guess), it)
        guess = guess - f(guess) / diff(guess)
        it += 1


def ex2_f(x):
    return -x + 40*m.cos(m.sqrt(x)) + 3


def ex2_df(x):
    return -1 - (20*m.sin(m.sqrt(x)) / m.sqrt(x))


ex2_newton(1.7, ex2_f, ex2_df, 3)


B = (m.sqrt(5) - 1) / 2
A = B ** 2


def ex5_f(x):
    return 5*m.cos(x) - m.sin(x)


def ex5(x1, x2, it, function):
    _it = 0
    while it != _it:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        print(_it, x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4))
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
        _it += 1


print("\nEX5:")
ex5(2, 4, 4, ex5_f)


def ex7_f(x):
    return x**4 - 4*x**3 + x - 3


def ex7_g(x):
    return (4*x**3 -x+3)**0.25


def ex7_d(guess, function, it):
    _it = 0
    while _it != it:
        print(_it, guess)
        guess = function(guess)
        _it += 1


ex7_d(3.5, ex7_g, 3)
