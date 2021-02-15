import math as m


def ex5_f(x):
    return x**3 + 2*x**2 + 10*x - 17


def ex5_df(x):
    return 3*x**2 + 4*x + 10


def newton(guess, function, diff, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        print(guess, new_guess, function(new_guess), _it)
        guess = new_guess
        new_guess = guess - (function(guess) / diff(guess))
        _it += 1
    print(guess, new_guess, function(guess), _it)
    return new_guess


print("EX5:")
newton(0, ex5_f, ex5_df, 10**-4, 2)


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


def ex6_f1(x, y):
    return y - m.log(x - 1)


def ex6_d1x(x, y):
    return -1/(x- 1)


def ex6_d1y(x, y):
    return 1


def ex6_f2(x, y):
    return y**2 + (x - 3)**2 - 4


def ex6_d2x(x, y):
    return 2*(x - 3)


def ex6_d2y(x, y):
    return 2*y


print("EX6:")
newton_system(1.5, 1.3, [ex6_f1, ex6_f2], [[ex6_d1x, ex6_d1y], [ex6_d2x, ex6_d2y]], 10**-4, 2)
