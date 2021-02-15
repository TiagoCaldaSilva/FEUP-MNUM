import math as m


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


def ex1_f1(x, y):
    return x**2 - y - 1.2


def ex1_f2(x, y):
    return -x + y**2 - 1


def ex1_f1x(x, y):
    return 2*x


def ex1_f1y(x, y):
    return -1


def ex1_f2x(x, y):
    return -1


def ex1_f2y(x, y):
    return 2*y


print("EX2:")
newton_system(1, 1, [ex1_f1, ex1_f2], [[ex1_f1x, ex1_f1y], [ex1_f2x, ex1_f2y]], 10**-4, 2)


def rope(a, b, it, error, function):
    _it = 0
    w = 0
    while abs(function(a) - function(b)) > error and _it != it:
        w = (a * function(b) - b * function(a)) / (function(b) - function(a))
        print(a, b, w, function(a), function(b), function(w), _it)
        if function(a) * function(w) < 0:
            b = w
        else:
            a = w
        _it += 1
    w = (a * function(b) - b * function(a)) / (function(b) - function(a))
    print(a, b, w, function(a), function(b), function(w), _it)
    return w


def ex4_f(x):
    return x**7 + 0.5*x - 0.5


print("EX4:")
rope(0, 0.8, 3, 10**-4, ex4_f)


def ex5_fy(t, y, z):
    return z


def ex5_fz(t, y, z):
    return 0.5 + t**2 + t*z


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
    return y


def delta1_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x, y, z)
    return h * function[1](x, y, z)


def delta2_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h/2, y + delta1_system(x, y, z, h, function, char) / 2, z + delta1_system(x, y, z, h, function, 'z') / 2)
    return h * function[1](x + h/2, y + delta1_system(x, y, z, h, function, 'y') / 2, z + delta1_system(x, y, z, h, function, char) / 2)


def delta3_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h/2, y + delta2_system(x, y, z, h, function, char) / 2, z + delta2_system(x, y, z, h, function, 'z') / 2)
    return h * function[1](x + h/2, y + delta2_system(x, y, z, h, function, 'y') / 2, z + delta2_system(x, y, z, h, function, char) / 2)


def delta4_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h, y + delta3_system(x, y, z, h, function, char), z + delta3_system(x, y, z, h, function, 'z'))
    return h * function[1](x + h, y + delta3_system(x, y, z, h, function, 'y'), z + delta3_system(x, y, z, h, function, char))


def delta_system(x, y, z, h, function, char):
    return delta1_system(x, y, z, h, function, char)/6 + delta2_system(x, y, z, h, function, char)/3 + delta3_system(x, y, z, h, function, char)/3 + delta4_system(x, y, z, h, function, char)/6


def rk4_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, z, _it)
        y_old = y
        y += delta_system(x, y_old, z, h, functions, 'y')
        z += delta_system(x, y_old, z, h, functions, 'z')
        x += h
        _it += 1
    print(x, y, z, _it)
    return y, z


print("EX5:")
print("Euler")
euler_system(0, 10, 0, 1, [ex5_fy, ex5_fz], 0.25, 10**-4, 2)
print("RK4:")
rk4_system(0, 10, 0, 1, [ex5_fy, ex5_fz], 0.25, 100**-4, 2)


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
    print(s, s_, s__, qc)
    # while int(qc + 0.5) != 2**order:
    #     h0 /= 2
    #     s = method(x0, xf, h0, function, it)
    #     s_ = method(x0, xf, h0 / 2, function, it)
    #     s__ = method(x0, xf, h0 / 4, function, it)
    #     qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


def ex6_f(x):
    return m.sqrt(1 + ((1.5*m.exp(1.5*x))**2))


print("EX6:")
print("trap")
qc_value_s_t(trap, 0.5, 0, 2, ex6_f, 100, 2)
print("simpsons")
qc_value_s_t(simpson, 0.5, 0, 2, ex6_f, 100, 4)
