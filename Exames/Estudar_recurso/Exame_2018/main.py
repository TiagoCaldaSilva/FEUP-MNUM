import math as m


def ex1_f1(x, y):
    return m.sin(x + y) - m.exp(x - y)


def ex1_f1x(x, y):
    return m.cos(y + x) - m.exp(x - y)


def ex1_f1y(x, y):
    return m.cos(x + y) + m.exp(x - y)


def ex1_f2(x, y):
    return m.cos(x + y) - x**2 * y**2


def ex1_f2x(x, y):
    return -m.sin(y + x) - 2* x * y**2


def ex1_f2y(x, y):
    return -m.sin(x + y) - 2 * y * x**2


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


print("EX1:")
newton_system(0.5, 0.25, [ex1_f1, ex1_f2], [[ex1_f1x, ex1_f1y], [ex1_f2x, ex1_f2y]], 10**-4, 2)


def cubatura():
    x0 = 0
    xf = 2
    y0 = 0
    yf = 2
    hx = (xf - x0) / 2
    hy = (yf - y0) / 2
    soma_vertices = 1.1 + 7.8 + 9.8 + 1.2
    soma_medios = 2.1 + 1.5 + 1.4 + 2.2
    centro = 4
    result = (hx * hy) / 9 * (soma_vertices + 4*soma_medios + 16*centro)
    print(result)


print("EX3:")
cubatura()


def euler_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, z, _it)
        y_old = y
        y += functions[0](x, y, z) * h
        z += functions[1](x, y_old, z) * h
        x += h
        _it += 1
    print(x, y, z, _it)
    return y, z


def ex4_y(x, y, z):
    return z


def ex4_z(x, y, z):
    return -7*z - 4*y


print("EX4:")
euler_system(0.4, 1, 2, 1, [ex4_y, ex4_z], 0.2, 10**-4, 1000)
