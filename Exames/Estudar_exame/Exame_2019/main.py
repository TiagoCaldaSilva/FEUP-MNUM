import math as m


def ex1_f(x):
    return m.sin(x) + x ** 5 - 0.2 * x + 1


def bisection(a, b, function, it):
    _it = 0
    middle = (a + b) / 2
    while _it != it:
        print(_it, a, b)
        middle = (a + b) / 2
        if function(middle) * function(a) < 0:
            b = middle
        else:
            a = middle
        _it += 1
    print(_it, a, b)
    return a, middle


print("EX1:")
a_value, value = bisection(-1, 0, ex1_f, 6)
error_abs = abs(value - a_value)
error_r = error_abs / abs(a_value)
print("Results:")
print(value, error_abs, error_r)


def ex2_f1(x, y):
    return x**2 - y - 1.2


def ex2_df1_dx(x, y):
    return 2*x


def ex2_df1_dy(x, y):
    return -1


def ex2_f2(x, y):
    return -x + y**2 - 1


def ex2_df2_dx(x, y):
    return -1


def ex2_df2_dy(x, y):
    return 2*y


def newton_systems(x, y, f1, df1, f2, df2, it):
    _it = 0
    while _it != it:
        print(_it, x, y)
        x_old = x
        y_old = y
        x -= ((f1(x_old, y_old) * df2[1](x_old, y_old) - f2(x_old, y_old)*df1[1](x_old, y_old)) / (df1[0](x_old, y_old)*df2[1](x_old, y_old) - df1[1](x_old, y_old)*df2[0](x_old, y_old)))
        y -= ((f2(x_old, y_old) * df1[0](x_old, y_old) - f1(x_old, y_old)*df2[0](x_old, y_old)) / (df1[0](x_old, y_old)*df2[1](x_old, y_old) - df1[1](x_old, y_old)*df2[0](x_old, y_old)))
        _it += 1


print("EX2:")
newton_systems(1, 1, ex2_f1, [ex2_df1_dx, ex2_df1_dy], ex2_f2, [ex2_df2_dx, ex2_df2_dy], 3)


def ex3_f(x):
    return m.sqrt(1 + (1.5*m.exp(1.5*x))**2)


def trap(a, b, h, function):
    result = function(a) + function(b)
    while a + h != b:
        a += h
        result += 2 * function(a)
    return result * h / 2


def simpsons(a, b, h, function):
    result = function(a) + function(b)
    i = 1
    while a + h != b:
        a += h
        if i % 2:
            result += 4 * function(a)
        else:
            result += 2 * function(a)
        i += 1
    return result * h / 3


print("EX3:")

_h = 0.25

val = trap(0, 2, _h, ex3_f)
val_ = trap(0, 2, _h / 2, ex3_f)
val__ = trap(0, 2, _h / 4, ex3_f)
print(val, val_, val__, ((val_ - val) / (val__ - val_)), (val__ - val_) / 3)

val = simpsons(0, 2, _h, ex3_f)
val_ = simpsons(0, 2, _h / 2, ex3_f)
val__ = simpsons(0, 2, _h / 4, ex3_f)
print(val, val_, val__, ((val_ - val) / (val__ - val_)), (val__ - val_) / 15)


def ex4_t(t, T):
    return -0.25*(T - 59)


def euler(t, T, h, function, it):
    _it = 0
    while _it != it:
        print(_it, t, T)
        T += function(t, T) * h
        t += t
        _it += 1


print("EX4:")
euler(2, 2, 0.5, ex4_t, 3)


def ex5_f(x):
    return -5*m.cos(x) + m.sin(x) + 10


def max_aurea(x1, x2, function, it):
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    _it = 0
    while _it != it:
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        print(_it, x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4))
        if function(x3) > function(x4):
            x2 = x4
        else:
            x1 = x3
        _it += 1
    print("Amplitude = {}".format(abs(x1-x2)))


print("EX5:")
max_aurea(2, 4, ex5_f, 3)


def ex6_f(x, y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x


def ex6_dfx(x, y):
    return 6*x - y - 8


def ex6_dfy(x, y):
    return -x + 11 + 2*y


def gradient(x, y, f, df, it, l):
    _it = 0
    while _it != it:
        print(_it, x, y, f(x, y), df[0](x, y), df[1](x, y), l)
        x_old = x
        y_old = y
        x -= l * df[0](x_old, y_old)
        y -= l * df[1](x_old, y_old)
        _it += 1


print("EX6:")
gradient(2, 2, ex6_f, [ex6_dfx, ex6_dfy], 2, 1)
