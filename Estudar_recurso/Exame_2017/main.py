import math as m


def aurea(x1, x2, function, error, it):
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
    print(x1, x2, _it)
    # print("Amplitude = {}".format(abs(x1 - x2)))
    return x1, x2


def ex1_f(x):
    return (x - 5)**2 + x**4


print("EX1:")
aurea(0, 3, ex1_f, 10**-4, 100)


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
    print(h0, h0/2, h0/4)
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


def ex2_f(x):
    return m.sqrt(1 + ((2.5*m.exp(2.5*x)) ** 2))


print("EX2:")
print("Trap")
qc_value_s_t(trap, 0.125, 0, 1, ex2_f, 100, 2)
print("simpson")
qc_value_s_t(simpson, 0.125, 0, 1, ex2_f, 100, 4)


def newton(guess, function, diff, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        # print(guess, new_guess, function(new_guess), _it)
        guess = new_guess
        new_guess = guess - (function(guess) / diff(guess))
        _it += 1
    print(guess, new_guess, function(guess), _it)
    return new_guess


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


def ex3_newton_f(x):
    return m.exp(x) - x - 5


def ex3_newton_df(x):
    return m.exp(x) - 1


def ex3_picard_peano_f(x):
    return m.log(5 + x)


print("EX3:")
print("Newton:")
newton(1.8, ex3_newton_f, ex3_newton_df, 10**-4, 100)
print("Picard-peano:")
picard_peano(1.8, ex3_picard_peano_f, 10**-4, 100)


def euler_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        # print(x, y, z, _it)
        y_old = y
        y += functions[0](x, y, z) * h
        z += functions[1](x, y_old, z) * h
        x += h
        _it += 1
    # print(x, y, z, _it)
    return y, z


def ex4_fC(t, T, C):
    return -m.exp(-0.5/(T+273))*C


def ex4_fT(t, T, C):
    return 30 * m.exp(-0.5/(T+273))*C - 0.5*(T-20)


print("EX4:")
print("Euler:")
euler_system(0, 0.5, 25, 2.5, [ex4_fT, ex4_fC], 0.25, 10**-4, 8)


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


print("rk4:")
rk4_system(0, 8, 25, 2.5, [ex4_fT, ex4_fC], 0.25, 10**-4, 2)


def qc_value_euler_rk_system(method, h0, x0, xf, y, z, functions, it, order, error):
    _y, _z = method(x0, xf, y, z, functions, h0, error, it)
    y_, z_ = method(x0, xf, y, z, functions, h0 / 2, error, it)
    y__, z__ = method(x0, xf, y, z, functions, h0 / 4, error, it)
    qcy = (y_ - _y) / (y__ - y_)
    qcz = (z_ - _z) / (z__ - z_)
    print(_y, h0)
    print(y_, h0/2)
    print(y__, h0/4)
    print(qcy)
    # while int(qcy + 0.5) != 2**order or int(qcz + 0.5) != 2**order:
    #     h0 /= 2
    #     _y, _z = method(x0, xf, y, z, functions, h0, error, it)
    #     y_, z_ = method(x0, xf, y, z, functions, h0 / 2, error, it)
    #     y__, z__ = method(x0, xf, y, z, functions, h0 / 4, error, it)
    #     qcy = (y_ - _y) / (y__ - y_)
    #     qcz = (z_ - _z) / (z__ - z_)

    error_y = (y__ - y_) / (2**order - 1)
    error_z = (z__ - z_) / (2 ** order - 1)
    print("qcy = {} | erro absoluto estimado y = {} | h = {}" .format(qcy, error_y, h0))
    # print("qcz = {} | erro absoluto estimado z = {} | h = {}" .format(qcz, error_z, h0))
    print("erro relativo estimado y = {}" .format(error / y__))
    # print("erro relativo estimado z = {}".format(error / z__))


print("qc:")
qc_value_euler_rk_system(euler_system, 0.25, 0, 0.5, 25, 2.5, [ex4_fT, ex4_fC], 8, 1, 10**-4)


def gradient(x, y, h, gradient_xy, function, error, it):
    _it = 0
    x_old = x + error * 10
    y_old = y + error * 10
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


def ex5_f(x, y):
    return -1.1*x*y + 12*y + 7*x**2 - 8*x


def ex5_fx(x, y):
    return -1.1*y + 14*x - 8


def ex5_fy(x, y):
    return -1.1*x + 12


print("EX5:")
gradient(3, 1, 0.1, [ex5_fx, ex5_fy], ex5_f, 10**-4, 1)