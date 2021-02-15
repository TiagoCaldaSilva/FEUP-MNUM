import math as m


def ex1_f(x):
    return m.exp(0.7*x) - x**2 - 0.5


def bisection(a, b, it, error, function):
    middle = (b + a) / 2
    _it = 0
    while abs(b - a) > error and _it != it:
        middle = (b + a) / 2
        print(a, b, (b + a) / 2, function(a), function(b), function(middle), _it)
        if function(a) * function(middle) < 0:
            b = middle
        else:
            a = middle
        _it += 1
    print(a, b, (b + a) / 2, function(a), function(b), function(middle), _it)
    print("Erro absoluto/Amplitude = {}" .format(a - b))
    # print("Erro relativo = {}" .format((a-b)/middle))
    return middle


print("EX1:")
bisection(-1, 0, 2, 10**-4, ex1_f)


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


def ex2_f1(x, y):
    return x**2 - y - 1.2


def ex2_df1x(x, y):
    return 2*x


def ex2_df1y(x, y):
    return -1


def ex2_f2(x, y):
    return -x + y**2 - 0.5


def ex2_df2x(x, y):
    return -1


def ex2_df2y(x, y):
    return 2*y


print("EX2:")
newton_system(1.1, 1.1, [ex2_f1, ex2_f2], [[ex2_df1x, ex2_df1y], [ex2_df2x, ex2_df2y]], 10**-4, 2)
