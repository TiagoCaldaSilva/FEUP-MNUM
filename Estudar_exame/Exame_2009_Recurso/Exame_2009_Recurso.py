import math as m


def ex1_f(t, y):
    return y / (t - 1)


def ex1_euler(t, y, tf, h, function, it):
    _it = 0
    while _it != it:
        print(_it, y, t)
        y += h * function(t, y)
        t += h
        _it += 1


print("EX1 EULER:")
ex1_euler(2, 2, 10, 0.25, ex1_f, 3)


def d1(t, y, h, function):
    return h * function(t, y)


def d2(t, y, h, function):
    return h * function(t + h / 2, y + d1(t, y, h, function) / 2)


def d3(t, y, h, function):
    return h * function(t + h / 2, y + d2(t, y, h, function) / 2)


def d4(t, y, h, function):
    return h * function(t + h, y + d3(t, y, h, function))


def delta(t, y, h, function):
    return d1(t, y, h, function) / 6 + d2(t, y, h, function) / 3 + d3(t, y, h, function) / 3 + d4(t, y, h, function) / 6


def ex1_rk2(t, y, tf, h, function, it):
    _it = 0
    while _it != it:
        print(_it, t, y, d1(t, y, h, function), d2(t, y, h, function), d3(t, y, h, function), d4(t, y, h, function))
        y += delta(t, y, h, function)
        t += h
        _it += 1


print("EX1 RK2:")
ex1_rk2(2, 2, 10, 0.25, ex1_f, 3)


def ex3_f(x, y):
    return -1.7 * x * y + 12 * y + 7 * x ** 2 - 8 * x


def ex3_dx(x, y):
    return -1.7 * y + 14 * x - 8


def ex3_dy(x, y):
    return -1.7 * x + 12


def ex3_gradient(x, y, h, function, gradient):
    x_old = x
    y_old = y
    x = x_old - h * gradient[0](x_old, y_old)
    y = y_old - h * gradient[1](x_old, y_old)
    print(x, y, function(x, y))


print("EX3")
ex3_gradient(2.4, 4.3, 0.1, ex3_f,  [ex3_dx, ex3_dy])


def ex5_f1(x, y):
    return x**2 - y - 2


def ex5_f2(x, y):
    return -x + y**2 - 2


def ex5_f1x(x, y):
    return 2*x


def ex5_f1y(x, y):
    return -1


def ex5_f2x(x, y):
    return -1


def ex5_f2y(x, y):
    return 2*y


def ex5_newton(x, y, f1, df1, f2, df2, it):
    _it = 0
    while _it != it:
        print(_it, x, y)
        x_old = x
        y_old = y
        x = x_old - (f1(x_old, y_old) * df2[1](x_old, y_old) - f2(x_old, y_old)*df1[1](x_old, y_old))/((df1[0](x_old, y_old)*df2[1](x_old, y_old)) - df2[0](x_old, y_old)*df1[1](x_old, y_old))
        y = y_old - (f2(x_old, y_old) * df1[0](x_old, y_old) - f1(x_old, y_old)*df2[0](x_old, y_old))/((df1[0](x_old, y_old)*df2[1](x_old, y_old)) - df2[0](x_old, y_old)*df1[1](x_old, y_old))
        _it += 1


print("EX5")
ex5_newton(1.5, 0.8, ex5_f1, [ex5_f1x, ex5_f1y], ex5_f2, [ex5_f2x, ex5_f2y], 3)


def ex7_function(x):
    return m.exp(1.5 * x)


def ex7_simpsons(a, b, h, function):
    result = function(a) + function(b)
    _it = 1
    while (a + h) < b:
        a += h
        if _it % 2:
            result += 4 * function(a)
        else:
            result += 2 * function(a)
        _it += 1
    print(a, b, result * h / 3)
    return result * h / 3


print("EX7")

value = ex7_simpsons(2.5, 3, 0.125, ex7_function)
value_ = ex7_simpsons(2.5, 3, 0.125 / 2, ex7_function)
value__ = ex7_simpsons(2.5, 3, 0.125 / 4, ex7_function)
print((value_ - value) / (value__ - value_))
print((value__ - value_) / 15 / value__)
