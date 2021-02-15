import math as m


def picard_peano(guess, g, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        # print(new_guess, g(new_guess), _it)
        guess = new_guess
        new_guess = g(guess)
        _it += 1
    print(new_guess, g(new_guess), _it)
    return new_guess


def ex1_g(x):
    return 1/0.645


print("EX1:")
picard_peano(1, ex1_g, 10**-4, 5)


def newton_system(guess_x, guess_y, function, gradient, error, it):
    _it = 0
    new_x = guess_x
    new_y = guess_y
    guess_x += error * 10
    guess_y += error * 10
    while (abs(new_x - guess_x) > 0 or abs(new_y - guess_y) > 0) and _it != it:
        # print(new_x, new_y, _it)
        guess_x = new_x
        guess_y = new_y
        new_x = guess_x - ((function[0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - function[1](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)) / (gradient[0][0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - gradient[1][0](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)))
        new_y = guess_y - ((function[1](guess_x, guess_y) * gradient[0][0](guess_x, guess_y) - function[0](guess_x, guess_y) * gradient[1][0](guess_x, guess_y)) / (gradient[0][0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - gradient[1][0](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)))
        _it += 1
    print(new_x, new_y, _it)
    return new_x, new_y


def ex3_1(x, y):
    return 1 - x**2 - y


def ex3_d1x(x, y):
    return -2*x


def ex3_d1y(x, y):
    return -1


def ex3_2(x, y):
    return 0.7 + x - y


def ex3_d2x(x, y):
    return 1


def ex3_d2y(x, y):
    return -1


print("EX3:")
print("Newton:")
newton_system(1, 2, [ex3_1, ex3_2], [[ex3_d1x, ex3_d1y], [ex3_d2x, ex3_d2y]], 10**-3, 100)


def picard_peano_system(guess_x, guess_y, g, error, it):
    _it = 0
    new_x = guess_x
    new_y = guess_y
    guess_x += error * 10
    guess_y += error * 10
    while (abs(new_x - guess_x) > 0 or abs(new_y - guess_y) > 0) and _it != it:
        # print(new_x, new_y, _it)
        guess_x = new_x
        guess_y = new_y
        new_x = g[0](guess_x, guess_y)
        new_y = g[1](guess_x, guess_y)
        _it += 1
    print(new_x, new_y, _it)
    return new_x, new_y


def ex3_pp1_x(x, y):
    return -m.sqrt(1 - y)


def ex3_pp1_y(x, y):
    return 0.7 + x


def ex3_pp2_x(x, y):
    return y - 0.7


def ex3_pp2_y(x, y):
    return 1 - x**2


print("PP1:")
picard_peano_system(0, 0.5, [ex3_pp1_x, ex3_pp1_y], 10**-3, 100)
print("PP2:")
picard_peano_system(0, 0.5, [ex3_pp2_x, ex3_pp2_y], 10**-3, 100)
print("Newton teste:")
newton_system(0, 0.5, [ex3_1, ex3_2], [[ex3_d1x, ex3_d1y], [ex3_d2x, ex3_d2y]], 10**-3, 100)
