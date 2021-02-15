import math as m


def ex1_dv(t, y, v):
    return 0.5 + t**2 + t*v


def ex1_dy(t, y, v):
    return v


def ex1_euler(t, y, v, h, diff_f1, diff_f2, it):
    _it = 0
    while _it != it:
        print(_it, t, y, v)
        y_old = y
        v_old = v
        y += h * diff_f1(t, y_old, v_old)
        v += h * diff_f2(t, y_old, v_old)
        t += h
        _it += 1


print("EX1 EULER:")
ex1_euler(0, 0, 1, 0.25, ex1_dy, ex1_dv, 3)


def d1(t, y, v, char, h, diff_f1, diff_f2):
    if char == 'y':
        return h * diff_f1(t, y, v)
    return h * diff_f2(t, y, v)


def d2(t, y, v, char, h, diff_f1, diff_f2):
    if char == 'y':
        return h * diff_f1(t + h / 2, y + d1(t, y, v, char, h, diff_f1, diff_f2) / 2, v + d1(t, y, v, 'v', h, diff_f1, diff_f2) / 2)
    return h * diff_f2(t + h / 2, y + d1(t, y, v, 'y', h, diff_f1, diff_f2) / 2, v + d1(t, y, v, char, h, diff_f1, diff_f2) / 2)


def d3(t, y, v, char, h, diff_f1, diff_f2):
    if char == 'y':
        return h * diff_f1(t + h / 2, y + d2(t, y, v, char, h, diff_f1, diff_f2) / 2, v + d2(t, y, v, 'v', h, diff_f1, diff_f2) / 2)
    return h * diff_f2(t + h / 2, y + d2(t, y, v, 'y', h, diff_f1, diff_f2) / 2, v + d2(t, y, v, char, h, diff_f1, diff_f2) / 2)


def d4(t, y, v, char, h, diff_f1, diff_f2):
    if char == 'y':
        return h * diff_f1(t + h, y + d3(t, y, v, char, h, diff_f1, diff_f2), v + d3(t, y, v, 'v', h, diff_f1, diff_f2))
    return h * diff_f2(t + h, y + d3(t, y, v, 'y', h, diff_f1, diff_f2), v + d3(t, y, v, char, h, diff_f1, diff_f2))


def delta(t, y, v, char, h, diff_f1, diff_f2):
    return d1(t, y, v, char, h, diff_f1, diff_f2) / 6 + d2(t, y, v, char, h, diff_f1, diff_f2) / 3 + d3(t, y, v, char, h, diff_f1, diff_f2) / 3 + d4(t, y, v, char, h, diff_f1, diff_f2) / 6


def ex1_rk4(t, y, v, h, diff_f1, diff_f2, it):
    _it = 0
    while _it != it:
        print(_it, t, y, v, h)
        y_old = y
        v_old = v
        y += delta(t, y_old, v_old, 'y', h, diff_f1, diff_f2)
        v += delta(t, y_old, v_old, 'v', h, diff_f1, diff_f2)
        t += h
        _it += 1


print("EX1 RK4:")
ex1_rk4(0, 0, 1, 0.25, ex1_dy, ex1_dv, 3)


def ex3_f(x, y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x


def ex3_f_x(x, y):
    return 6*x - y - 8


def ex3_f_y(x, y):
    return -x + 11 + 2 * y


def ex3_gradient(x, y, h, function, gradient, it):
    _it = 0
    while _it != it:
        print(_it, x, y, function(x, y), gradient[0](x, y), gradient[1](x, y))
        x_old = x
        y_old = y
        x -= h * gradient[0](x_old, y_old)
        y -= h * gradient[1](x_old, y_old)
        _it += 1


print("EX3:")
ex3_gradient(2, 2, 0.5, ex3_f, [ex3_f_x, ex3_f_y], 2)


def ex4_f(x):
    return m.exp(1.5*x)


def ex4_simpson(x, xf, h, function):
    result = function(x) + function(xf)
    it_ = 1
    x += h
    while x != xf:
        if it_ % 2:
            result += 4 * function(x)
        else:
            result += 2 * function(x)
        x += h
        it_ += 1
    return result * h / 3


print("EX4:")
h_ = 0.125
value = ex4_simpson(1, 1.5, h_, ex4_f)
value_ = ex4_simpson(1, 1.5, h_ / 2, ex4_f)
value__ = ex4_simpson(1, 1.5, h_ / 4, ex4_f)
print(value, value_, value__)
print((value_ - value) / (value__ - value_))
print((value__ - value_) / 15)


def ex5_f(x):
    return (x - 3.7) + (m.cos(x + 1.2))**3


def ex5_f_diff(x):
    return 1 - 3*(m.cos (x + 1.2)**2) * m.sin(x + 1.2)


def ex5_newton(guess, function, diff, it):
    _it = 0
    while _it != it:
        print(_it, guess)
        guess -= function(guess) / diff(guess)
        _it += 1


print("EX5:")
ex5_newton(3.8, ex5_f, ex5_f_diff, 2)
