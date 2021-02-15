import math as m


def ex1_f1(x, y):
    return x ** 2 - y - 1.2


def ex1_f2(x, y):
    return -x + y ** 2 - 1


def ex1_df1_dx(x, y):
    return 2*x


def ex1_df1_dy(x, y):
    return -1


def ex1_df2_dx(x, y):
    return -1


def ex1_df2_dy(x, y):
    return 2*y


def ex1_newton(x, y, f1, df1, f2, df2, it):
    _it = 0
    while _it != it:
        print(_it, x, y)
        x_old = x
        y_old = y
        x = x_old - (f1(x_old, y_old)*df2[1](x_old, y_old) - f2(x_old, y_old)*df1[1](x_old, y_old))/(df1[0](x_old, y_old)*df2[1](x_old, y_old) - df2[0](x_old, y_old)*df1[1](x_old, y_old))
        y = y_old - (f2(x_old, y_old)*df1[0](x_old, y_old) - f1(x_old, y_old)*df2[0](x_old, y_old))/(df1[0](x_old, y_old)*df2[1](x_old, y_old) - df2[0](x_old, y_old)*df1[1](x_old, y_old))
        _it += 1


print("EX1:")
ex1_newton(1, 1, ex1_f1, [ex1_df1_dx, ex1_df1_dy], ex1_f2, [ex1_df2_dx, ex1_df2_dy], 3)


def ex4_f(x):
    return x**7 + 0.5*x - 0.5


def ex4_rope(a, b, function, it):
    _it = 0
    x = 0
    while _it != it:
        print(_it, a, b, x)
        x = (a*function(b) - b*function(a)) / (function(b) - function(a))
        if function(a) * function(x) < 0:
            b = x
        else:
            a = x
        _it += 1


print("EX4:")
ex4_rope(0, 0.8, ex4_f, 4)


def ex5_f_v(t, y, v):
    return 0.5 + t**2 +t*v


def ex5_f_y(t, y, v):
    return v


def euler(t, y, v, fy, fv, h, it):
    _it = 0
    while _it != it:
        print(_it, t, y, v)
        y_old = y
        y += fy(t, y, v)*h
        v += fv(t, y_old, v)*h
        t += h
        _it += 1


print("EX5:")
euler(0, 0, 1, ex5_f_y, ex5_f_v, 0.25, 3)


def d1(t, y, v, h, fy, fv, c):
    if c == 'y':
        return h * fy(t, y, v)
    return h * fv(t, y, v)


def d2(t, y, v, h, fy, fv, c):
    if c == 'y':
        return h * fy(t + h / 2, y + d1(t, y, v, h, fy, fv, 'y') / 2, v + d1(t, y, v, h, fy, fv, 'v') / 2)
    return h * fv(t + h / 2, y + d1(t, y, v, h, fy, fv, 'y') / 2, v + d1(t, y, v, h, fy, fv, 'v') / 2)


def d3(t, y, v, h, fy, fv, c):
    if c == 'y':
        return h * fy(t + h / 2, y + d2(t, y, v, h, fy, fv, 'y') / 2, v + d2(t, y, v, h, fy, fv, 'v') / 2)
    return h * fv(t + h / 2, y + d2(t, y, v, h, fy, fv, 'y') / 2, v + d2(t, y, v, h, fy, fv, 'v') / 2)


def d4(t, y, v, h, fy, fv, c):
    if c == 'y':
        return h * fy(t + h, y + d3(t, y, v, h, fy, fv, 'y'), v + d3(t, y, v, h, fy, fv, 'v'))
    return h * fv(t + h, y + d3(t, y, v, h, fy, fv, 'y'), v + d3(t, y, v, h, fy, fv, 'v'))


def delta(t, y, v, h, fy, fv, c):
    return d1(t, y, v, h, fy, fv, c) / 6 + d2(t, y, v, h, fy, fv, c) / 3 + d3(t, y, v, h, fy, fv, c) / 3 + d4(t, y, v, h, fy, fv, c) / 6


def rk4(t, y, v, h, fy, fv, it):
    _it = 0
    while _it != it:
        print(_it, t, y)
        y_old = y
        y += delta(t, y, v, h, fy, fv, 'y')
        v += delta(t, y_old, v, h, fy, fv, 'z')
        t += h
        _it += 1


print("EX5, RK4:")
rk4(0, 0, 1, 0.25, ex5_f_y, ex5_f_v, 3)


def ex6_f(x):
    return m.sqrt(1 + ((1.5 * m.exp(1.5 * x))**2))


def trap(a, b, h, function):
    result = function(a) + function(b)
    while (a + h) != b:
        a += h
        result += function(a) * 2
    return result * h / 2


def simpson(a, b, h, function):
    result = function(a) + function(b)
    i = 1
    while (a + h) != b:
        a += h
        if i % 2:
            result += function(a) * 4
        else:
            result += function(a) * 2
        i += 1
    return result * h / 3


_h = 0.5
value = trap(0, 2, _h, ex6_f)
value_ = trap(0, 2, _h / 2, ex6_f)
value__ = trap(0, 2, _h / 4, ex6_f)
print(value, value_, value__, ((value_ - value) / (value__ - value_)), (value__ - value_) / 3)

_h = 0.5
value = simpson(0, 2, _h, ex6_f)
value_ = simpson(0, 2, _h / 2, ex6_f)
value__ = simpson(0, 2, _h / 4, ex6_f)
print(value, value_, value__, ((value_ - value) / (value__ - value_)), (value__ - value_) / 15)
