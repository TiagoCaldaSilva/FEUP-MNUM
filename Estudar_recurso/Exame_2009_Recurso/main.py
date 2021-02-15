import math as m

def delta1(x, y, h, function):
    return h * function(x, y)


def delta2(x, y, h, function):
    return h * function(x + h/2, y + delta1(x, y, h, function) / 2)


def delta3(x, y, h, function):
    return h * function(x + h/2, y + delta2(x, y, h, function) / 2)


def delta4(x, y, h, function):
    return h * function(x + h, y + delta3(x, y, h, function))


def delta(x, y, h, function):
    d1 = delta1(x, y, h, function)
    d2 = delta2(x, y, h, function)
    d3 = delta3(x, y, h, function)
    d4 = delta4(x, y, h, function)
    print(d1,d2,d3,d4)
    return d1/6 + d2/3 + d3/3 + d4/6


def rk4(x, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, _it)
        y += delta(x, y, h, function)
        x += h
        _it += 1
    print(x, y, _it)
    return y

def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        _it += 1
    print(x0, y, _it)
    return y


def ex1_f(t, y):
    return y/(t-1)


print("EX1:")
print("euler:")
euler(2, 10, 2, ex1_f, 0.25, 10**-4, 2)
print("rk4:")
rk4(2, 10, 2, ex1_f, 0.25, 10**-4, 2)


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


def ex3_f(x, y):
    return -1.7*x*y + 12*y +7*x**2 - 8*x


def ex3_dx(x, y):
    return -1.7*y + 14*x - 8


def ex3_dy(x, y):
    return -1.7*x + 12


print("EX3:")
gradient(2.4, 4.3, 0.1, [ex3_dx, ex3_dy], ex3_f, 10**-4, 1)


def ex5_1(x, y):
    return x**2 - y - 2


def ex5_2(x, y):
    return -x + y**2 - 2


def ex5_1_dx(x, y):
    return 2*x

def ex5_1_dy(x, y):
    return -1


def ex5_2_dx(x, y):
    return -1


def ex5_2_dy(x, y):
    return 2*y


def newton_system(guess_x, guess_y, function, _gradient, error, it):
    _it = 0
    new_x = guess_x
    new_y = guess_y
    guess_x += error * 10
    guess_y += error * 10
    while (abs(new_x - guess_x) > 0 or abs(new_y - guess_y) > 0) and _it != it:
        print(new_x, new_y, _it)
        guess_x = new_x
        guess_y = new_y
        new_x = guess_x - ((function[0](guess_x, guess_y) * _gradient[1][1](guess_x, guess_y) - function[1](guess_x, guess_y) * _gradient[0][1](guess_x, guess_y)) / (_gradient[0][0](guess_x, guess_y) * _gradient[1][1](guess_x, guess_y) - _gradient[1][0](guess_x, guess_y) * _gradient[0][1](guess_x, guess_y)))
        new_y = guess_y - ((function[1](guess_x, guess_y) * _gradient[0][0](guess_x, guess_y) - function[0](guess_x, guess_y) * _gradient[1][0](guess_x, guess_y)) / (_gradient[0][0](guess_x, guess_y) * _gradient[1][1](guess_x, guess_y) - _gradient[1][0](guess_x, guess_y) * _gradient[0][1](guess_x, guess_y)))
        _it += 1
    print(new_x, new_y, _it)
    return new_x, new_y


print("EX5:")
newton_system(1.5, 0.8, [ex5_1, ex5_2], [[ex5_1_dx, ex5_1_dy], [ex5_2_dx, ex5_2_dy]], 10**-4, 2)

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
    print(s)
    s_ = method(x0, xf, h0 / 2, function, it)
    print(s_)
    s__ = method(x0, xf, h0 / 4, function, it)
    print(s__)
    qc = (s_ - s) / (s__ - s_)
    while int(qc + 0.5) != 2**order:
        h0 /= 2
        s = method(x0, xf, h0, function, it)
        s_ = method(x0, xf, h0 / 2, function, it)
        s__ = method(x0, xf, h0 / 4, function, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


def ex7(x):
    return m.exp(1.5*x)
print("EX7:")
qc_value_s_t(simpson, 0.125, 2.5, 3, ex7, 100, 4)