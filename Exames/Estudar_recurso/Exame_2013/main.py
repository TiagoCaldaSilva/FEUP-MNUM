import math as m


def ex1_dfy(t, y, z):
    return z


def ex1_dfz(t, y, z):
    return 0.5 + t**2 + t*z


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

print("EX1:")
print("Euler:")
euler_system(0, 8, 0, 1, [ex1_dfy, ex1_dfz], 0.25, 10**-4, 2)
print("Rk4:")
rk4_system(0, 8, 0, 1, [ex1_dfy, ex1_dfz], 0.25, 10**-4, 2)


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


def ex3_f(x, y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x


def ex3_fx(x, y):
    return 6*x - y - 8


def ex3_fy(x, y):
    return -x + 11 + 2*y


print("EX3:")
gradient(2, 2, 0.5, [ex3_fx, ex3_fy], ex3_f, 10**-4, 1)


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


def ex4_f(x):
    return m.exp(1.5*x)


def qc_value_s_t(method, h0, x0, xf, function, it, order):
    s = method(x0, xf, h0, function, it)
    s_ = method(x0, xf, h0 / 2, function, it)
    s__ = method(x0, xf, h0 / 4, function, it)
    qc = (s_ - s) / (s__ - s_)
    print(s, s_, s__, qc)
    while int(qc + 0.5) != 2**order:
        h0 /= 2
        s = method(x0, xf, h0, function, it)
        s_ = method(x0, xf, h0 / 2, function, it)
        s__ = method(x0, xf, h0 / 4, function, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


print("EX4:")
qc_value_s_t(simpson, 0.125, 1, 1.5, ex4_f, 100, 4)


def newton(guess, function, diff, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        print(guess, new_guess, function(guess), _it)
        guess = new_guess
        new_guess = guess - (function(guess) / diff(guess))
        _it += 1
    print(guess, new_guess, function(guess), _it)
    return new_guess


def ex5_f(x):
    return (x - 3.7) + (m.cos(x + 1.2))**3


def ex5_df(x):
    return 1 - 3 * ((m.cos(x + 1.2))**2) * m.sin(x + 1.2)


print("EX5:")
newton(3.8, ex5_f, ex5_df, 10**-4, 1)
